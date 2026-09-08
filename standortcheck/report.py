"""Erzeugt den Auditbericht als eigenständige HTML-Datei.

Der Bericht ist das Verkaufsdokument: Er wird als PDF gedruckt und per Post
oder im Termin übergeben. Deshalb keine externen Schriften, keine
Fremdskripte - die Datei muss auf jedem Rechner und offline sauber aussehen.
"""

from __future__ import annotations

import html
import re
from datetime import date
from pathlib import Path
from typing import Any

FARBEN = {
    "kritisch": ("#b3261e", "#fdeceb"),
    "hoch": ("#a35200", "#fdf1e3"),
    "mittel": ("#7a5c00", "#fdf8e3"),
    "niedrig": ("#3d5a80", "#eef3f9"),
}
SCHWERE_TEXT = {
    "kritisch": "Kritisch",
    "hoch": "Hoch",
    "mittel": "Mittel",
    "niedrig": "Gering",
}
KATEGORIE_REIHENFOLGE = ["Recht", "Technik", "Sichtbarkeit", "Vertrauen", "Barrierefreiheit"]

CSS = """
* { box-sizing: border-box; }
body { margin:0; font-family: -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
       color:#1a1a1a; background:#f4f4f2; line-height:1.55; font-size:15px; }
.blatt { max-width: 860px; margin: 0 auto; background:#fff; padding: 48px 56px 64px; }
.kopf { display:flex; justify-content:space-between; align-items:flex-start;
        border-bottom:3px solid #1a1a1a; padding-bottom:20px; margin-bottom:32px; gap:24px; }
.kopf h1 { margin:0 0 6px; font-size:27px; letter-spacing:-0.02em; }
.kopf .sub { color:#5c5c5c; font-size:14px; }
.absender { text-align:right; font-size:12.5px; color:#5c5c5c; white-space:nowrap; }
.absender strong { display:block; color:#1a1a1a; font-size:14px; margin-bottom:3px; }

.ampel { display:flex; gap:20px; align-items:center; background:#faf9f7;
         border:1px solid #e3e0da; border-radius:10px; padding:22px 26px; margin-bottom:30px; }
.ring { width:104px; height:104px; flex:0 0 104px; border-radius:50%;
        display:flex; flex-direction:column; align-items:center; justify-content:center;
        color:#fff; font-weight:700; }
.ring .zahl { font-size:34px; line-height:1; }
.ring .label { font-size:10px; text-transform:uppercase; letter-spacing:0.09em; opacity:0.9; margin-top:3px; }
.ampel .text h2 { margin:0 0 6px; font-size:19px; }
.ampel .text p { margin:0; color:#4a4a4a; font-size:14.5px; }

.kennzahlen { display:grid; grid-template-columns:repeat(4,1fr); gap:12px; margin-bottom:34px; }
.kennzahl { background:#faf9f7; border:1px solid #e3e0da; border-radius:8px; padding:13px 15px; }
.kennzahl .wert { font-size:20px; font-weight:700; }
.kennzahl .name { font-size:11.5px; color:#666; text-transform:uppercase; letter-spacing:0.05em; margin-top:2px; }

h3.abschnitt { font-size:12px; text-transform:uppercase; letter-spacing:0.11em; color:#666;
               border-bottom:1px solid #e3e0da; padding-bottom:7px; margin:34px 0 18px; }

.befund { border:1px solid #e3e0da; border-left-width:5px; border-radius:7px;
          padding:16px 20px; margin-bottom:13px; page-break-inside:avoid; }
.befund .zeile { display:flex; justify-content:space-between; align-items:baseline; gap:14px; margin-bottom:8px; }
.befund h4 { margin:0; font-size:16.5px; }
.marke { font-size:10.5px; font-weight:700; text-transform:uppercase; letter-spacing:0.07em;
         padding:3px 9px; border-radius:20px; white-space:nowrap; }
.befund dl { margin:0; display:grid; grid-template-columns:112px 1fr; gap:5px 14px; font-size:14px; }
.befund dt { color:#6b6b6b; font-weight:600; font-size:12.5px; padding-top:1px; }
.befund dd { margin:0; }

table.plan { width:100%; border-collapse:collapse; font-size:14px; margin-top:6px; }
table.plan th { text-align:left; font-size:11.5px; text-transform:uppercase; letter-spacing:0.05em;
                color:#666; border-bottom:2px solid #1a1a1a; padding:8px 10px; }
table.plan td { border-bottom:1px solid #eae7e1; padding:9px 10px; vertical-align:top; }
table.plan tr:last-child td { border-bottom:none; }
table.plan td.num, table.plan th.num { text-align:right; white-space:nowrap; }
tr.summe td { font-weight:700; border-top:2px solid #1a1a1a; }

.angebot { background:#1a1a1a; color:#fff; border-radius:10px; padding:26px 30px; margin-top:30px; }
.angebot h3 { margin:0 0 10px; font-size:19px; color:#fff; }
.angebot p { margin:0 0 14px; color:#d6d6d6; font-size:14.5px; }
.angebot .preis { font-size:29px; font-weight:700; }
.angebot .preis small { font-size:14px; font-weight:400; color:#b8b8b8; }

.hinweis { font-size:12px; color:#6b6b6b; border-top:1px solid #e3e0da;
           margin-top:38px; padding-top:16px; }

@media print {
  body { background:#fff; font-size:11.5pt; }
  .blatt { max-width:none; padding:0; }
  .befund, .angebot, .ampel { page-break-inside:avoid; }
  @page { margin: 18mm 16mm; }
}
@media (max-width:640px) {
  .blatt { padding:26px 20px; }
  .kennzahlen { grid-template-columns:repeat(2,1fr); }
  .kopf { flex-direction:column; }
  .absender { text-align:left; }
  .befund dl { grid-template-columns:1fr; }
  .befund dt { padding-top:6px; }
}
"""


def _e(t: Any) -> str:
    return html.escape(str(t if t is not None else ""))


def _ampelfarbe(score: int) -> tuple[str, str, str]:
    if score >= 60:
        return "#b3261e", "Dringender Handlungsbedarf", (
            "Die Prüfung hat Mängel ergeben, die Anfragen kosten und teilweise "
            "ein rechtliches Risiko darstellen."
        )
    if score >= 30:
        return "#c77700", "Deutlicher Handlungsbedarf", (
            "Die Seite funktioniert grundsätzlich, verschenkt aber an mehreren "
            "Stellen Anfragen aus der Region."
        )
    if score >= 12:
        return "#4a7c2f", "Solide Basis mit Feinschliff", (
            "Die Grundlagen stimmen. Mit wenigen gezielten Korrekturen holen "
            "Sie spürbar mehr aus der Seite heraus."
        )
    return "#2e6b3f", "Sehr guter Zustand", (
        "Die Prüfung hat keine wesentlichen Mängel ergeben."
    )


def _stunden(h: float) -> str:
    """Aufwand in deutscher Schreibweise: 0,25 h statt 0.25 h."""
    text = f"{h:.2f}".rstrip("0").rstrip(".") or "0"
    return text.replace(".", ",") + " h"


def _euro(betrag: float) -> str:
    return f"{betrag:,.0f}".replace(",", ".") + " EUR"


def bericht_erzeugen(
    lead: dict[str, Any],
    audit: dict[str, Any],
    absender: dict[str, str],
    angebot: dict[str, float] | None = None,
    stundensatz: float = 75.0,
) -> str:
    """Erzeugt den Auditbericht. ``angebot`` stammt aus ``scoring.angebot``."""
    score = int(audit.get("schmerz_score", 0))
    farbe, ueberschrift, einleitung = _ampelfarbe(score)
    befunde = audit.get("befunde", [])

    kritisch = sum(1 for b in befunde if b["schwere"] == "kritisch")
    rechtsthemen = sum(1 for b in befunde if b["kategorie"] == "Recht")
    aufwand = audit.get("aufwand_h") or sum(b.get("aufwand_h", 0) for b in befunde)

    ladezeit = audit.get("ladezeit_ms")
    if not ladezeit:
        ladetext = "n. v."
    elif ladezeit < 100:
        ladetext = "&lt; 0,1 s"
    else:
        ladetext = f"{ladezeit/1000:.1f} s".replace(".", ",")

    # -- Befunde nach Kategorie ------------------------------------------
    nach_kategorie: dict[str, list[dict[str, Any]]] = {}
    for b in befunde:
        nach_kategorie.setdefault(b["kategorie"], []).append(b)

    abschnitte = []
    for kat in KATEGORIE_REIHENFOLGE + sorted(set(nach_kategorie) - set(KATEGORIE_REIHENFOLGE)):
        eintraege = nach_kategorie.get(kat)
        if not eintraege:
            continue
        karten = []
        for b in eintraege:
            rand, hintergrund = FARBEN.get(b["schwere"], FARBEN["niedrig"])
            karten.append(f"""
        <div class="befund" style="border-left-color:{rand}">
          <div class="zeile">
            <h4>{_e(b['titel'])}</h4>
            <span class="marke" style="color:{rand};background:{hintergrund}">{_e(SCHWERE_TEXT.get(b['schwere'], b['schwere']))}</span>
          </div>
          <dl>
            <dt>Befund</dt><dd>{_e(b['befund'])}</dd>
            <dt>Auswirkung</dt><dd>{_e(b['wirkung'])}</dd>
            <dt>Empfehlung</dt><dd>{_e(b['massnahme'])}</dd>
          </dl>
        </div>""")
        abschnitte.append(
            f'<h3 class="abschnitt">{_e(kat)} &mdash; {len(eintraege)} Befund'
            f'{"e" if len(eintraege) != 1 else ""}</h3>' + "".join(karten)
        )

    if not befunde:
        abschnitte.append(
            '<h3 class="abschnitt">Ergebnis</h3><div class="befund" '
            'style="border-left-color:#2e6b3f"><h4>Keine wesentlichen Mängel gefunden</h4>'
            "<p>Die automatisierte Prüfung hat keine Auffälligkeiten ergeben.</p></div>"
        )

    # -- Maßnahmenplan ----------------------------------------------------
    zeilen = []
    for b in sorted(befunde, key=lambda x: {"kritisch": 0, "hoch": 1, "mittel": 2, "niedrig": 3}[x["schwere"]]):
        stunden = b.get("aufwand_h", 1)
        zeilen.append(
            f"<tr><td>{_e(b['titel'])}</td><td>{_e(SCHWERE_TEXT.get(b['schwere'], ''))}</td>"
            f'<td class="num">{_stunden(stunden)}</td>'
            f'<td class="num">{_euro(stunden * stundensatz)}</td></tr>'
        )
    listenpreis = aufwand * stundensatz
    zeilen.append(
        f'<tr class="summe"><td>Gesamt</td><td></td><td class="num">{_stunden(aufwand)}</td>'
        f'<td class="num">{_euro(listenpreis)}</td></tr>'
    )

    angebot = angebot or {}
    paket = float(angebot.get("paket") or round(listenpreis * 0.82, -1))
    betreuung = float(angebot.get("betreuung") or 0)
    ersparnis = listenpreis - paket

    if ersparnis >= 50:
        einleitung_angebot = (
            f"Einzeln beauftragt summieren sich die Ma&szlig;nahmen auf "
            f"{_euro(listenpreis)}. Gemeinsam umgesetzt entf&auml;llt der "
            f"wiederholte Einarbeitungsaufwand &mdash; das sind "
            f"{_euro(ersparnis)} weniger."
        )
    elif angebot.get("neuaufbau"):
        einleitung_angebot = (
            "Der Betrag umfasst den vollst&auml;ndigen Neuaufbau: Struktur, "
            "Texte, Bilder, Rechtstexte und die Einrichtung beim Hoster."
        )
    else:
        einleitung_angebot = (
            "Alle oben genannten Ma&szlig;nahmen in einem Durchgang, "
            "zum Festpreis und mit fester Umsetzungsdauer."
        )

    betreuungszeile = ""
    if betreuung > 0:
        betreuungszeile = (
            f'<p style="margin:14px 0 0">Optional danach: laufende Betreuung '
            f'f&uuml;r {_euro(betreuung)} im Monat &mdash; Aktualisierungen, '
            f'Sicherungen und Erreichbarkeits&uuml;berwachung. Monatlich k&uuml;ndbar, '
            f'keine Mindestlaufzeit.</p>'
        )

    website_zeile = lead.get("website") or "keine Website hinterlegt"
    heute = date.today().strftime("%d.%m.%Y")

    return f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Website-Analyse {_e(lead.get('name', ''))}</title>
<style>{CSS}</style>
</head>
<body>
<div class="blatt">

  <div class="kopf">
    <div>
      <h1>Website-Analyse</h1>
      <div class="sub">{_e(lead.get('name', ''))}
        {(' &middot; ' + _e(lead.get('ort'))) if lead.get('ort') else ''}<br>
        {_e(website_zeile)} &middot; gepr&uuml;ft am {heute}</div>
    </div>
    <div class="absender">
      <strong>{_e(absender.get('name', ''))}</strong>
      {_e(absender.get('strasse', ''))}<br>
      {_e(absender.get('ort', ''))}<br>
      {_e(absender.get('telefon', ''))}<br>
      {_e(absender.get('email', ''))}
    </div>
  </div>

  <div class="ampel">
    <div class="ring" style="background:{farbe}">
      <span class="zahl">{score}</span>
      <span class="label">von 100</span>
    </div>
    <div class="text">
      <h2>{_e(ueberschrift)}</h2>
      <p>{_e(einleitung)}</p>
    </div>
  </div>

  <div class="kennzahlen">
    <div class="kennzahl"><div class="wert">{len(befunde)}</div><div class="name">Befunde</div></div>
    <div class="kennzahl"><div class="wert">{kritisch}</div><div class="name">davon kritisch</div></div>
    <div class="kennzahl"><div class="wert">{rechtsthemen}</div><div class="name">Rechtsthemen</div></div>
    <div class="kennzahl"><div class="wert">{ladetext}</div><div class="name">Ladezeit</div></div>
  </div>

  {''.join(abschnitte)}

  <h3 class="abschnitt">Ma&szlig;nahmen und Aufwand</h3>
  <table class="plan">
    <thead><tr><th>Ma&szlig;nahme</th><th>Priorit&auml;t</th>
    <th class="num">Aufwand</th><th class="num">Einzeln</th></tr></thead>
    <tbody>{''.join(zeilen)}</tbody>
  </table>

  <div class="angebot">
    <h3>Vorschlag: alles in einem Durchgang</h3>
    <p>{einleitung_angebot}</p>
    <div class="preis">{_euro(paket)} <small>netto, Festpreis</small></div>
    {betreuungszeile}
  </div>

  <div class="hinweis">
    Die Analyse beruht auf einer automatisierten Pr&uuml;fung der &ouml;ffentlich
    abrufbaren Startseite am {heute}. Die Hinweise zu Impressum, Datenschutz
    und Barrierefreiheit benennen technische Auff&auml;lligkeiten und stellen
    keine Rechtsberatung dar; die rechtliche Bewertung im Einzelfall
    &mdash; einschlie&szlig;lich m&ouml;glicher Ausnahmen f&uuml;r Kleinstunternehmen &mdash;
    bleibt einer fachkundigen Pr&uuml;fung vorbehalten.
    Angaben ohne Gew&auml;hr.
  </div>

</div>
</body>
</html>"""


def dateiname(lead: dict[str, Any]) -> str:
    roh = f"{lead.get('id', 0):04d}-{lead.get('name', 'bericht')}"
    sauber = re.sub(r"[^\w\s-]", "", roh, flags=re.UNICODE).strip()
    sauber = re.sub(r"[\s_]+", "-", sauber).lower()
    umlaute = {"ä": "ae", "ö": "oe", "ü": "ue", "ß": "ss"}
    for a, b in umlaute.items():
        sauber = sauber.replace(a, b)
    return f"{sauber[:70]}.html"


def schreiben(pfad: Path, inhalt: str) -> Path:
    pfad.parent.mkdir(parents=True, exist_ok=True)
    pfad.write_text(inhalt, encoding="utf-8")
    return pfad
