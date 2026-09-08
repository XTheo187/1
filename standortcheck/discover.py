"""Lead-Recherche über OpenStreetMap.

Warum OpenStreetMap: Die Abfrage ist kostenfrei und die Daten stehen unter
der ODbL. Das passt zu einem Startkapital von 500 Euro, bei dem kein Budget
für Datenbank-Abonnements übrig ist.

Zwei Schritte: Nominatim übersetzt den Ortsnamen in Koordinaten, Overpass
liefert die Betriebe im Umkreis. Die naheliegendere Variante über
Overpass-Gebietsfilter ("area") wurde verworfen - sie läuft auf der
öffentlichen Instanz regelmäßig ins Zeitlimit, während die Umkreissuche in
Sekunden antwortet. Der Umkreis passt ohnehin besser zum Geschäft: Ein
lokaler Dienstleister denkt in Fahrminuten, nicht in Gemeindegrenzen.

Rücksicht auf die Gegenstelle: Beide Dienste werden von Freiwilligen
betrieben. Der Client hält die Pausen ein, die deren Nutzungsbedingungen
verlangen, und bricht bei Überlastmeldungen ab, statt zu hämmern.
"""

from __future__ import annotations

import json
import time
import urllib.error
import urllib.parse
import urllib.request
from typing import Any, Iterator

from . import branchen

OVERPASS_SERVER = [
    "https://overpass-api.de/api/interpreter",
    "https://overpass.kumi.systems/api/interpreter",
]
NOMINATIM = "https://nominatim.openstreetmap.org/search"

# Nominatim erlaubt höchstens eine Anfrage je Sekunde, Overpass verlangt
# Pausen zwischen umfangreichen Abfragen.
PAUSE_NOMINATIM = 1.2
PAUSE_OVERPASS = 3.0
TIMEOUT_ABFRAGE = 60
TIMEOUT_VERBINDUNG = 90

USER_AGENT = "Standortcheck/1.0 (lokale Leadrecherche; Kontakt via Impressum)"


class RechercheFehler(RuntimeError):
    pass


# --------------------------------------------------------------------------
# Ortsauflösung
# --------------------------------------------------------------------------


def ort_aufloesen(ort: str, laender: str = "de,at,ch") -> tuple[float, float, str]:
    """Übersetzt einen Ortsnamen in Koordinaten.

    Gibt ``(lat, lon, anzeigename)`` zurück, damit der Aufrufer prüfen kann,
    ob der richtige Ort getroffen wurde - „Neustadt“ gibt es reichlich.
    """
    parameter = urllib.parse.urlencode({
        "q": ort,
        "format": "json",
        "limit": "1",
        "countrycodes": laender,
        "addressdetails": "0",
    })
    anfrage = urllib.request.Request(
        f"{NOMINATIM}?{parameter}",
        headers={"User-Agent": USER_AGENT, "Accept": "application/json",
                 "Accept-Language": "de"},
    )
    try:
        with urllib.request.urlopen(anfrage, timeout=30) as antwort:
            treffer = json.loads(antwort.read().decode("utf-8"))
    except Exception as e:
        raise RechercheFehler(f"Ort '{ort}' konnte nicht aufgelöst werden: {e}") from e
    finally:
        time.sleep(PAUSE_NOMINATIM)

    if not treffer:
        raise RechercheFehler(
            f"Kein Ort namens '{ort}' gefunden. Schreibweise prüfen, bei "
            "mehrdeutigen Namen das Bundesland ergänzen, etwa "
            "'Neustadt an der Weinstraße'."
        )
    erster = treffer[0]
    return float(erster["lat"]), float(erster["lon"]), erster.get("display_name", ort)


# --------------------------------------------------------------------------
# Overpass
# --------------------------------------------------------------------------


def _filter_zerlegen(ausdruck: str) -> tuple[str, str] | None:
    """'nwr["craft"="roofer"]' -> ('craft', 'roofer')."""
    try:
        inhalt = ausdruck[ausdruck.index("[") + 1 : ausdruck.rindex("]")].replace('"', "")
    except ValueError:
        return None
    if "=" not in inhalt:
        return None
    schluessel, wert = inhalt.split("=", 1)
    return schluessel, wert


def _umkreis_abfrage(
    lat: float, lon: float, filter_ausdruecke: tuple[str, ...], radius_km: float
) -> str:
    """Baut eine Umkreisabfrage mit möglichst wenigen Klauseln.

    Jede einzelne around-Klausel kostet die Overpass-Instanz eine eigene
    räumliche Suche. Acht Klauseln liefen auf der öffentlichen Instanz
    reproduzierbar ins Zeitlimit (HTTP 504). Deshalb werden alle Werte
    desselben Tag-Schlüssels zu einer Klausel mit regulärem Ausdruck
    zusammengefasst - aus acht Suchen werden so zwei bis drei.
    """
    radius_m = int(radius_km * 1000)
    nach_schluessel: dict[str, list[str]] = {}
    for f in filter_ausdruecke:
        zerlegt = _filter_zerlegen(f)
        if zerlegt is None:
            continue
        schluessel, wert = zerlegt
        nach_schluessel.setdefault(schluessel, []).append(wert)

    klauseln = []
    for schluessel, werte in nach_schluessel.items():
        eindeutig = sorted(set(werte))
        if len(eindeutig) == 1:
            bedingung = f'["{schluessel}"="{eindeutig[0]}"]'
        else:
            bedingung = f'["{schluessel}"~"^({"|".join(eindeutig)})$"]'
        klauseln.append(f"nwr{bedingung}(around:{radius_m},{lat},{lon});")

    teile = "\n  ".join(klauseln)
    return f"""[out:json][timeout:{TIMEOUT_ABFRAGE}];
(
  {teile}
);
out center tags;"""


def _senden(abfrage: str) -> dict[str, Any]:
    letzter_fehler: Exception | None = None
    for server in OVERPASS_SERVER:
        daten = urllib.parse.urlencode({"data": abfrage}).encode()
        anfrage = urllib.request.Request(
            server, data=daten,
            headers={"User-Agent": USER_AGENT, "Accept": "application/json"},
        )
        try:
            with urllib.request.urlopen(anfrage, timeout=TIMEOUT_VERBINDUNG) as antwort:
                return json.loads(antwort.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code in (429, 504):
                letzter_fehler = RechercheFehler(
                    f"Overpass ist ausgelastet (HTTP {e.code}). Einige Minuten "
                    "warten - der Dienst ist ein Freiwilligenprojekt."
                )
                time.sleep(PAUSE_OVERPASS)
                continue
            letzter_fehler = RechercheFehler(f"Overpass antwortete mit HTTP {e.code}")
        except Exception as e:
            letzter_fehler = e
        time.sleep(PAUSE_OVERPASS)
    raise RechercheFehler(f"Recherche fehlgeschlagen: {letzter_fehler}")


def _element_zu_lead(
    el: dict[str, Any], branche: branchen.Branche, fallback_ort: str
) -> dict[str, Any] | None:
    tags = el.get("tags") or {}
    name = (tags.get("name") or tags.get("operator") or "").strip()
    if not name:
        return None  # ohne Namen ist kein Anschreiben möglich

    mittelpunkt = el.get("center") or {}
    strasse = " ".join(
        t for t in [tags.get("addr:street", ""), tags.get("addr:housenumber", "")] if t
    ).strip()

    return {
        "name": name,
        "branche": branche.bezeichnung,
        "ort": tags.get("addr:city") or fallback_ort,
        "plz": tags.get("addr:postcode", ""),
        "strasse": strasse,
        "telefon": (tags.get("phone") or tags.get("contact:phone") or "").strip(),
        "email": (tags.get("email") or tags.get("contact:email") or "").strip(),
        "website": (
            tags.get("website") or tags.get("contact:website") or tags.get("url") or ""
        ).strip(),
        "quelle": "openstreetmap",
        "quelle_id": f"{el.get('type')}/{el.get('id')}",
        "lat": el.get("lat") or mittelpunkt.get("lat"),
        "lon": el.get("lon") or mittelpunkt.get("lon"),
    }


def suchen(
    ort: str,
    branchen_schluessel: list[str],
    radius_km: float = 12.0,
    koordinaten: tuple[float, float] | None = None,
) -> Iterator[dict[str, Any]]:
    """Liefert Leads im Umkreis eines Ortes für eine oder mehrere Branchen.

    Alle Branchen laufen in einer einzigen Overpass-Abfrage. Das schont die
    Gegenstelle und ist deutlich schneller als eine Abfrage je Gewerk.
    """
    kandidaten = [branchen.aufloesen(s) for s in branchen_schluessel]

    if koordinaten:
        lat, lon = koordinaten
    else:
        lat, lon, _ = ort_aufloesen(ort)

    # Filter je Branche merken, um die Treffer später wieder zuzuordnen.
    filter_zu_branche: dict[str, branchen.Branche] = {}
    alle_filter: list[str] = []
    for b in kandidaten:
        for f in b.osm_filter:
            alle_filter.append(f)
            filter_zu_branche[f] = b

    antwort = _senden(_umkreis_abfrage(lat, lon, tuple(alle_filter), radius_km))

    for el in antwort.get("elements", []):
        branche = _branche_bestimmen(el, kandidaten)
        if branche is None:
            continue
        lead = _element_zu_lead(el, branche, ort)
        if lead:
            yield lead


def _branche_bestimmen(
    el: dict[str, Any], kandidaten: list[branchen.Branche]
) -> branchen.Branche | None:
    """Ordnet ein OSM-Element der Branche zu, deren Filter darauf passt."""
    tags = el.get("tags") or {}
    for b in kandidaten:
        for f in b.osm_filter:
            zerlegt = _filter_zerlegen(f)
            if zerlegt and tags.get(zerlegt[0]) == zerlegt[1]:
                return b
    return None
