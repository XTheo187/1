"""Erzeugt Gesprächsleitfaden, Brief und Nachfass-E-Mail zu einem Lead.

Rechtlicher Rahmen der Erstansprache in Deutschland - bewusst konservativ:

* Brief  : Postalische Werbung an Gewerbetreibende ist zulässig. Die Daten
           stammen aus einer öffentlichen Quelle; die Verarbeitung stützt
           sich auf das berechtigte Interesse (Art. 6 Abs. 1 lit. f DSGVO).
           Der Empfänger wird nach Art. 14 DSGVO über Herkunft und
           Widerspruchsrecht informiert - der Baustein steht im Brief.
* Anruf  : Bei Gewerbetreibenden erlaubt § 7 Abs. 2 Nr. 1 UWG den Anruf bei
           mutmaßlicher Einwilligung. Die trägt nur, wenn das Angebot
           sachlich zum Geschäft des Angerufenen passt. Der Leitfaden stellt
           den Bezug deshalb im ersten Satz her.
* E-Mail : Werbe-E-Mails ohne vorherige ausdrückliche Einwilligung sind auch
           gegenüber Unternehmen nach § 7 Abs. 2 Nr. 2 UWG unzulässig und
           regelmäßig abmahnfähig. Die hier erzeugten E-Mails sind
           ausschließlich Nachfass-Texte nach einem geführten Gespräch.

Das ist keine Rechtsberatung. Bei Unsicherheit vor der ersten Kampagne
einmal anwaltlich prüfen lassen - einmalige Kosten, dauerhafte Sicherheit.
"""

from __future__ import annotations

from datetime import date, timedelta
from typing import Any

from . import angebote, branchen, scoring

# Aufhänger je Befund: ein Satz, der am Telefon in drei Sekunden sitzt.
AUFHAENGER = {
    "kein_impressum": "auf Ihrer Startseite habe ich keinen Impressumshinweis gefunden",
    "keine_datenschutzerklaerung": "auf Ihrer Seite ist keine Datenschutzerklärung verlinkt",
    "tracking_ohne_einwilligung": "Ihre Seite lädt Analysedienste, bevor der Besucher zustimmen kann",
    "schriften_extern": "Ihre Seite lädt Schriften direkt von einem Google-Server",
    "kein_viewport": "Ihre Seite ist auf dem Handy nicht richtig lesbar",
    "viewport_fest": "Ihre Seite passt sich der Handy-Breite nicht an",
    "kein_https": "Ihre Seite wird im Browser als „Nicht sicher“ angezeigt",
    "tls_kaputt": "Browser zeigen bei Ihrer Seite gerade eine Sicherheitswarnung",
    "nicht_erreichbar": "Ihre Website war bei meinen Aufrufen nicht erreichbar",
    "keine_website": "ich habe zu Ihrem Betrieb keine eigene Website gefunden",
    "sehr_langsam": "Ihre Startseite braucht spürbar lange zum Laden",
    "verwaist": "in Ihrer Fußzeile steht noch eine alte Jahreszahl",
    "keine_telefonnummer": "auf Ihrer Startseite steht Ihre Rufnummer nicht direkt sichtbar",
    "telefon_nicht_klickbar": "Ihre Rufnummer lässt sich auf dem Handy nicht antippen",
    "kein_markup": "Ihr Eintrag bei Google zeigt keine Öffnungszeiten an",
    "titel_platzhalter": "bei Google steht über Ihrem Eintrag nur ein Platzhaltertext",
    "ort_fehlt_im_titel": "Ihr Ort taucht in Ihrem Google-Eintrag gar nicht auf",
    "frames": "Ihre Seite läuft noch auf einer sehr alten Technik",
}

EINWAENDE = [
    (
        "„Wir haben schon jemanden dafür.“",
        "Gut, dann ist die Betreuung geklärt. Der Punkt, den ich gefunden habe, "
        "ist dem offenbar durchgerutscht - schicken Sie ihm die Analyse einfach "
        "weiter. Wenn er es macht: perfekt. Wenn nicht, melden Sie sich.",
    ),
    (
        "„Dafür haben wir kein Budget.“",
        "Verstehe. Deshalb frage ich anders: Was ist bei Ihnen ein neuer Kunde "
        "im Schnitt wert? … Bei dem Betrag rechnet sich die Sache ab dem "
        "{amortisation}. Auftrag. Wollen wir nur den kritischsten Punkt zuerst machen?",
    ),
    (
        "„Schicken Sie mir was per Mail.“",
        "Mache ich - dann darf ich Ihnen an {email_platzhalter} schreiben? "
        "Ich rufe Donnerstag kurz an, ob es angekommen ist. Zwei Minuten, nicht mehr.",
    ),
    (
        "„Wir kriegen unsere Aufträge über Empfehlung.“",
        "Das glaube ich sofort - und genau deshalb schauen die Empfohlenen "
        "vorher auf Ihre Seite. Der erste Eindruck entscheidet dann, ob sie anrufen.",
    ),
    (
        "„Keine Zeit.“",
        "Verstehe, ich halte mich kurz: Ich habe Ihnen die Analyse schon "
        "fertig gemacht, das kostet Sie nichts. Wann passt es Ihnen besser - "
        "morgen früh oder eher gegen Feierabend?",
    ),
]


def _top_befunde(audit: dict[str, Any], anzahl: int = 3) -> list[dict[str, Any]]:
    return (audit or {}).get("befunde", [])[:anzahl]


def _aufhaenger_satz(audit: dict[str, Any], als_satz: bool = False) -> str:
    satz = ""
    for b in _top_befunde(audit, 6):
        if b["code"] in AUFHAENGER:
            satz = AUFHAENGER[b["code"]]
            break
    if not satz:
        top = _top_befunde(audit, 1)
        satz = top[0]["befund"] if top else "mir sind ein paar Punkte aufgefallen"
    if als_satz:
        satz = satz[:1].upper() + satz[1:]
        if not satz.endswith("."):
            satz += "."
    return satz


def _entkodieren(t: str) -> str:
    """HTML-Entities zu Klartext - Leitfaden und Brief sind reiner Text."""
    ersetzungen = {
        "ä": "ä", "ö": "ö", "ü": "ü", "Ä": "Ä",
        "Ö": "Ö", "Ü": "Ü", "ß": "ß", "&": "&",
    }
    for a, b in ersetzungen.items():
        t = t.replace(a, b)
    return t


def _ortsname(ort: str) -> str:
    """„93047 Regensburg“ -> „Regensburg“."""
    teile = [t for t in (ort or "").split() if not t.isdigit()]
    return " ".join(teile) or ort


def telefonleitfaden(lead: dict[str, Any], audit: dict[str, Any], absender: dict[str, str]) -> str:
    schluessel = scoring.branche_zu_schluessel(lead.get("branche"))
    branche = branchen.KATALOG.get(schluessel) if schluessel else None
    kundenwert = branche.kundenwert_eur if branche else 1500
    ang = scoring.angebot(lead, audit)
    amortisation = max(1, round(ang["paket"] / max(kundenwert, 1)))

    aufhaenger = _entkodieren(_aufhaenger_satz(audit, als_satz=True))
    befunde = _top_befunde(audit, 3)
    punkte = "\n".join(
        f"   {i}. {_entkodieren(b['titel'])} - {_entkodieren(b['wirkung'].split('.')[0])}."
        for i, b in enumerate(befunde, 1)
    ) or "   (keine wesentlichen Befunde - dieser Lead lohnt den Anruf nicht)"

    einwaende = "\n\n".join(
        f"  {frage}\n  -> " + antwort.format(
            amortisation=amortisation,
            email_platzhalter=lead.get("email") or "Ihre Adresse",
        ).replace("\n", "\n     ")
        for frage, antwort in EINWAENDE
    )

    return f"""GESPRÄCHSLEITFADEN
{'=' * 68}
Betrieb   : {lead.get('name', '')}
Branche   : {lead.get('branche', '')}
Ort       : {lead.get('plz', '')} {lead.get('ort', '')}
Telefon   : {lead.get('telefon') or 'NICHT BEKANNT - vorher recherchieren'}
Website   : {lead.get('website') or 'keine gefunden'}
Score     : {audit.get('schmerz_score', 0)}/100
Angebot   : {ang['paket']:.0f} EUR Festpreis + {ang['betreuung']:.0f} EUR/Monat Betreuung
            = {ang['jahr_eins']:.0f} EUR im ersten Jahr

RECHTLICHER RAHMEN
  Anruf bei Gewerbetreibenden: § 7 Abs. 2 Nr. 1 UWG erlaubt ihn bei
  mutmaßlicher Einwilligung. Die trägt nur, wenn der sachliche Bezug zum
  Geschäft des Angerufenen im ersten Satz klar wird. Genau dafür ist der
  Einstieg unten gebaut. Auf Widerspruch: sofort beenden, Lead auf
  "verloren" setzen, Notiz "Kontaktaufnahme unerwünscht" - und nie wieder
  anrufen.

1) EINSTIEG (max. 15 Sekunden, Bezug sofort herstellen)
   "Guten Tag, {absender.get('name', '')} hier, ich bin aus {_ortsname(absender.get('ort', '')) or 'der Region'}.
    Ich rufe an, weil ich mir die Websites der {lead.get('branche', 'Betriebe')} hier
    in {lead.get('ort', 'der Umgebung')} angesehen habe. Bei Ihnen ist mir eine
    Sache aufgefallen: {aufhaenger}
    Haben Sie zwei Minuten, oder rufe ich besser später an?"

   -> Warten. Nicht weiterreden. Die Pause macht die Arbeit.

2) BEFUND KONKRET MACHEN (was ich gefunden habe)
{punkte}

3) FRAGEN (der Betrieb soll den Schmerz selbst aussprechen)
   - "Wie viele Anfragen kommen bei Ihnen im Monat über die Website?"
   - "Wissen Sie, ob die Leute Sie eher übers Handy oder am Rechner finden?"
   - "Wer betreut die Seite bei Ihnen aktuell?"
   - "Was wäre Ihnen ein zusätzlicher Auftrag im Monat wert?"

4) ABSCHLUSS (Ziel ist NICHT der Verkauf, sondern der Termin)
   "Ich habe Ihnen die vollständige Analyse schon als PDF fertig gemacht -
    sechs Seiten, kostet Sie nichts. Ich komme Dienstag ohnehin nach
    {lead.get('ort', 'Ihnen')}. Passt es Ihnen um 10 Uhr oder eher um 14 Uhr?"

   -> Alternativfrage. Nie "Hätten Sie Interesse?" fragen.

5) EINWÄNDE

{einwaende}

6) NACH DEM GESPRÄCH (sofort, nicht später)
   [ ] Ergebnis eintragen:  standortcheck stufe {lead.get('id', '?')} <stufe> --notiz "..."
   [ ] Zeit buchen:         standortcheck zeit akquise <minuten> --lead {lead.get('id', '?')}
   [ ] Bericht senden, falls zugesagt (dann ist die E-Mail erlaubt)
   [ ] Wiedervorlage setzen: --faellig {(date.today() + timedelta(days=3)).isoformat()}
"""


def brief(lead: dict[str, Any], audit: dict[str, Any], absender: dict[str, str]) -> str:
    aufhaenger = _entkodieren(_aufhaenger_satz(audit, als_satz=True))
    befunde = _top_befunde(audit, 3)
    aufzaehlung = "\n".join(
        f"  - {_entkodieren(b['titel'])}: {_entkodieren(b['befund'])}" for b in befunde
    )
    anrede = "Sehr geehrte Damen und Herren,"
    heute = date.today().strftime("%d.%m.%Y")
    rueckruf = (date.today() + timedelta(days=7)).strftime("%d.%m.%Y")

    return f"""{absender.get('name', '')}
{absender.get('strasse', '')}
{absender.get('ort', '')}
{absender.get('telefon', '')} | {absender.get('email', '')}


{lead.get('name', '')}
{lead.get('strasse', '')}
{lead.get('plz', '')} {lead.get('ort', '')}


{_ortsname(absender.get('ort', ''))}, {heute}


Kurze Rückmeldung zu Ihrer Website


{anrede}

ich betreue Websites für Handwerks- und Dienstleistungsbetriebe hier in der
Region. Dabei habe ich mir auch Ihren Auftritt angesehen. Eine Sache ist mir
dabei sofort aufgefallen: {aufhaenger}

Die drei auffälligsten Punkte:

{aufzaehlung}

Die vollständige Auswertung liegt diesem Schreiben bei. Sie ist für Sie
kostenfrei, unabhängig davon, ob wir ins Geschäft kommen. Sie können damit
auch zu Ihrem bisherigen Dienstleister gehen - mir ist wichtiger, dass die
Punkte abgestellt werden, als von wem.

Falls Sie mögen, rufe ich Sie in der Woche ab dem {rueckruf} kurz an und
gehe die Punkte mit Ihnen durch. Wenn Ihnen das nicht recht ist, genügt
eine kurze Nachricht - dann höre ich nichts mehr von mir.

Mit freundlichen Grüßen


{absender.get('name', '')}


Anlage: Website-Analyse {lead.get('name', '')}, Stand {heute}

---
Hinweis nach Art. 14 DSGVO: Ihre Kontaktdaten (Firmenname, Anschrift, ggf.
Rufnummer und Website) stammen aus der öffentlich zugänglichen Datenbank
OpenStreetMap. Ich verarbeite sie zur einmaligen geschäftlichen
Kontaktaufnahme auf Grundlage meines berechtigten Interesses an Direktwerbung
(Art. 6 Abs. 1 lit. f DSGVO). Sie können der Verarbeitung jederzeit formlos
widersprechen (Art. 21 DSGVO), etwa unter {absender.get('email', '')}. Ihre
Daten werden dann gelöscht und für weitere Ansprachen gesperrt.
"""


def nachfass_mail(lead: dict[str, Any], audit: dict[str, Any], absender: dict[str, str]) -> str:
    ang = scoring.angebot(lead, audit)
    befunde = _top_befunde(audit, 3)
    aufzaehlung = "\n".join(f"  {i}. {_entkodieren(b['titel'])}" for i, b in enumerate(befunde, 1))

    return f"""!! NUR NACH GEFÜHRTEM GESPRÄCH VERSENDEN !!
Werbe-E-Mails ohne vorherige ausdrückliche Einwilligung sind auch gegenüber
Unternehmen nach § 7 Abs. 2 Nr. 2 UWG unzulässig und regelmäßig abmahnfähig.
Dieser Text ist die Zusammenfassung eines Telefonats, in dem der Versand
zugesagt wurde. Zusage in der Notiz zum Lead dokumentieren.

An      : {lead.get('email') or '<im Gespräch erfragt>'}
Betreff : Ihre Website-Analyse wie besprochen, {lead.get('name', '')}

Guten Tag,

wie eben am Telefon besprochen - hier die vollständige Analyse Ihrer
Website als PDF im Anhang.

Die drei Punkte, die ich zuerst angehen würde:

{aufzaehlung}

Ich habe Ihnen das als Festpreis gerechnet: {ang['paket']:.0f} EUR netto,
alles inklusive, feste Umsetzungsdauer. Wenn Sie mögen, übernehme ich
danach die laufende Betreuung für {ang['betreuung']:.0f} EUR im Monat -
monatlich kündbar, keine Mindestlaufzeit.

Wenn Sie mögen, setzen wir es diesen Monat um. Ein kurzes "ja" genügt,
den Rest übernehme ich.

Viele Grüße
{absender.get('name', '')}
{absender.get('telefon', '')}
{absender.get('email', '')}
"""


def einstiegsgespraech(
    lead: dict[str, Any], audit: dict[str, Any], absender: dict[str, str]
) -> str:
    """Kurzleitfaden für die persönliche Übergabe an der Tür.

    Ziel ist nicht das Projekt, sondern eine Zusage über wenige hundert Euro,
    die im Stehen fallen kann. Deshalb ist der Text kurz: Wer an der Tür
    ausholt, wird weggeschickt.
    """
    einstieg = angebote.einstieg_waehlen(audit)
    if not einstieg:
        return (
            f"{lead.get('name', '')}: kein Einstiegsangebot ableitbar - "
            "das Audit hat keinen Befund geliefert, der sich als "
            "Einzelmaßnahme verkaufen lässt. Diesen Lead überspringen."
        )

    bausteine = einstieg["bausteine"]
    liste = "\n".join(
        f"   - {b['titel']} ({b['preis']:.0f} EUR, {angebote.stunden_text(b['stunden'])})"
        for b in bausteine
    )
    ersparnis = einstieg["einzelpreise"] - einstieg["preis"]
    buendel = ""
    if len(bausteine) > 1 and ersparnis > 0:
        buendel = (
            f"\n   Zusammen {einstieg['preis']:.0f} EUR statt "
            f"{einstieg['einzelpreise']:.0f} EUR."
        )

    return f"""EINSTIEGSGESPRÄCH (persönliche Übergabe)
{'=' * 68}
Betrieb : {lead.get('name', '')}
Adresse : {lead.get('strasse', '')}, {lead.get('plz', '')} {lead.get('ort', '')}
Telefon : {lead.get('telefon') or 'nicht bekannt'}

ANGEBOT : {einstieg['preis']:.0f} EUR Festpreis, {angebote.stunden_text(einstieg['stunden'])} Aufwand
          ({einstieg['stundensatz']:.0f} EUR je Stunde){buendel}
{liste}

Offen bleiben danach {einstieg['weitere_offen']} weitere Befunde - das ist
der Anknüpfungspunkt für das nächste Gespräch, nicht für dieses.

1) AN DER TÜR (30 Sekunden, nicht mehr)
   "Guten Tag, {absender.get('name', '')}, ich bin aus {_ortsname(absender.get('ort', '')) or 'der Gegend'}.
    Ich habe mir die Websites der Betriebe hier angeschaut und Ihnen das
    hier ausgedruckt - kostet Sie nichts.
    {_entkodieren(einstieg['haken'])}"

   -> Ausdruck übergeben. Dann still sein.

2) WENN INTERESSE DA IST
   "Das mache ich Ihnen für {einstieg['preis']:.0f} Euro fest. Keine laufenden
    Kosten, keine Vertragsbindung. Ich brauche einmal Ihren Zugang, dann
    ist es {'heute noch' if einstieg['stunden'] <= 1.5 else 'in zwei Tagen'} erledigt."

   -> Nicht über weitere Punkte reden. Ein Thema, ein Preis, eine Zusage.

3) BEI ZUSAGE (sofort, im Stehen)
   [ ] Rechnung noch heute schreiben, Zahlungsziel 7 Tage
   [ ] Zugangsdaten notieren (Hoster, Redaktionssystem)
   [ ] Termin für die Umsetzung nennen und halten
   [ ] standortcheck stufe {lead.get('id', '?')} gewonnen --umsatz {einstieg['preis']:.0f}

4) BEI "MUSS ICH ÜBERLEGEN"
   "Klar. Ich bin Donnerstag wieder in der Gegend - soll ich kurz
    reinschauen?" -> standortcheck stufe {lead.get('id', '?')} gespraech --faellig {(date.today() + timedelta(days=4)).isoformat()}

5) BEI ABLEHNUNG
   Ausdruck dalassen, bedanken, gehen. Der Bericht arbeitet weiter.
   Kein Nachfassen bei klarem Nein.

NACH DER UMSETZUNG - der eigentliche Zweck des Einstiegs
   Wenn die Maßnahme sitzt und der Betrieb zufrieden ist:
   "Die anderen {einstieg['weitere_offen']} Punkte aus der Analyse stehen ja noch offen.
    Soll ich Ihnen das mal als Gesamtpaket rechnen?"
   -> Jetzt sind Sie kein Fremder mehr. Hier entsteht der große Auftrag.
"""
