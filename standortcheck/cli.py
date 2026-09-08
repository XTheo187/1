"""Kommandozeile von Standortcheck."""

from __future__ import annotations

import argparse
import csv
import sqlite3
import sys
from datetime import date, timedelta
from pathlib import Path
from typing import Any

from . import audit as audit_modul
from . import branchen, db, discover, konfig, outreach, planner, report, scoring

BERICHTE_ORDNER = Path("berichte")
ANSPRACHE_ORDNER = Path("ansprache")


# --------------------------------------------------------------------------
# Ausgabehilfen
# --------------------------------------------------------------------------

def kopf(text: str) -> None:
    print(f"\n{text}\n{'=' * min(len(text), 72)}")


def euro(betrag: float) -> str:
    return f"{betrag:,.0f}".replace(",", ".").replace("-", "−") + " EUR"


def tabelle(spalten: list[str], zeilen: list[list[Any]], rechts: set[int] | None = None) -> None:
    if not zeilen:
        print("  (keine Einträge)")
        return
    rechts = rechts or set()
    alle = [spalten] + [[str(z) for z in zeile] for zeile in zeilen]
    breiten = [max(len(str(r[i])) for r in alle) for i in range(len(spalten))]
    def zeile_form(werte: list[str]) -> str:
        return "  " + "  ".join(
            str(w).rjust(breiten[i]) if i in rechts else str(w).ljust(breiten[i])
            for i, w in enumerate(werte)
        )
    print(zeile_form(spalten))
    print("  " + "  ".join("-" * b for b in breiten))
    for zeile in zeilen:
        print(zeile_form([str(z) for z in zeile]))


def balken(anteil: float, breite: int = 24) -> str:
    gefuellt = int(max(0.0, min(1.0, anteil)) * breite)
    return "█" * gefuellt + "·" * (breite - gefuellt)


# --------------------------------------------------------------------------
# Befehle
# --------------------------------------------------------------------------

def cmd_einrichten(args: argparse.Namespace) -> int:
    daten = konfig.laden(args.konfig)
    kopf("Einrichtung")
    print("Diese Angaben stehen auf Berichten und Briefen. Leer lassen = unverändert.\n")
    felder = [
        ("name", "Ihr Name / Firmenname"),
        ("strasse", "Straße und Hausnummer"),
        ("ort", "PLZ und Ort"),
        ("telefon", "Telefon"),
        ("email", "E-Mail"),
    ]
    for schluessel, frage in felder:
        aktuell = daten["absender"].get(schluessel, "")
        eingabe = input(f"  {frage} [{aktuell}]: ").strip()
        if eingabe:
            daten["absender"][schluessel] = eingabe

    satz = input(f"  Stundensatz in EUR [{daten['stundensatz']:.0f}]: ").strip()
    if satz:
        try:
            daten["stundensatz"] = float(satz.replace(",", "."))
        except ValueError:
            print("  ! Keine Zahl, Wert bleibt unverändert.")

    pfad = konfig.speichern(daten, args.konfig)
    print(f"\nGespeichert in {pfad}")

    with db.session(args.db) as con:
        if db.summe(con, "SELECT COUNT(*) FROM ausgaben") == 0:
            antwort = input("\nStartbudget von 500 EUR als Ausgabenplan anlegen? [j/N]: ")
            if antwort.strip().lower().startswith("j"):
                for posten, betrag, kategorie, _ in planner.BUDGET_500:
                    if betrag > 0:
                        db.ausgabe_buchen(con, posten, betrag, kategorie)
                print("  Budgetposten gebucht. Ändern mit: standortcheck ausgabe ...")
    return 0


def cmd_branchen(args: argparse.Namespace) -> int:
    kopf("Branchenkatalog")
    zeilen = [
        [b.schluessel, b.bezeichnung, euro(b.projektpreis_eur),
         euro(b.betreuung_eur) + "/M", euro(b.kundenwert_eur)]
        for b in branchen.liste()
    ]
    tabelle(["Schlüssel", "Branche", "Projekt", "Betreuung", "Kundenwert"],
            zeilen, rechts={2, 3, 4})
    print("\n  Kundenwert = was ein Neukunde dem Betrieb wert ist. Das ist das")
    print("  Argument im Gespräch: Die Investition rechnet sich ab Auftrag Nr. 1.")
    return 0


def cmd_suchen(args: argparse.Namespace) -> int:
    schluessel = args.branche or [b.schluessel for b in branchen.liste()[:5]]
    kopf(f"Recherche: {args.ort} (Umkreis {args.radius:.0f} km)")
    print(f"Branchen: {', '.join(schluessel)}")
    print("Quelle  : OpenStreetMap (ODbL). Bitte den Freiwilligendienst schonen.")

    try:
        lat, lon, anzeige = discover.ort_aufloesen(args.ort)
    except discover.RechercheFehler as e:
        print(f"\n  ! {e}", file=sys.stderr)
        return 1
    print(f"Gefunden: {anzeige}\n")

    neu = bekannt = 0
    with db.session(args.db) as con:
        try:
            for lead in discover.suchen(
                args.ort, schluessel, radius_km=args.radius, koordinaten=(lat, lon)
            ):
                lead_id, ist_neu = db.lead_speichern(con, lead)
                if ist_neu:
                    neu += 1
                    marke = "neu"
                else:
                    bekannt += 1
                    marke = "bekannt"
                if args.ausfuehrlich:
                    print(f"  [{marke:7}] {lead['name'][:44]:44} {lead.get('website', '')[:34]}")
        except discover.RechercheFehler as e:
            print(f"\n  ! {e}", file=sys.stderr)
            if neu == 0:
                return 1

    print(f"\n  {neu} neue Leads, {bekannt} bereits bekannt.")
    if neu + bekannt == 0:
        print("  Keine Treffer. In OpenStreetMap sind nicht alle Betriebe erfasst –")
        print("  größeren Radius versuchen (--radius 25) oder weitere Branchen wählen.")
    else:
        print("  Nächster Schritt: standortcheck pruefen --alle")
    return 0


def cmd_pruefen(args: argparse.Namespace) -> int:
    with db.session(args.db) as con:
        leads = db.leads_holen(
            con, ort=args.ort, ungeprueft=not args.erneut, limit=args.limit
        )
        if not leads:
            print("  Keine Leads zu prüfen. Erst recherchieren: standortcheck suchen --ort ...")
            return 0

        kopf(f"Audit: {len(leads)} Leads")
        for i, row in enumerate(leads, 1):
            lead = dict(row)
            website = lead.get("website") or ""
            print(f"  [{i:>3}/{len(leads)}] {lead['name'][:40]:40} ", end="", flush=True)
            try:
                ergebnis = audit_modul.pruefen(website, lead, http_check=not args.schnell)
            except Exception as e:
                print(f"Fehler: {type(e).__name__}")
                continue

            db.audit_speichern(con, lead["id"], ergebnis)
            p = scoring.prioritaet(lead, ergebnis)
            db.lead_aktualisieren(
                con, lead["id"], deal_wert=p["deal_wert"],
                stage="geprueft" if lead["stage"] == "neu" else lead["stage"],
            )
            con.commit()
            print(
                f"Score {ergebnis['schmerz_score']:>3} | "
                f"Prio {p['prioritaet']:>3} | {len(ergebnis['befunde'])} Befunde"
            )

    print("\n  Nächster Schritt: standortcheck liste")
    return 0


def _lead_mit_audit(con: sqlite3.Connection, row: sqlite3.Row) -> tuple[dict, dict | None, dict]:
    lead = dict(row)
    a = db.letztes_audit(con, lead["id"])
    p = scoring.prioritaet(lead, a)
    return lead, a, p


def cmd_liste(args: argparse.Namespace) -> int:
    with db.session(args.db) as con:
        rows = db.leads_holen(con, stage=args.stufe, ort=args.ort)
        eintraege = []
        for row in rows:
            lead, a, p = _lead_mit_audit(con, row)
            eintraege.append({
                "id": lead["id"], "name": lead["name"], "ort": lead.get("ort") or "",
                "stage": lead["stage"], "telefon": "ja" if lead.get("telefon") else "-",
                "score": (a or {}).get("schmerz_score", 0),
                "prioritaet": p["prioritaet"], "wert": p["deal_wert"],
            })

    eintraege = scoring.rangliste(eintraege)[: args.limit]
    kopf(f"Leads nach Priorität ({len(eintraege)} von {len(rows)})")
    tabelle(
        ["ID", "Betrieb", "Ort", "Stufe", "Tel", "Score", "Prio", "Wert"],
        [[e["id"], e["name"][:32], e["ort"][:16], e["stage"], e["telefon"],
          e["score"], e["prioritaet"], f"{e['wert']:.0f}"] for e in eintraege],
        rechts={5, 6, 7},
    )
    return 0


def cmd_bericht(args: argparse.Namespace) -> int:
    einstellungen = konfig.laden(args.konfig)
    if not konfig.absender_vollstaendig(einstellungen):
        print("  ! Absenderdaten fehlen. Erst ausführen: standortcheck einrichten")
        return 1

    ordner = Path(args.ordner or BERICHTE_ORDNER)
    with db.session(args.db) as con:
        if args.lead:
            rows = [r for r in (db.lead_holen(con, i) for i in args.lead) if r]
        else:
            rows = db.leads_holen(con, stage=args.stufe, ort=args.ort)
            bewertet = []
            for row in rows:
                lead, a, p = _lead_mit_audit(con, row)
                if a:
                    bewertet.append((p["prioritaet"], row))
            rows = [r for _, r in sorted(bewertet, key=lambda x: -x[0])][: args.limit]

        if not rows:
            print("  Keine passenden Leads mit Audit gefunden.")
            return 0

        kopf(f"Berichte erzeugen ({len(rows)})")
        for row in rows:
            lead, a, p = _lead_mit_audit(con, row)
            if not a:
                print(f"  übersprungen (kein Audit): {lead['name']}")
                continue
            satz = einstellungen["stundensatz"]
            html = report.bericht_erzeugen(
                lead, a, einstellungen["absender"],
                angebot=scoring.angebot(lead, a, satz),
                stundensatz=satz,
            )
            ziel = report.schreiben(ordner / report.dateiname(lead), html)
            print(f"  {ziel}")

    print("\n  Zum Versenden: Datei im Browser öffnen und über „Drucken → Als PDF")
    print("  sichern“ ausgeben. Kein zusätzliches Werkzeug nötig.")
    return 0


def cmd_ansprache(args: argparse.Namespace) -> int:
    einstellungen = konfig.laden(args.konfig)
    if not konfig.absender_vollstaendig(einstellungen):
        print("  ! Absenderdaten fehlen. Erst ausführen: standortcheck einrichten")
        return 1

    ordner = Path(args.ordner or ANSPRACHE_ORDNER)
    ordner.mkdir(parents=True, exist_ok=True)
    absender = einstellungen["absender"]

    with db.session(args.db) as con:
        if args.lead:
            rows = [r for r in (db.lead_holen(con, i) for i in args.lead) if r]
        else:
            bewertet = []
            for row in db.leads_holen(con, stage=args.stufe or "geprueft", ort=args.ort):
                lead, a, p = _lead_mit_audit(con, row)
                if a:
                    bewertet.append((p["prioritaet"], row))
            rows = [r for _, r in sorted(bewertet, key=lambda x: -x[0])][: args.limit]

        if not rows:
            print("  Keine passenden Leads gefunden.")
            return 0

        kopf(f"Ansprache erzeugen ({len(rows)})")
        for row in rows:
            lead, a, _ = _lead_mit_audit(con, row)
            if not a:
                continue
            basis = f"{lead['id']:04d}"
            erzeuger = {
                "telefon": (outreach.telefonleitfaden, "leitfaden.txt"),
                "brief": (outreach.brief, "brief.txt"),
                "mail": (outreach.nachfass_mail, "nachfass-mail.txt"),
            }
            arten = [args.art] if args.art != "alle" else list(erzeuger)
            for art in arten:
                fn, endung = erzeuger[art]
                ziel = ordner / f"{basis}-{endung}"
                ziel.write_text(fn(lead, a, absender), encoding="utf-8")
                print(f"  {ziel}")

    if args.art in ("mail", "alle"):
        print("\n  ! Die Nachfass-E-Mail erst nach einem geführten Gespräch senden.")
        print("    Kalte Werbe-E-Mails sind nach § 7 Abs. 2 Nr. 2 UWG unzulässig.")
    return 0


def cmd_stufe(args: argparse.Namespace) -> int:
    if args.stufe not in db.STAGES:
        print(f"  ! Unbekannte Stufe. Möglich: {', '.join(db.STAGES)}")
        return 1
    with db.session(args.db) as con:
        lead = db.lead_holen(con, args.lead)
        if not lead:
            print(f"  ! Lead {args.lead} nicht gefunden.")
            return 1
        felder: dict[str, Any] = {"stage": args.stufe}
        if args.notiz:
            bisher = lead["notiz"] or ""
            felder["notiz"] = f"{bisher}\n[{db.heute()}] {args.notiz}".strip()
        if args.umsatz is not None:
            felder["umsatz"] = args.umsatz
        if args.wert is not None:
            felder["deal_wert"] = args.wert
        if args.faellig:
            felder["faellig_am"] = args.faellig
        if args.naechster:
            felder["naechster_schritt"] = args.naechster
        db.lead_aktualisieren(con, args.lead, **felder)
        db.aktivitaet_buchen(
            con, art=f"stufe:{args.stufe}", minuten=args.minuten or 0,
            lead_id=args.lead, notiz=args.notiz,
        )
        print(f"  {lead['name']}: {lead['stage']} → {args.stufe}")
        if args.umsatz:
            print(f"  Umsatz gebucht: {euro(args.umsatz)}")
    return 0


def cmd_zeit(args: argparse.Namespace) -> int:
    with db.session(args.db) as con:
        db.aktivitaet_buchen(
            con, art=args.art, minuten=args.minuten, lead_id=args.lead, notiz=args.notiz
        )
        gesamt = db.summe(con, "SELECT SUM(minuten) FROM aktivitaeten") / 60
        woche = db.summe(
            con, "SELECT SUM(minuten) FROM aktivitaeten WHERE am >= ?",
            ((date.today() - timedelta(days=7)).isoformat(),),
        ) / 60
    print(f"  {args.minuten} Minuten auf '{args.art}' gebucht.")
    print(f"  Diese Woche: {woche:.1f} h von 20 h  {balken(woche / 20)}")
    print(f"  Insgesamt  : {gesamt:.1f} h")
    return 0


def cmd_ausgabe(args: argparse.Namespace) -> int:
    with db.session(args.db) as con:
        db.ausgabe_buchen(con, args.posten, args.betrag, args.kategorie)
        gesamt = db.summe(con, "SELECT SUM(betrag) FROM ausgaben")
    einstellungen = konfig.laden(args.konfig)
    kapital = einstellungen.get("startkapital", 500.0)
    rest = kapital - gesamt
    print(f"  Gebucht: {args.posten} – {euro(args.betrag)}")
    print(f"  Verbraucht: {euro(gesamt)} von {euro(kapital)}  {balken(gesamt / kapital)}")
    if rest < 0:
        print(f"  ! Startkapital überschritten um {euro(abs(rest))}")
    else:
        print(f"  Verbleibend: {euro(rest)}")
    return 0


def cmd_kennzahlen(args: argparse.Namespace) -> int:
    einstellungen = konfig.laden(args.konfig)
    with db.session(args.db) as con:
        k = planner.kennzahlen(con)

    kopf("Kennzahlen")
    print(f"  Umsatz            {euro(k['umsatz']):>14}")
    print(f"  Ausgaben          {euro(k['ausgaben']):>14}")
    print(f"  Ergebnis          {euro(k['gewinn']):>14}")
    print(f"  Arbeitszeit       {k['stunden']:>10.1f} h")
    print(f"  Stundenlohn       {k['stundenlohn']:>10.2f} EUR/h")
    print(f"  Offene Pipeline   {euro(k['offene_pipeline']):>14}")
    if k["ausgaben"]:
        print(f"  Kapitalrendite    {k['roi_startkapital']:>10.2f} x")

    kopf("Trichter")
    gesamt = max(k["leads_gesamt"], 1)
    for stufe in db.STAGES:
        anzahl = k["verteilung"][stufe]
        print(f"  {stufe:<13} {anzahl:>4}  {balken(anzahl / gesamt)}")
    print(f"\n  Kontaktquote     {k['kontaktquote']:>6.1f} %")
    print(f"  Abschlussquote   {k['abschlussquote']:>6.1f} %")
    if k["umsatz_je_gewonnen"]:
        print(f"  Umsatz je Auftrag {euro(k['umsatz_je_gewonnen'])}")

    if k["zeit_nach_art"]:
        kopf("Zeitverwendung")
        tabelle(["Aktivität", "Stunden"],
                [[art, f"{h:.1f}"] for art, h in k["zeit_nach_art"].items()], rechts={1})

    a = planner.Annahmen(stunden_pro_woche=einstellungen.get("stunden_pro_woche", 20.0))
    kopf("Nächste Schritte")
    for i, rat in enumerate(planner.empfehlung(k, a), 1):
        print(f"  {i}. {rat}")
    return 0


def cmd_plan(args: argparse.Namespace) -> int:
    einstellungen = konfig.laden(args.konfig)
    kapital = args.kapital or einstellungen.get("startkapital", 500.0)
    stunden = args.stunden or einstellungen.get("stunden_pro_woche", 20.0)
    a = planner.Annahmen(stunden_pro_woche=stunden)

    kopf(f"Startkapital: {euro(kapital)}")
    summe_plan = sum(b for _, b, _, _ in planner.BUDGET_500)
    tabelle(
        ["Posten", "Betrag", "Kategorie"],
        [[p, euro(b), kat] for p, b, kat, _ in planner.BUDGET_500],
        rechts={1},
    )
    print(f"\n  Summe: {euro(summe_plan)}")
    print("\n  Begründungen:")
    for posten, _, _, warum in planner.BUDGET_500:
        print(f"    {posten}\n      {warum}")

    kopf("Bewusst nicht gekauft")
    for posten, warum in planner.NICHT_KAUFEN:
        print(f"  ✗ {posten}\n      {warum}")

    kopf(f"Wochenmodell bei {stunden:.0f} Stunden")
    optimal = planner.briefe_optimieren(a)
    print(f"  Optimale Briefmenge je Woche: {optimal['briefe']}")
    print(f"  → mehr Briefe erzeugen mehr Aufträge, als in {stunden:.0f} h umsetzbar sind\n")
    tabelle(
        ["Stufe", "Anzahl"],
        [["Briefe versendet", optimal["briefe"]],
         ["davon erreicht", optimal["erreicht"]],
         ["echte Gespräche", optimal["gespraeche"]],
         ["Angebote", optimal["angebote"]],
         ["Aufträge", optimal["abschluesse"]]],
        rechts={1},
    )
    print("\n  Zeitaufteilung:")
    for posten, h in optimal["zeit"].items():
        print(f"    {posten:<22} {h:>5.1f} h  {balken(h / stunden, 18)}")
    print(f"    {'Gesamt':<22} {optimal['zeit_gesamt']:>5.1f} h von {stunden:.0f} h")

    print(f"\n  Umsatz je Woche          {euro(optimal['umsatz_woche']):>12}")
    print(f"  Akquisekosten je Woche   {euro(optimal['kosten_woche']):>12}")
    print(f"  Deckungsbeitrag je Woche {euro(optimal['deckungsbeitrag_woche']):>12}")
    print(f"  Effektiver Stundenlohn   {optimal['stundensatz_effektiv']:>8} EUR/h")
    print(f"  Hochrechnung Monat       {euro(optimal['umsatz_monat']):>12}")
    print(f"  Wiederkehrend nach 12 M. {euro(optimal['wiederkehrend_nach_12m']):>12} pro Monat")

    kopf("Drei Szenarien")
    sz = planner.szenarien(a)
    tabelle(
        ["Szenario", "Briefe/W", "Aufträge/W", "Umsatz/Monat", "EUR/Stunde"],
        [[name, e["briefe"], f'{e["abschluesse"]:.2f}',
          euro(e["umsatz_monat"]), e["stundensatz_effektiv"]]
         for name, e in sz.items()],
        rechts={1, 2, 3, 4},
    )
    print("\n  „vorsichtig“ ist die Zahl, mit der geplant werden sollte.")
    print("  „gut“ tritt erst ein, wenn Gespräch und Preis eingespielt sind –")
    print("  erfahrungsgemäß nicht vor dem dritten Monat.")

    kopf("Reichweite des Akquisebudgets")
    r = planner.startkapital_reichweite(a, budget_akquise=200.0)
    print(f"  200 EUR Porto und Druck reichen für {r['briefe_moeglich']} Briefe.")
    print(f"  Erwartete Aufträge daraus : {r['erwartete_abschluesse']}")
    print(f"  Erwarteter Umsatz         : {euro(r['erwarteter_umsatz'])}")
    print(f"  Akquisekosten je Auftrag  : {euro(r['kosten_je_abschluss'])}")
    print(f"  Verhältnis Umsatz/Einsatz : {r['rendite']} zu 1")

    print("\n  Die Zahlen sind Annahmen, keine Zusage. Nach 100 versendeten")
    print("  Briefen die eigenen Ist-Quoten aus 'standortcheck kennzahlen'")
    print("  einsetzen – dann rechnet das Modell mit der Wirklichkeit.")
    return 0


def cmd_tagesplan(args: argparse.Namespace) -> int:
    with db.session(args.db) as con:
        k = planner.kennzahlen(con)
        faellig = list(con.execute(
            "SELECT * FROM leads WHERE faellig_am IS NOT NULL AND faellig_am <= ? "
            "AND stage NOT IN ('gewonnen','verloren') ORDER BY faellig_am",
            (db.heute(),),
        ))
        eintraege = []
        for row in db.leads_holen(con, stage="geprueft"):
            lead, a, p = _lead_mit_audit(con, row)
            if a and lead.get("telefon"):
                eintraege.append({**lead, **p})
        top = scoring.rangliste(eintraege)[: args.anzahl]

    kopf(f"Tagesplan {date.today().strftime('%d.%m.%Y')}")

    if faellig:
        print("  Wiedervorlagen fällig:\n")
        tabelle(
            ["ID", "Betrieb", "Stufe", "Seit", "Nächster Schritt"],
            [[r["id"], r["name"][:26], r["stage"], r["faellig_am"],
              (r["naechster_schritt"] or "")[:30]] for r in faellig],
        )
        print()

    if top:
        print(f"  Beste {len(top)} Anrufe heute:\n")
        tabelle(
            ["ID", "Betrieb", "Telefon", "Prio", "Wert", "Aufhänger"],
            [[e["id"], e["name"][:24], (e.get("telefon") or "")[:16], e["prioritaet"],
              f"{e['deal_wert']:.0f}", (e["begruendung"][0] if e["begruendung"] else "")[:28]]
             for e in top],
            rechts={3, 4},
        )
        ids = " ".join(str(e["id"]) for e in top)
        print("\n  Leitfäden erzeugen:")
        print(f"    standortcheck ansprache --art telefon --lead {ids}")
    else:
        print("  Keine anrufbereiten Leads (geprüft + Rufnummer bekannt).")

    print()
    for rat in planner.empfehlung(k, planner.Annahmen())[:3]:
        print(f"  → {rat}")
    return 0


def cmd_export(args: argparse.Namespace) -> int:
    ziel = Path(args.datei)
    with db.session(args.db) as con:
        rows = db.leads_holen(con, stage=args.stufe, ort=args.ort)
        zeilen = []
        for row in rows:
            lead, a, p = _lead_mit_audit(con, row)
            zeilen.append({
                "id": lead["id"], "name": lead["name"], "branche": lead.get("branche", ""),
                "strasse": lead.get("strasse", ""), "plz": lead.get("plz", ""),
                "ort": lead.get("ort", ""), "telefon": lead.get("telefon", ""),
                "email": lead.get("email", ""), "website": lead.get("website", ""),
                "stufe": lead["stage"], "score": (a or {}).get("schmerz_score", ""),
                "prioritaet": p["prioritaet"], "deal_wert": p["deal_wert"],
                "umsatz": lead.get("umsatz", 0),
                "befunde": "; ".join(b["titel"] for b in (a or {}).get("befunde", [])[:5]),
            })
    if not zeilen:
        print("  Keine Daten zum Exportieren.")
        return 0
    with ziel.open("w", newline="", encoding="utf-8-sig") as f:
        schreiber = csv.DictWriter(f, fieldnames=list(zeilen[0]), delimiter=";")
        schreiber.writeheader()
        schreiber.writerows(zeilen)
    print(f"  {len(zeilen)} Leads exportiert nach {ziel}")
    return 0


# --------------------------------------------------------------------------
# Argumente
# --------------------------------------------------------------------------

def parser_bauen() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="standortcheck",
        description="Lead-Recherche, Website-Audit und Vertriebssteuerung "
                    "für lokale Dienstleistung.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Typischer Ablauf:
  standortcheck einrichten
  standortcheck plan
  standortcheck suchen --ort Regensburg --branche dachdecker sanitaer
  standortcheck pruefen --alle
  standortcheck liste
  standortcheck bericht --limit 20
  standortcheck ansprache --art alle --limit 20
  standortcheck tagesplan
  standortcheck stufe 12 gewonnen --umsatz 1900
  standortcheck kennzahlen
""",
    )
    p.add_argument("--db", default=str(db.DEFAULT_DB), help="Pfad zur Datenbank")
    p.add_argument("--konfig", default=str(konfig.DEFAULT_PFAD), help="Pfad zur Konfiguration")
    u = p.add_subparsers(dest="befehl", required=True)

    u.add_parser("einrichten", help="Absenderdaten und Budget anlegen").set_defaults(fn=cmd_einrichten)
    u.add_parser("branchen", help="Branchenkatalog anzeigen").set_defaults(fn=cmd_branchen)

    s = u.add_parser("suchen", help="Leads recherchieren (OpenStreetMap)")
    s.add_argument("--ort", required=True)
    s.add_argument("--branche", nargs="+", help="Branchenschlüssel, siehe 'branchen'")
    s.add_argument("--radius", type=float, default=12.0,
                   help="Suchradius in km um den Ort (Vorgabe: 12)")
    s.add_argument("--ausfuehrlich", action="store_true")
    s.set_defaults(fn=cmd_suchen)

    pr = u.add_parser("pruefen", help="Websites auditieren")
    pr.add_argument("--alle", action="store_true", help="alle ungeprüften Leads")
    pr.add_argument("--erneut", action="store_true", help="auch bereits geprüfte")
    pr.add_argument("--ort")
    pr.add_argument("--limit", type=int)
    pr.add_argument("--schnell", action="store_true", help="ohne HTTP-Umleitungsprüfung")
    pr.set_defaults(fn=cmd_pruefen)

    li = u.add_parser("liste", help="Leads nach Priorität")
    li.add_argument("--stufe", choices=db.STAGES)
    li.add_argument("--ort")
    li.add_argument("--limit", type=int, default=30)
    li.set_defaults(fn=cmd_liste)

    be = u.add_parser("bericht", help="Auditberichte als HTML erzeugen")
    be.add_argument("--lead", type=int, nargs="+")
    be.add_argument("--stufe", choices=db.STAGES)
    be.add_argument("--ort")
    be.add_argument("--limit", type=int, default=20)
    be.add_argument("--ordner")
    be.set_defaults(fn=cmd_bericht)

    an = u.add_parser("ansprache", help="Leitfaden, Brief und Nachfass-Mail erzeugen")
    an.add_argument("--art", choices=["telefon", "brief", "mail", "alle"], default="alle")
    an.add_argument("--lead", type=int, nargs="+")
    an.add_argument("--stufe", choices=db.STAGES)
    an.add_argument("--ort")
    an.add_argument("--limit", type=int, default=20)
    an.add_argument("--ordner")
    an.set_defaults(fn=cmd_ansprache)

    st = u.add_parser("stufe", help="Pipeline-Stufe eines Leads setzen")
    st.add_argument("lead", type=int)
    st.add_argument("stufe", choices=db.STAGES)
    st.add_argument("--notiz")
    st.add_argument("--umsatz", type=float)
    st.add_argument("--wert", type=float)
    st.add_argument("--faellig", help="Wiedervorlage JJJJ-MM-TT")
    st.add_argument("--naechster", help="nächster Schritt")
    st.add_argument("--minuten", type=int)
    st.set_defaults(fn=cmd_stufe)

    ze = u.add_parser("zeit", help="Arbeitszeit buchen")
    ze.add_argument("art", help="z. B. akquise, umsetzung, verwaltung")
    ze.add_argument("minuten", type=int)
    ze.add_argument("--lead", type=int)
    ze.add_argument("--notiz")
    ze.set_defaults(fn=cmd_zeit)

    au = u.add_parser("ausgabe", help="Ausgabe buchen")
    au.add_argument("posten")
    au.add_argument("betrag", type=float)
    au.add_argument("--kategorie")
    au.set_defaults(fn=cmd_ausgabe)

    u.add_parser("kennzahlen", help="Ist-Zahlen und Empfehlungen").set_defaults(fn=cmd_kennzahlen)

    pl = u.add_parser("plan", help="Budget-, Trichter- und Kapazitätsmodell")
    pl.add_argument("--kapital", type=float)
    pl.add_argument("--stunden", type=float)
    pl.set_defaults(fn=cmd_plan)

    tp = u.add_parser("tagesplan", help="Was heute zu tun ist")
    tp.add_argument("--anzahl", type=int, default=10)
    tp.set_defaults(fn=cmd_tagesplan)

    ex = u.add_parser("export", help="Leads als CSV exportieren")
    ex.add_argument("datei")
    ex.add_argument("--stufe", choices=db.STAGES)
    ex.add_argument("--ort")
    ex.set_defaults(fn=cmd_export)

    return p


def main(argv: list[str] | None = None) -> int:
    args = parser_bauen().parse_args(argv)
    try:
        return args.fn(args)
    except KeyboardInterrupt:
        print("\n  Abgebrochen.")
        return 130
    except KeyError as e:
        print(f"  ! {e}", file=sys.stderr)
        return 1
