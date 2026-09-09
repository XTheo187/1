"""Tests fuer Standortcheck. Ohne Netzzugriff - Seitenabruf wird ersetzt."""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from standortcheck import (angebote, audit, branchen, db, outreach, planner,
                           report, scoring)

GUTE_SEITE = """<!DOCTYPE html><html lang="de"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Dachdecker in Musterstadt - Bedachungen Mustermann GmbH</title>
<meta name="description" content="Bedachungen Mustermann in Musterstadt: Steildach, Flachdach, Dachfenster und Reparaturen. Seit 1978 im Familienbetrieb. Jetzt anrufen.">
<link rel="icon" href="/favicon.ico">
<script type="application/ld+json">{"@type":"LocalBusiness","name":"Mustermann"}</script>
</head><body>
<h1>Dachdeckermeister in Musterstadt</h1>
<a href="tel:+499411234567">0941 1234567</a>
<img src="d.jpg" alt="Dach"><img src="e.jpg" alt="Team">
<form><label for="n">Name</label><input id="n" type="text"></form>
<a href="/impressum">Impressum</a> <a href="/datenschutz">Datenschutz</a>
<p>&copy; 2026 Mustermann GmbH</p>
</body></html>"""

SCHLECHTE_SEITE = """<html><head><title>Startseite</title>
<script src="https://www.googletagmanager.com/gtag/js?id=G-1"></script>
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto">
</head><body><h2>Willkommen</h2>
<img src="a.jpg"><img src="b.jpg"><img src="c.jpg">
<p>&copy; 2017 Muster</p></body></html>"""


def _antwort(html: str, url: str = "https://beispiel.de/", **rest):
    grund = {
        "url": url, "erreichbar": True, "fehler": None, "status_code": 200,
        "endgueltige_url": url, "ladezeit_ms": 800, "seitengroesse": len(html),
        "html": html, "header": {"content-encoding": "gzip"}, "tls_fehler": None,
    }
    grund.update(rest)
    return grund


class TestAudit(unittest.TestCase):
    def _pruefen(self, html, lead=None, **rest):
        with mock.patch.object(audit, "seite_laden", return_value=_antwort(html, **rest)):
            return audit.pruefen("https://beispiel.de/", lead or {}, http_check=False)

    def test_gute_seite_hat_niedrigen_score(self):
        e = self._pruefen(GUTE_SEITE, {"ort": "Musterstadt"})
        self.assertLess(e["schmerz_score"], 15, [b["titel"] for b in e["befunde"]])

    def test_schlechte_seite_findet_kernprobleme(self):
        e = self._pruefen(SCHLECHTE_SEITE, {"ort": "Musterstadt"})
        codes = {b["code"] for b in e["befunde"]}
        for erwartet in (
            "kein_viewport", "kein_impressum", "keine_datenschutzerklaerung",
            "tracking_ohne_einwilligung", "schriften_extern", "titel_platzhalter",
            "keine_h1", "bilder_ohne_alt", "keine_sprache", "kein_favicon",
            "verwaist", "kein_markup", "ort_fehlt_im_titel",
        ):
            self.assertIn(erwartet, codes)

    def test_score_ist_gedeckelt(self):
        e = self._pruefen(SCHLECHTE_SEITE, {"ort": "Musterstadt"})
        self.assertLessEqual(e["schmerz_score"], 100)
        self.assertGreaterEqual(e["schmerz_score"], 0)

    def test_kein_https_wird_erkannt(self):
        e = self._pruefen(GUTE_SEITE, {}, url="http://beispiel.de/",
                          endgueltige_url="http://beispiel.de/")
        self.assertIn("kein_https", {b["code"] for b in e["befunde"]})

    def test_fehlende_website_ergibt_neubau_befund(self):
        e = audit.pruefen("", {})
        self.assertEqual(e["befunde"][0]["code"], "keine_website")
        self.assertFalse(e["erreichbar"])

    def test_nicht_erreichbar(self):
        tot = _antwort("", erreichbar=False, fehler="timed out", status_code=None)
        with mock.patch.object(audit, "seite_laden", return_value=tot):
            e = audit.pruefen("https://tot.example/", {}, http_check=False)
        self.assertIn("nicht_erreichbar", {b["code"] for b in e["befunde"]})

    def test_tls_fehler(self):
        kaputt = _antwort("", erreichbar=False, fehler="cert",
                          tls_fehler="certificate has expired")
        with mock.patch.object(audit, "seite_laden", return_value=kaputt):
            e = audit.pruefen("https://alt.example/", {}, http_check=False)
        self.assertIn("tls_kaputt", {b["code"] for b in e["befunde"]})

    def test_langsame_seite(self):
        e = self._pruefen(GUTE_SEITE, {}, ladezeit_ms=6200)
        self.assertIn("sehr_langsam", {b["code"] for b in e["befunde"]})

    def test_befunde_sind_nach_schwere_sortiert(self):
        e = self._pruefen(SCHLECHTE_SEITE, {"ort": "Musterstadt"})
        rang = {"kritisch": 0, "hoch": 1, "mittel": 2, "niedrig": 3}
        werte = [rang[b["schwere"]] for b in e["befunde"]]
        self.assertEqual(werte, sorted(werte))

    def test_jeder_befund_ist_vollstaendig(self):
        e = self._pruefen(SCHLECHTE_SEITE, {"ort": "Musterstadt"})
        for b in e["befunde"]:
            for feld in ("code", "titel", "kategorie", "schwere", "befund",
                         "wirkung", "massnahme", "aufwand_h"):
                self.assertTrue(b.get(feld) not in (None, ""), f"{b['code']}.{feld}")

    def test_url_normalisierung(self):
        self.assertEqual(audit.url_normalisieren("beispiel.de"), "https://beispiel.de")
        self.assertEqual(audit.url_normalisieren("http://x.de"), "http://x.de")
        self.assertEqual(audit.url_normalisieren("  "), "")

    def test_kaputtes_html_stuerzt_nicht_ab(self):
        e = self._pruefen("<html><head><title>Test<body><p>offen<div>")
        self.assertIsInstance(e["schmerz_score"], int)


class TestPraxisfaelle(unittest.TestCase):
    """Fälle, die beim Lauf gegen echte Websites aufgefallen sind."""

    def test_meta_weiterleitung_wird_verfolgt(self):
        """Eine Weiterleitungsseite darf nicht statt des Ziels bewertet werden."""
        stub = ('<html><head><title>Firma</title>'
                '<meta http-equiv="refresh" content="0;url=https://ziel.example/home">'
                '</head><body></body></html>')
        antworten = [_antwort(stub, url="https://alt.example/"),
                     _antwort(GUTE_SEITE, url="https://ziel.example/home",
                              endgueltige_url="https://ziel.example/home")]
        with mock.patch.object(audit, "seite_laden", side_effect=antworten):
            e = audit.pruefen("https://alt.example/", {"ort": "Musterstadt"},
                              http_check=False)
        codes = {b["code"] for b in e["befunde"]}
        self.assertEqual(e["endgueltige_url"], "https://ziel.example/home")
        self.assertIn("meta_weiterleitung", codes)
        # Die Zielseite ist gut - die Mängel der leeren Hülle dürfen nicht zählen
        self.assertNotIn("kein_impressum", codes)
        self.assertNotIn("keine_h1", codes)

    def test_weiterleitungsschleife_endet(self):
        stub = ('<html><head><meta http-equiv="refresh" content="0;url=https://b.example/">'
                '</head><body></body></html>')
        with mock.patch.object(audit, "seite_laden",
                               return_value=_antwort(stub, url="https://a.example/")):
            e = audit.pruefen("https://a.example/", {}, http_check=False)
        self.assertIsInstance(e["schmerz_score"], int)

    def test_gekaperte_domain_meldet_nur_das_wesentliche(self):
        spam = ("<html><head><title>MONET11 Link Stabil Bonus Harian</title></head>"
                "<body>situs gacor slot online bonus harian maxwin togel judi "
                "cuan rtp live</body></html>")
        with mock.patch.object(audit, "seite_laden", return_value=_antwort(spam)):
            e = audit.pruefen("https://gekapert.example/",
                              {"name": "Elektro Sturm GmbH"}, http_check=False)
        codes = [b["code"] for b in e["befunde"]]
        self.assertEqual(codes, ["fremdinhalte"])  # kein Rauschen daneben
        self.assertGreater(e["schmerz_score"], 50)

    def test_geparkte_domain(self):
        park = "<html><body>This domain is for sale. sedoparking.com</body></html>"
        with mock.patch.object(audit, "seite_laden", return_value=_antwort(park)):
            e = audit.pruefen("https://geparkt.example/", {"name": "X"}, http_check=False)
        self.assertEqual([b["code"] for b in e["befunde"]], ["domain_geparkt"])

    def test_normale_seite_gilt_nicht_als_gekapert(self):
        with mock.patch.object(audit, "seite_laden", return_value=_antwort(GUTE_SEITE)):
            e = audit.pruefen("https://ok.example/", {"name": "Mustermann"},
                              http_check=False)
        codes = {b["code"] for b in e["befunde"]}
        self.assertNotIn("fremdinhalte", codes)
        self.assertNotIn("domain_geparkt", codes)

    def test_kein_nutzbarer_auftritt_ergibt_neuaufbaupreis(self):
        for code in ("fremdinhalte", "domain_geparkt", "nicht_erreichbar"):
            a = {"schmerz_score": 55, "aufwand_h": 16.0,
                 "befunde": [{"code": code, "aufwand_h": 16.0}]}
            ang = scoring.angebot({"branche": "Elektrobetrieb",
                                   "website": "https://x.de"}, a)
            self.assertTrue(ang["neuaufbau"], code)
            self.assertGreaterEqual(
                ang["paket"], branchen.KATALOG["elektriker"].projektpreis_eur, code)


class TestDatenbank(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.pfad = Path(self.tmp.name) / "t.db"

    def tearDown(self):
        self.tmp.cleanup()

    def test_lead_wird_nicht_doppelt_angelegt(self):
        daten = {"name": "Muster", "ort": "Stadt", "quelle": "osm", "quelle_id": "node/1"}
        with db.session(self.pfad) as con:
            a, neu_a = db.lead_speichern(con, daten)
            b, neu_b = db.lead_speichern(con, daten)
        self.assertEqual(a, b)
        self.assertTrue(neu_a)
        self.assertFalse(neu_b)

    def test_leere_felder_werden_ergaenzt_gefuellte_nicht(self):
        with db.session(self.pfad) as con:
            lid, _ = db.lead_speichern(con, {
                "name": "Muster", "ort": "Stadt", "telefon": "0111",
                "quelle": "osm", "quelle_id": "node/1"})
            db.lead_speichern(con, {
                "name": "Muster", "ort": "Stadt", "telefon": "0999",
                "website": "https://neu.de", "quelle": "osm", "quelle_id": "node/1"})
            lead = dict(db.lead_holen(con, lid))
        self.assertEqual(lead["telefon"], "0111")       # bestehend bleibt
        self.assertEqual(lead["website"], "https://neu.de")  # leeres wird ergaenzt

    def test_audit_rundlauf_erhaelt_aufwand(self):
        ergebnis = {
            "erreichbar": True, "schmerz_score": 42, "aufwand_h": 9.5,
            "befunde": [{"code": "x", "titel": "T", "kategorie": "Technik",
                         "schwere": "hoch", "punkte": 10, "befund": "b",
                         "wirkung": "w", "massnahme": "m", "aufwand_h": 9.5}],
            "rohdaten": {"titel": "T"},
        }
        with db.session(self.pfad) as con:
            lid, _ = db.lead_speichern(con, {"name": "M", "ort": "S"})
            db.audit_speichern(con, lid, ergebnis)
            geladen = db.letztes_audit(con, lid)
        self.assertEqual(geladen["schmerz_score"], 42)
        self.assertEqual(geladen["aufwand_h"], 9.5)
        self.assertEqual(len(geladen["befunde"]), 1)

    def test_kennzahlen_bei_leerer_datenbank(self):
        with db.session(self.pfad) as con:
            k = planner.kennzahlen(con)
        self.assertEqual(k["leads_gesamt"], 0)
        self.assertEqual(k["stundenlohn"], 0)
        self.assertEqual(k["abschlussquote"], 0.0)

    def test_kennzahlen_rechnen_korrekt(self):
        with db.session(self.pfad) as con:
            a, _ = db.lead_speichern(con, {"name": "A", "ort": "S"})
            b, _ = db.lead_speichern(con, {"name": "B", "ort": "S"})
            db.lead_aktualisieren(con, a, stage="gewonnen", umsatz=2000.0)
            db.lead_aktualisieren(con, b, stage="verloren")
            db.ausgabe_buchen(con, "Porto", 200.0, "Akquise")
            db.aktivitaet_buchen(con, "akquise", 600)  # 10 Stunden
            k = planner.kennzahlen(con)
        self.assertEqual(k["umsatz"], 2000.0)
        self.assertEqual(k["gewinn"], 1800.0)
        self.assertEqual(k["stunden"], 10.0)
        self.assertEqual(k["stundenlohn"], 180.0)
        self.assertEqual(k["abschlussquote"], 50.0)


class TestBewertung(unittest.TestCase):
    def test_rufnummer_hebt_prioritaet(self):
        a = {"schmerz_score": 50, "befunde": [], "aufwand_h": 10}
        mit = scoring.prioritaet({"telefon": "0941", "branche": "Dachdecker"}, a)
        ohne = scoring.prioritaet({"branche": "Dachdecker"}, a)
        self.assertGreater(mit["prioritaet"], ohne["prioritaet"])

    def test_prioritaet_bleibt_im_bereich(self):
        extrem = {
            "schmerz_score": 100, "aufwand_h": 60,
            "befunde": [{"code": c} for c in scoring.ZUGKRAFT],
        }
        p = scoring.prioritaet(
            {"telefon": "1", "branche": "Bauunternehmen", "strasse": "A", "plz": "1"}, extrem)
        self.assertLessEqual(p["prioritaet"], 100)
        self.assertGreaterEqual(scoring.prioritaet({}, None)["prioritaet"], 0)

    def test_paketpreis_unterbietet_die_einzelsumme(self):
        """Der Bericht behauptet eine Ersparnis - sie muss auch stimmen."""
        for aufwand in (8.0, 15.0, 33.1, 60.0):
            a = {"schmerz_score": 50, "befunde": [], "aufwand_h": aufwand,
                 "erreichbar": True}
            ang = scoring.angebot({"branche": "Dachdecker", "website": "https://x.de"}, a)
            if ang["paket"] > scoring.MINDESTPREIS:
                self.assertLess(ang["paket"], ang["listenpreis"], f"{aufwand} h")

    def test_mindestpreis_greift_bei_kleinem_aufwand(self):
        a = {"schmerz_score": 5, "befunde": [], "aufwand_h": 1.0, "erreichbar": True}
        ang = scoring.angebot({"branche": "Gastronomie", "website": "https://x.de"}, a)
        self.assertGreaterEqual(ang["paket"], scoring.MINDESTPREIS)

    def test_ohne_website_gilt_der_projektpreis(self):
        a = {"schmerz_score": 40, "befunde": [], "aufwand_h": 14.0, "erreichbar": False}
        ang = scoring.angebot({"branche": "Rechtsanwaltskanzlei"}, a)
        self.assertGreaterEqual(ang["paket"], branchen.KATALOG["anwalt"].projektpreis_eur)

    def test_jahr_eins_ist_paket_plus_zwoelf_monate(self):
        a = {"schmerz_score": 50, "befunde": [], "aufwand_h": 20.0, "erreichbar": True}
        lead = {"branche": "Dachdecker", "website": "https://x.de"}
        ang = scoring.angebot(lead, a)
        self.assertEqual(ang["jahr_eins"], ang["paket"] + 12 * ang["betreuung"])
        self.assertEqual(scoring.deal_wert(lead, a), ang["jahr_eins"])

    def test_deal_wert_folgt_branche(self):
        a = {"schmerz_score": 40, "befunde": [], "aufwand_h": 12}
        teuer = scoring.deal_wert({"branche": "Immobilienmakler"}, a)
        guenstig = scoring.deal_wert({"branche": "Gastronomie"}, a)
        self.assertGreater(teuer, guenstig)

    def test_unbekannte_branche_faellt_zurueck(self):
        self.assertGreater(scoring.deal_wert({"branche": "Zirkus"}, None), 0)
        self.assertIsNone(scoring.branche_zu_schluessel(None))

    def test_rangliste_sortiert_absteigend(self):
        werte = scoring.rangliste([{"prioritaet": 5}, {"prioritaet": 90}, {"prioritaet": 40}])
        self.assertEqual([e["prioritaet"] for e in werte], [90, 40, 5])


class TestPlanung(unittest.TestCase):
    def test_optimum_haelt_die_zeitgrenze_ein(self):
        for stunden in (5, 10, 20, 40):
            a = planner.Annahmen(stunden_pro_woche=stunden)
            e = planner.briefe_optimieren(a)
            self.assertLessEqual(e["zeit_gesamt"], stunden, f"{stunden} h")
            self.assertGreater(e["briefe"], 0)

    def test_mehr_briefe_erzeugen_mehr_abschluesse(self):
        klein = planner.trichter(planner.Annahmen(briefe_pro_woche=10))
        gross = planner.trichter(planner.Annahmen(briefe_pro_woche=50))
        self.assertGreater(gross["abschluesse"], klein["abschluesse"])

    def test_szenarien_sind_geordnet(self):
        s = planner.szenarien(planner.Annahmen())
        self.assertLess(s["vorsichtig"]["umsatz_monat"], s["erwartet"]["umsatz_monat"])
        self.assertLess(s["erwartet"]["umsatz_monat"], s["gut"]["umsatz_monat"])

    def test_budget_summiert_auf_startkapital(self):
        self.assertEqual(sum(b for _, b, _, _ in planner.BUDGET_500), 500.0)

    def test_empfehlung_liefert_immer_etwas(self):
        a = planner.Annahmen()
        leer = {"leads_gesamt": 0, "verteilung": {s: 0 for s in db.STAGES},
                "kontaktquote": 0, "abschlussquote": 0, "stunden": 0,
                "stundenlohn": 0, "ausgaben": 0, "umsatz": 0}
        self.assertTrue(planner.empfehlung(leer, a))
        voll = {**leer, "leads_gesamt": 100,
                "verteilung": {**leer["verteilung"], "geprueft": 40, "angebot": 5}}
        self.assertTrue(planner.empfehlung(voll, a))


class TestAusgabe(unittest.TestCase):
    def setUp(self):
        self.absender = {"name": "T. Muster", "strasse": "Weg 1", "ort": "93047 Regensburg",
                         "telefon": "0941 1", "email": "a@b.de"}
        with mock.patch.object(audit, "seite_laden",
                               return_value=_antwort(SCHLECHTE_SEITE)):
            self.audit = audit.pruefen("https://x.de/", {"ort": "Musterstadt"}, http_check=False)
        self.lead = {"id": 1, "name": "Muster GmbH", "ort": "Musterstadt", "plz": "93047",
                     "strasse": "Weg 3", "telefon": "0941 9", "branche": "Dachdecker",
                     "website": "https://x.de/"}

    def test_bericht_ist_vollstaendiges_html(self):
        h = report.bericht_erzeugen(self.lead, self.audit, self.absender)
        self.assertTrue(h.startswith("<!DOCTYPE html>"))
        self.assertIn("</html>", h)
        self.assertIn("Muster GmbH", h)
        self.assertIn('lang="de"', h)
        # keine externen Ressourcen: der Bericht muss offline funktionieren
        self.assertNotIn("http://", h.replace("http://www.w3.org", ""))
        self.assertNotIn("<script", h)

    def test_bericht_enthaelt_jeden_befund(self):
        h = report.bericht_erzeugen(self.lead, self.audit, self.absender)
        for b in self.audit["befunde"]:
            self.assertIn(b["titel"], h)

    def test_bericht_nennt_keine_erfundene_ersparnis(self):
        """Wenn das Paket nicht guenstiger ist, darf der Bericht das nicht behaupten."""
        ang = scoring.angebot(self.lead, self.audit)
        h = report.bericht_erzeugen(self.lead, self.audit, self.absender, angebot=ang)
        if ang["paket"] >= ang["listenpreis"]:
            self.assertNotIn("weniger", h)
        else:
            self.assertIn("weniger", h)

    def test_bericht_zeigt_betreuung_getrennt(self):
        ang = scoring.angebot(self.lead, self.audit)
        h = report.bericht_erzeugen(self.lead, self.audit, self.absender, angebot=ang)
        self.assertIn("im Monat", h)
        self.assertIn("ndbar", h)  # "kündbar", im HTML als Entity geschrieben
        self.assertIn(report._euro(ang["paket"]), h)

    def test_bericht_ohne_befunde(self):
        h = report.bericht_erzeugen(
            self.lead, {"schmerz_score": 0, "befunde": [], "aufwand_h": 0}, self.absender)
        self.assertIn("Keine wesentlichen Mängel", h)

    def test_bericht_maskiert_html_in_daten(self):
        boese = {**self.lead, "name": "<script>alert(1)</script>"}
        h = report.bericht_erzeugen(boese, self.audit, self.absender)
        self.assertNotIn("<script>alert", h)
        self.assertIn("&lt;script&gt;", h)

    def test_dateiname_ist_sicher(self):
        n = report.dateiname({"id": 7, "name": "Müller & Söhne GmbH / Nord"})
        self.assertTrue(n.endswith(".html"))
        for zeichen in "/\\ &äöüß":
            self.assertNotIn(zeichen, n)

    def test_texte_ohne_html_entities(self):
        for erzeuger in (outreach.telefonleitfaden, outreach.brief, outreach.nachfass_mail):
            t = erzeuger(self.lead, self.audit, self.absender)
            self.assertNotIn("&auml;", t)
            self.assertNotIn("&szlig;", t)
            self.assertNotIn("{", t.replace("{}", ""))  # keine offenen Platzhalter

    def test_brief_enthaelt_dsgvo_hinweis(self):
        t = outreach.brief(self.lead, self.audit, self.absender)
        self.assertIn("Art. 14 DSGVO", t)
        self.assertIn("Art. 21 DSGVO", t)
        self.assertIn("a@b.de", t)

    def test_mail_warnt_vor_kaltversand(self):
        t = outreach.nachfass_mail(self.lead, self.audit, self.absender)
        self.assertIn("§ 7", t)
        self.assertIn("NUR NACH GEFÜHRTEM GESPRÄCH", t)

    def test_leitfaden_nennt_ort_ohne_plz(self):
        t = outreach.telefonleitfaden(self.lead, self.audit, self.absender)
        self.assertIn("ich bin aus Regensburg", t)
        self.assertNotIn("aus 93047", t)

    def test_ansprache_ohne_befunde_bricht_nicht(self):
        leer = {"schmerz_score": 0, "befunde": [], "aufwand_h": 0}
        for erzeuger in (outreach.telefonleitfaden, outreach.brief, outreach.nachfass_mail):
            self.assertTrue(erzeuger(self.lead, leer, self.absender))


class TestEinstiegsangebote(unittest.TestCase):
    def _audit_mit(self, *codes):
        return {"schmerz_score": 50, "aufwand_h": 10.0,
                "befunde": [{"code": c, "aufwand_h": 1.0} for c in codes]}

    def test_katalog_ist_konsistent(self):
        for b in angebote.KATALOG:
            self.assertGreater(b.preis, 0)
            self.assertGreater(b.stunden, 0)
            self.assertTrue(0 <= b.zugkraft <= 100)
            self.assertTrue(b.haken and b.ergebnis)
            # Ein Baustein, der unter 60 EUR/h einbringt, lohnt die Fahrt nicht
            self.assertGreaterEqual(b.stundensatz, 60, b.code)

    def test_jeder_baustein_hat_einen_echten_befund(self):
        """Ein Baustein ohne passenden Audit-Befund wird nie angeboten."""
        with mock.patch.object(audit, "seite_laden",
                               return_value=_antwort(SCHLECHTE_SEITE)):
            bekannt = {b["code"] for b in
                       audit.pruefen("https://x.de/", {"ort": "M"},
                                     http_check=False)["befunde"]}
        # Codes, die das Audit grundsätzlich erzeugen kann
        alle_codes = bekannt | {
            "kein_https", "keine_https_umleitung", "tracking_ohne_einwilligung",
            "karte_ohne_einwilligung", "telefon_nicht_klickbar",
            "keine_telefonnummer", "mixed_content", "zoom_gesperrt",
            "keine_komprimierung", "formular_ohne_label", "kein_impressum",
            "keine_datenschutzerklaerung",
        }
        for b in angebote.KATALOG:
            self.assertIn(b.code, alle_codes, f"Baustein '{b.code}' ohne Befund")

    def test_waehlt_den_zugkraeftigsten(self):
        e = angebote.einstieg_waehlen(
            self._audit_mit("kein_favicon", "kein_impressum", "keine_komprimierung"))
        self.assertEqual(e["bausteine"][0]["code"], "kein_impressum")

    def test_angebot_haelt_die_preisgrenze_ein(self):
        codes = ("schriften_extern", "kein_impressum",
                 "keine_datenschutzerklaerung", "kein_markup")
        for grenze in (150, 200, 350, 500):
            e = angebote.einstieg_waehlen(self._audit_mit(*codes), grenze=grenze)
            self.assertLessEqual(e["preis"], grenze, f"Grenze {grenze}")
            self.assertFalse(e["ueber_grenze"], f"Grenze {grenze}")

    def test_zu_enge_grenze_wird_gemeldet_statt_verschwiegen(self):
        e = angebote.einstieg_waehlen(
            self._audit_mit("keine_datenschutzerklaerung"), grenze=50)
        self.assertTrue(e["ueber_grenze"])
        self.assertEqual(len(e["bausteine"]), 1)  # kein Buendel obendrauf

    def test_bei_enger_grenze_gewinnt_der_guenstigste(self):
        e = angebote.einstieg_waehlen(
            self._audit_mit("keine_datenschutzerklaerung", "kein_favicon"),
            grenze=100)
        self.assertEqual(e["bausteine"][0]["code"], "kein_favicon")

    def test_buendel_ist_guenstiger_als_einzeln(self):
        e = angebote.einstieg_waehlen(
            self._audit_mit("telefon_nicht_klickbar", "kein_favicon"))
        if len(e["bausteine"]) > 1:
            self.assertLess(e["preis"], e["einzelpreise"])

    def test_ohne_passenden_befund_kein_angebot(self):
        self.assertIsNone(angebote.einstieg_waehlen(self._audit_mit("frames")))
        self.assertIsNone(angebote.einstieg_waehlen(None))

    def test_gekaperte_domain_bekommt_kein_kleinticket(self):
        """Eine gekaperte Domain repariert man nicht für 149 EUR."""
        spam = ("<html><head><title>MONET11</title></head><body>situs gacor "
                "slot online bonus harian maxwin togel judi cuan</body></html>")
        with mock.patch.object(audit, "seite_laden", return_value=_antwort(spam)):
            a = audit.pruefen("https://x.example/", {"name": "Y"}, http_check=False)
        self.assertIsNone(angebote.einstieg_waehlen(a))

    def test_offene_befunde_werden_gezaehlt(self):
        a = self._audit_mit("kein_impressum", "kein_favicon", "kein_markup",
                            "keine_beschreibung")
        e = angebote.einstieg_waehlen(a)
        self.assertEqual(e["weitere_offen"], 4 - len(e["bausteine"]))

    def test_leitfaden_nennt_preis_und_naechsten_schritt(self):
        a = self._audit_mit("kein_impressum", "kein_markup")
        lead = {"id": 3, "name": "Muster", "ort": "Stadt", "plz": "1", "strasse": "W 1"}
        absender = {"name": "T", "ort": "93047 Regensburg", "telefon": "1", "email": "a@b.de"}
        text = outreach.einstiegsgespraech(lead, a, absender)
        e = angebote.einstieg_waehlen(a)
        self.assertIn(f"{e['preis']:.0f} EUR", text)
        self.assertIn("stufe 3 gewonnen", text)
        self.assertIn("Gesamtpaket", text)  # der Anschluss ans grosse Ticket
        self.assertNotIn("{", text.replace("{}", ""))

    def test_leitfaden_ohne_angebot_sagt_es_deutlich(self):
        text = outreach.einstiegsgespraech(
            {"name": "X"}, self._audit_mit("frames"),
            {"name": "T", "ort": "R", "telefon": "1", "email": "a@b.de"})
        self.assertIn("überspringen", text)


class TestKanalvergleich(unittest.TestCase):
    def test_kleines_ticket_schliesst_besser(self):
        nach_name = {k.name: k for k in planner.KANAELE}
        self.assertGreater(nach_name["Vor Ort, Einstieg"].quote,
                           nach_name["Vor Ort, Projekt"].quote)

    def test_vergleich_ist_nach_aufwand_geordnet(self):
        v = planner.kanalvergleich()
        kontakte = [e["kontakte_bis_erster"] for e in v]
        self.assertEqual(kontakte, sorted(kontakte))

    def test_briefkanal_ist_der_teuerste_einstieg(self):
        v = planner.kanalvergleich()
        teuerster = max(v, key=lambda e: e["kosten_bis_erster"])
        self.assertTrue(teuerster["name"].startswith("Brief"))

    def test_risiko_stimmt_mit_dem_szenariomodell_ueberein(self):
        """Kanal- und Szenariomodell müssen dieselbe Briefquote ergeben."""
        brief = next(k for k in planner.KANAELE if k.name.startswith("Brief"))
        a = planner.Annahmen(**{**planner.Annahmen().__dict__,
                                **planner.SZENARIEN["vorsichtig"]})
        szenario_quote = (a.quote_erreicht * a.quote_gespraech
                          * a.quote_angebot * a.quote_abschluss)
        self.assertAlmostEqual(brief.quote, szenario_quote, places=3)

    def test_risiko_faellt_mit_mehr_kontakten(self):
        k = planner.KANAELE[0]
        self.assertGreater(planner.risiko_ohne_abschluss(k, 5),
                           planner.risiko_ohne_abschluss(k, 50))
        self.assertLessEqual(planner.risiko_ohne_abschluss(k, 0), 100.0)


class TestBranchen(unittest.TestCase):
    def test_katalog_ist_konsistent(self):
        for b in branchen.liste():
            self.assertGreater(b.projektpreis_eur, 0)
            self.assertGreater(b.kundenwert_eur, 0)
            self.assertTrue(b.osm_filter)
            self.assertTrue(b.aufhaenger.endswith("."))

    def test_unbekannte_branche_meldet_alternativen(self):
        with self.assertRaises(KeyError) as ctx:
            branchen.aufloesen("raumschiffbau")
        self.assertIn("dachdecker", str(ctx.exception))


if __name__ == "__main__":
    unittest.main(verbosity=2)
