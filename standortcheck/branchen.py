"""Branchenkatalog: OSM-Tags, Zahlungsbereitschaft und Ansprache.

Die Auswahl ist bewusst auf Gewerke zugeschnitten, bei denen ein einzelner
Neukunde vierstellig wert ist. Dort rechnet sich eine Website-Investition
für den Betrieb selbst - das ist das stärkste Verkaufsargument.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Branche:
    schluessel: str
    bezeichnung: str
    osm_filter: tuple[str, ...]
    # Was ein einzelner gewonnener Kunde dem Betrieb typischerweise wert ist.
    kundenwert_eur: int
    # Realistischer Projektpreis für eine kompakte Website in diesem Gewerk.
    projektpreis_eur: int
    # Monatlicher Betreuungspreis (Wartung, Aktualisierungen, Erreichbarkeit).
    betreuung_eur: int
    aufhaenger: str


KATALOG: dict[str, Branche] = {
    b.schluessel: b
    for b in [
        Branche(
            "dachdecker", "Dachdecker",
            ('nwr["craft"="roofer"]',),
            4500, 1900, 59,
            "Ein einziger Dachauftrag deckt die Investition mehrfach.",
        ),
        Branche(
            "elektriker", "Elektrobetrieb",
            ('nwr["craft"="electrician"]', 'nwr["shop"="electrical"]'),
            2200, 1700, 59,
            "Wallbox und Photovoltaik werden fast ausschließlich online gesucht.",
        ),
        Branche(
            "sanitaer", "Sanitär, Heizung, Klima",
            ('nwr["craft"="plumber"]', 'nwr["craft"="hvac"]'),
            3800, 1900, 59,
            "Heizungstausch und Wärmepumpe sind hochpreisige Suchanfragen.",
        ),
        Branche(
            "tischler", "Tischlerei und Schreinerei",
            ('nwr["craft"="carpenter"]', 'nwr["craft"="joiner"]'),
            3500, 1800, 49,
            "Möbel nach Maß werden über Bilder verkauft - die Seite ist das Schaufenster.",
        ),
        Branche(
            "maler", "Maler und Lackierer",
            ('nwr["craft"="painter"]',),
            2400, 1500, 49,
            "Vorher-nachher-Bilder verkaufen den Auftrag schon vor dem Termin.",
        ),
        Branche(
            "garten", "Garten- und Landschaftsbau",
            ('nwr["craft"="gardener"]', 'nwr["landuse"="landscaping"]'),
            3200, 1700, 49,
            "Gartenprojekte werden saisonal und regional gesucht.",
        ),
        Branche(
            "kfz", "Kfz-Werkstatt",
            ('nwr["shop"="car_repair"]',),
            600, 1400, 59,
            "Termin- und Reifenanfragen laufen fast nur noch über Handy und Karte.",
        ),
        Branche(
            "steuerberater", "Steuerberatung",
            ('nwr["office"="tax_advisor"]', 'nwr["office"="accountant"]'),
            2800, 2400, 89,
            "Mandate sind langlebig; Vertrauen entsteht über den Außenauftritt.",
        ),
        Branche(
            "anwalt", "Rechtsanwaltskanzlei",
            ('nwr["office"="lawyer"]',),
            2500, 2600, 89,
            "Eine Kanzlei ohne saubere Rechtstexte auf der eigenen Seite fällt auf.",
        ),
        Branche(
            "zahnarzt", "Zahnarztpraxis",
            ('nwr["healthcare"="dentist"]', 'nwr["amenity"="dentist"]'),
            1200, 2400, 89,
            "Selbstzahlerleistungen werden ausschließlich online recherchiert.",
        ),
        Branche(
            "physio", "Physiotherapie",
            ('nwr["healthcare"="physiotherapist"]',),
            700, 1500, 59,
            "Online-Terminbuchung entlastet spürbar das Telefon.",
        ),
        Branche(
            "restaurant", "Gastronomie",
            ('nwr["amenity"="restaurant"]',),
            60, 1200, 49,
            "Speisekarte und Öffnungszeiten müssen mobil sofort lesbar sein.",
        ),
        Branche(
            "hotel", "Hotel und Pension",
            ('nwr["tourism"="hotel"]', 'nwr["tourism"="guest_house"]'),
            450, 2600, 99,
            "Jede Direktbuchung spart zweistellige Portalprovision.",
        ),
        Branche(
            "immobilien", "Immobilienmakler",
            ('nwr["office"="estate_agent"]',),
            6000, 2400, 89,
            "Eigentümer prüfen den Makler vor dem Erstkontakt im Netz.",
        ),
        Branche(
            "bau", "Bauunternehmen",
            ('nwr["craft"="builder"]', 'nwr["office"="construction_company"]'),
            8000, 2200, 69,
            "Bei Auftragsgrößen im fünfstelligen Bereich zählt der erste Eindruck.",
        ),
        Branche(
            "fahrschule", "Fahrschule",
            ('nwr["amenity"="driving_school"]',),
            2000, 1400, 49,
            "Fahrschüler vergleichen ausschließlich mobil.",
        ),
    ]
}


def aufloesen(schluessel: str) -> Branche:
    if schluessel not in KATALOG:
        moeglich = ", ".join(sorted(KATALOG))
        raise KeyError(f"Unbekannte Branche '{schluessel}'. Verfügbar: {moeglich}")
    return KATALOG[schluessel]


def liste() -> list[Branche]:
    return sorted(KATALOG.values(), key=lambda b: -b.projektpreis_eur)
