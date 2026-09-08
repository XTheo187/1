"""Priorisierung: Welchen Lead rufe ich zuerst an?

Der Schmerz-Score aus dem Audit sagt nur, wie schlecht die Seite ist. Für
die Reihenfolge zählt zusätzlich, ob der Betrieb überhaupt erreichbar ist
und was ein Abschluss wert wäre. Bei 20 Stunden Wochenkapazität ist die
Reihenfolge der Anrufe die wichtigste Stellschraube überhaupt.
"""

from __future__ import annotations

from typing import Any

from . import branchen

# Rabatt auf die Einzelsumme, wenn alles in einem Durchgang beauftragt wird.
PAKET_FAKTOR = 0.82
# Unter diesem Betrag deckt ein Auftrag die Akquisekosten nicht.
MINDESTPREIS = 890.0
# Befunde, die bedeuten: Ein nutzbarer Auftritt existiert schlicht nicht.
KEIN_NUTZBARER_AUFTRITT = {
    "keine_website", "fremdinhalte", "domain_geparkt",
    "nicht_erreichbar", "tls_kaputt",
}

# Befunde, die im Gespräch sofort zünden, weil sie ein konkretes Risiko oder
# einen sichtbaren Mangel benennen.
ZUGKRAFT = {
    "kein_impressum": 12,
    "keine_datenschutzerklaerung": 11,
    "tracking_ohne_einwilligung": 10,
    "kein_viewport": 12,
    "kein_https": 11,
    "tls_kaputt": 12,
    "nicht_erreichbar": 12,
    "keine_website": 10,
    "fremdinhalte": 14,
    "domain_geparkt": 13,
    "verwaist": 8,
    "schriften_extern": 6,
    "keine_telefonnummer": 6,
    "frames": 8,
    "sehr_langsam": 6,
}


def branche_zu_schluessel(bezeichnung: str | None) -> str | None:
    if not bezeichnung:
        return None
    for b in branchen.KATALOG.values():
        if b.bezeichnung == bezeichnung:
            return b.schluessel
    return None


def angebot(
    lead: dict[str, Any],
    audit: dict[str, Any] | None,
    stundensatz: float = 75.0,
) -> dict[str, float]:
    """Rechnet Paketpreis und Betreuung aus dem gemessenen Aufwand.

    Einzige Quelle für jeden Preis: Bericht, Pipeline-Wert und Gespräch
    ziehen ihre Zahlen hier her. Sonst nennt das Angebot einen anderen
    Betrag als der beiliegende Maßnahmenplan - und genau das kostet
    im Termin die Glaubwürdigkeit.
    """
    schluessel = branche_zu_schluessel(lead.get("branche"))
    b = branchen.KATALOG.get(schluessel) if schluessel else None
    betreuung = float(b.betreuung_eur if b else 49)

    aufwand = float((audit or {}).get("aufwand_h") or 0)
    listenpreis = aufwand * stundensatz

    # Paketrabatt: gebündelt entfällt die wiederholte Einarbeitung.
    paket = round(listenpreis * PAKET_FAKTOR, -1)

    # Kein nutzbarer Auftritt vorhanden: Der Aufwand steckt dann nicht in
    # Einzelbefunden, sondern im kompletten Neuaufbau. Das gilt auch, wenn
    # unter der Adresse zwar etwas liegt - nur eben nicht der Betrieb.
    codes = {b.get("code") for b in (audit or {}).get("befunde", [])}
    ohne_website = (
        not (lead.get("website") or "").strip()
        or bool(codes & KEIN_NUTZBARER_AUFTRITT)
    )
    if ohne_website:
        paket = max(paket, float(b.projektpreis_eur if b else 1600))

    # Untergrenze: darunter deckt der Auftrag die Akquisekosten nicht.
    paket = max(paket, MINDESTPREIS)

    return {
        "listenpreis": round(listenpreis, 2),
        "paket": paket,
        "betreuung": betreuung,
        "jahr_eins": round(paket + betreuung * 12, 2),
        "aufwand_h": aufwand,
        "neuaufbau": ohne_website,
    }


def deal_wert(lead: dict[str, Any], audit: dict[str, Any] | None) -> float:
    """Pipeline-Wert: Paketpreis plus zwölf Monate Betreuung."""
    return angebot(lead, audit)["jahr_eins"]


def prioritaet(lead: dict[str, Any], audit: dict[str, Any] | None) -> dict[str, Any]:
    """Ergibt einen Prioritätswert von 0 bis 100 samt Begründung."""
    gruende: list[str] = []
    punkte = 0.0

    schmerz = (audit or {}).get("schmerz_score", 0)
    punkte += schmerz * 0.45
    if schmerz >= 60:
        gruende.append("gravierende Mängel auf der Website")
    elif schmerz >= 30:
        gruende.append("deutlicher Handlungsbedarf")

    codes = {b["code"] for b in (audit or {}).get("befunde", [])}
    zug = sum(ZUGKRAFT.get(c, 0) for c in codes)
    punkte += min(28, zug)
    if zug >= 20:
        gruende.append("mehrere sofort ansprechbare Risiken")

    # Erreichbarkeit entscheidet, ob aus dem Lead überhaupt ein Gespräch wird.
    if lead.get("telefon"):
        punkte += 14
        gruende.append("Rufnummer bekannt")
    else:
        punkte -= 6
        gruende.append("keine Rufnummer hinterlegt")

    wert = deal_wert(lead, audit)
    punkte += min(14, wert / 300)
    if wert >= 3000:
        gruende.append(f"Auftragswert im ersten Jahr rund {wert:.0f} EUR")

    if lead.get("strasse") and lead.get("plz"):
        punkte += 4  # postalische Ansprache ist rechtlich der sichere Weg
        gruende.append("Anschrift für Brief vorhanden")

    return {
        "prioritaet": int(max(0, min(100, round(punkte)))),
        "deal_wert": wert,
        "begruendung": gruende,
    }


def rangliste(eintraege: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(eintraege, key=lambda e: -e.get("prioritaet", 0))
