"""Website-Audit ohne Fremdbibliotheken.

Prüft eine Unternehmenswebsite auf technische, rechtliche und
verkaufsrelevante Schwachstellen und erzeugt daraus einen Schmerz-Score.
Jeder Befund trägt seine Verkaufsargumentation und einen Aufwandsschätzer
gleich mit - das ist die Grundlage für Bericht und Angebot.

Rechtlicher Hinweis: Die Prüfungen sind technische Indizien, keine
Rechtsberatung. Sie zeigen, wo ein Gespräch mit dem Betrieb lohnt.
"""

from __future__ import annotations

import gzip
import re
import socket
import ssl
import time
import urllib.error
import urllib.parse
import urllib.request
import zlib
from dataclasses import dataclass
from datetime import date
from html.parser import HTMLParser
from typing import Any

USER_AGENT = (
    "Mozilla/5.0 (compatible; Standortcheck/1.0; Website-Qualitaetspruefung; "
    "+kontakt per Impressum)"
)
TIMEOUT = 12
MAX_BYTES = 3_000_000  # Abbruch bei Riesenseiten, schützt vor Zeitfressern

SCHWERE_GEWICHT = {"kritisch": 1.0, "hoch": 0.7, "mittel": 0.45, "niedrig": 0.2}


@dataclass
class Befund:
    code: str
    titel: str
    kategorie: str  # Technik | Recht | Sichtbarkeit | Vertrauen | Barrierefreiheit
    schwere: str  # kritisch | hoch | mittel | niedrig
    punkte: int
    befund: str
    wirkung: str
    massnahme: str
    aufwand_h: float = 1.0

    def as_dict(self) -> dict[str, Any]:
        return self.__dict__.copy()


# --------------------------------------------------------------------------
# HTML-Auswertung
# --------------------------------------------------------------------------


class SeitenParser(HTMLParser):
    """Sammelt genau die Signale, die für die Prüfungen gebraucht werden."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.titel = ""
        self._in_titel = False
        self.meta: dict[str, str] = {}
        self.h1: list[str] = []
        self._in_h1 = False
        self.links: list[tuple[str, str]] = []  # (href, linktext)
        self._aktueller_link: str | None = None
        self._linktext: list[str] = []
        self.bilder: list[dict[str, str]] = []
        self.skripte: list[str] = []
        self.stylesheets: list[str] = []
        self.hat_favicon = False
        self.html_lang = ""
        self.generator = ""
        self.jsonld: list[str] = []
        self._in_jsonld = False
        self.frames = 0
        self.tabellen = 0
        self.formulare = 0
        self.eingabefelder = 0
        self.labels = 0
        self.text_teile: list[str] = []
        self.inline_style_bytes = 0

    # -- Tags ---------------------------------------------------------------
    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        a = {k.lower(): (v or "") for k, v in attrs}
        if tag == "title":
            self._in_titel = True
        elif tag == "html":
            self.html_lang = a.get("lang", "")
        elif tag == "meta":
            name = (a.get("name") or a.get("property") or a.get("http-equiv") or "").lower()
            if name:
                self.meta[name] = a.get("content", "")
            if a.get("charset"):
                self.meta["charset"] = a["charset"]
            if name == "generator":
                self.generator = a.get("content", "")
        elif tag == "link":
            rel = a.get("rel", "").lower()
            if "icon" in rel:
                self.hat_favicon = True
            if "stylesheet" in rel and a.get("href"):
                self.stylesheets.append(a["href"])
        elif tag == "h1":
            self._in_h1 = True
        elif tag == "a":
            self._aktueller_link = a.get("href", "")
            self._linktext = []
        elif tag == "img":
            self.bilder.append(
                {
                    "src": a.get("src", ""),
                    "alt": a.get("alt", "__FEHLT__" if "alt" not in a else a.get("alt", "")),
                    "loading": a.get("loading", ""),
                    "width": a.get("width", ""),
                    "height": a.get("height", ""),
                }
            )
        elif tag == "script":
            if a.get("src"):
                self.skripte.append(a["src"])
            if (a.get("type") or "").lower() == "application/ld+json":
                self._in_jsonld = True
        elif tag in ("frame", "frameset", "iframe"):
            if tag != "iframe":
                self.frames += 1
        elif tag == "table":
            self.tabellen += 1
        elif tag == "form":
            self.formulare += 1
        elif tag in ("input", "textarea", "select"):
            if a.get("type", "").lower() not in ("hidden", "submit", "button"):
                self.eingabefelder += 1
        elif tag == "label":
            self.labels += 1

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._in_titel = False
        elif tag == "h1":
            self._in_h1 = False
        elif tag == "script":
            self._in_jsonld = False
        elif tag == "a" and self._aktueller_link is not None:
            self.links.append((self._aktueller_link, " ".join(self._linktext).strip()))
            self._aktueller_link = None
            self._linktext = []

    def handle_data(self, data: str) -> None:
        if self._in_titel:
            self.titel += data
        if self._in_h1:
            self.h1.append(data.strip())
        if self._in_jsonld:
            self.jsonld.append(data)
        if self._aktueller_link is not None:
            self._linktext.append(data.strip())
        stripped = data.strip()
        if stripped:
            self.text_teile.append(stripped)

    @property
    def text(self) -> str:
        return " ".join(self.text_teile)


# --------------------------------------------------------------------------
# Abruf
# --------------------------------------------------------------------------


def _entpacken(rohdaten: bytes, encoding: str) -> bytes:
    try:
        if encoding == "gzip":
            return gzip.decompress(rohdaten)
        if encoding == "deflate":
            return zlib.decompress(rohdaten, -zlib.MAX_WBITS)
    except Exception:
        return rohdaten
    return rohdaten


def url_normalisieren(url: str) -> str:
    url = (url or "").strip()
    if not url:
        return ""
    if not re.match(r"^https?://", url, re.I):
        url = "https://" + url.lstrip("/")
    return url


def seite_laden(url: str) -> dict[str, Any]:
    """Lädt eine Seite und liefert Rohdaten plus Messwerte."""
    ergebnis: dict[str, Any] = {
        "url": url,
        "erreichbar": False,
        "fehler": None,
        "status_code": None,
        "endgueltige_url": None,
        "ladezeit_ms": None,
        "seitengroesse": None,
        "html": "",
        "header": {},
        "tls_fehler": None,
    }
    anfrage = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "text/html,application/xhtml+xml,*/*;q=0.8",
            "Accept-Language": "de-DE,de;q=0.9",
            "Accept-Encoding": "gzip, deflate",
        },
    )
    start = time.perf_counter()
    try:
        with urllib.request.urlopen(anfrage, timeout=TIMEOUT) as antwort:
            roh = antwort.read(MAX_BYTES)
            ergebnis["ladezeit_ms"] = int((time.perf_counter() - start) * 1000)
            ergebnis["status_code"] = antwort.status
            ergebnis["endgueltige_url"] = antwort.geturl()
            ergebnis["header"] = {k.lower(): v for k, v in antwort.headers.items()}
            ergebnis["seitengroesse"] = len(roh)
            roh = _entpacken(roh, ergebnis["header"].get("content-encoding", "").lower())
            zeichensatz = "utf-8"
            ctype = ergebnis["header"].get("content-type", "")
            if "charset=" in ctype:
                zeichensatz = ctype.split("charset=")[-1].split(";")[0].strip() or "utf-8"
            ergebnis["html"] = roh.decode(zeichensatz, errors="replace")
            ergebnis["erreichbar"] = True
    except urllib.error.HTTPError as e:
        ergebnis["status_code"] = e.code
        ergebnis["endgueltige_url"] = url
        ergebnis["ladezeit_ms"] = int((time.perf_counter() - start) * 1000)
        ergebnis["fehler"] = f"HTTP {e.code}"
        # 4xx/5xx sind Befunde, keine Abbrüche - Inhalt trotzdem mitnehmen
        try:
            ergebnis["html"] = e.read(MAX_BYTES).decode("utf-8", errors="replace")
        except Exception:
            pass
    except ssl.SSLError as e:
        ergebnis["fehler"] = f"TLS-Fehler: {e}"
        ergebnis["tls_fehler"] = str(e)
    except (urllib.error.URLError, socket.timeout, ConnectionError) as e:
        grund = getattr(e, "reason", e)
        ergebnis["fehler"] = str(grund)
        if isinstance(grund, ssl.SSLError) or "certificate" in str(grund).lower():
            ergebnis["tls_fehler"] = str(grund)
    except Exception as e:  # defensiv: ein kaputter Server darf den Lauf nicht killen
        ergebnis["fehler"] = f"{type(e).__name__}: {e}"
    return ergebnis


def http_weiterleitung_pruefen(url: str) -> dict[str, Any]:
    """Prüft, ob die unverschlüsselte Variante auf HTTPS umleitet."""
    teile = urllib.parse.urlsplit(url_normalisieren(url))
    http_url = urllib.parse.urlunsplit(("http", teile.netloc, teile.path or "/", "", ""))
    ergebnis = seite_laden(http_url)
    ziel = ergebnis.get("endgueltige_url") or ""
    return {
        "erreichbar": ergebnis["erreichbar"],
        "leitet_auf_https": ziel.startswith("https://"),
        "ziel": ziel,
    }


# --------------------------------------------------------------------------
# Prüfungen
# --------------------------------------------------------------------------

IMPRESSUM_MUSTER = re.compile(r"impressum|imprint|anbieterkennzeichnung|legal-notice", re.I)
DATENSCHUTZ_MUSTER = re.compile(r"datenschutz|privacy|privacy-policy", re.I)
CONSENT_MUSTER = re.compile(
    r"cookiebot|usercentrics|borlabs|cookieconsent|klaro|consentmanager|"
    r"cookie-?banner|osano|complianz|iubenda|didomi|onetrust|cookieyes",
    re.I,
)
TRACKING_MUSTER = re.compile(
    r"google-analytics|googletagmanager|gtag/js|connect\.facebook\.net|fbevents|"
    r"hotjar|matomo|piwik|doubleclick|tiktok\.com/i18n|clarity\.ms|linkedin\.com/px",
    re.I,
)
KARTEN_MUSTER = re.compile(r"maps\.google|google\.com/maps|maps\.googleapis", re.I)
SCHRIFT_CDN_MUSTER = re.compile(r"fonts\.googleapis\.com|fonts\.gstatic\.com", re.I)
PLATZHALTER_TITEL = re.compile(
    r"^(startseite|home|start|willkommen|unbenannt|untitled|neue seite|index|"
    r"website|homepage|meine website|wordpress site|just another wordpress site)",
    re.I,
)
PARKING_MUSTER = re.compile(
    r"sedoparking|parkingcrew|bodis\.com|afternic|dan\.com/domain|"
    r"undeveloped\.com|this domain (?:is|name is) for sale|"
    r"diese domain (?:steht zum verkauf|kaufen)|domain parking|"
    r"gesponserte verbindungen|buy this domain",
    re.I,
)
# Hinweise auf gekaperte oder zweckentfremdete Domains. Bewusst eng gefasst:
# es braucht mehrere Treffer, sonst schlaegt es bei normalen Seiten an.
FREMDINHALT_MUSTER = re.compile(
    r"\b(gacor|situs|togel|judi|slot online|bonus harian|maxwin|rtp live|"
    r"cuan|casino online|taruhan|deposit pulsa)\b",
    re.I,
)

ALTE_TECHNIK = [
    (re.compile(r"jquery[.-]?1\.\d", re.I), "jQuery 1.x (Ende der Wartung 2016)"),
    (re.compile(r"jquery[.-]?2\.\d", re.I), "jQuery 2.x (nicht mehr gepflegt)"),
    (re.compile(r"\.swf\b", re.I), "Adobe Flash (seit 2020 abgeschaltet)"),
    (re.compile(r"bootstrap[.-]?3\.", re.I), "Bootstrap 3 (nicht mehr gepflegt)"),
    (re.compile(r"jquery-ui-1\.[0-9]\.", re.I), "veraltetes jQuery UI"),
]


def _absolut(basis: str, href: str) -> str:
    try:
        return urllib.parse.urljoin(basis, href)
    except Exception:
        return href


def _refresh_ziel(meta_refresh: str, basis: str) -> str | None:
    """Liest das Ziel aus einem <meta http-equiv="refresh"> aus."""
    treffer = re.search(r"url\s*=\s*[\"\']?([^\"\';]+)", meta_refresh or "", re.I)
    if not treffer:
        return None
    ziel = _absolut(basis, treffer.group(1).strip())
    return ziel if ziel.rstrip("/") != basis.rstrip("/") else None


def pruefen(
    url: str,
    lead: dict[str, Any] | None = None,
    http_check: bool = True,
) -> dict[str, Any]:
    """Führt das vollständige Audit für eine URL durch."""
    lead = lead or {}
    url = url_normalisieren(url)
    befunde: list[Befund] = []

    if not url:
        befunde.append(
            Befund(
                "keine_website",
                "Keine Website vorhanden",
                "Sichtbarkeit",
                "kritisch",
                40,
                "Zu diesem Betrieb ist keine eigene Website auffindbar.",
                "Ohne eigene Seite entsteht kein Vertrauen bei Neukunden, und "
                "die Sichtbarkeit hängt komplett an Portalen Dritter.",
                "Kompakte Website mit Leistungen, Kontakt, Öffnungszeiten und "
                "Rechtstexten aufsetzen.",
                aufwand_h=14,
            )
        )
        return _zusammenfassen(url, {"erreichbar": False}, befunde, None)

    seite = seite_laden(url)
    parser: SeitenParser | None = None

    # -- Erreichbarkeit ----------------------------------------------------
    if not seite["erreichbar"] and not seite["html"]:
        if seite.get("tls_fehler"):
            befunde.append(
                Befund(
                    "tls_kaputt",
                    "Verschlüsselung defekt",
                    "Technik",
                    "kritisch",
                    45,
                    f"Der TLS-Aufbau scheitert: {seite['tls_fehler'][:160]}",
                    "Browser zeigen eine ganzseitige Sicherheitswarnung. Praktisch "
                    "jeder Besucher bricht an dieser Stelle ab.",
                    "Zertifikat erneuern (Let's Encrypt, kostenfrei) und automatische "
                    "Verlängerung einrichten.",
                    aufwand_h=1.5,
                )
            )
        else:
            befunde.append(
                Befund(
                    "nicht_erreichbar",
                    "Website nicht erreichbar",
                    "Technik",
                    "kritisch",
                    45,
                    f"Die Seite antwortet nicht: {seite.get('fehler') or 'keine Antwort'}",
                    "Jede Anfrage über die Website geht verloren. Auch Google "
                    "stuft dauerhaft nicht erreichbare Seiten ab.",
                    "Hosting und DNS prüfen, Erreichbarkeitsüberwachung einrichten.",
                    aufwand_h=2,
                )
            )
        return _zusammenfassen(url, seite, befunde, None)

    if seite["status_code"] and seite["status_code"] >= 400:
        befunde.append(
            Befund(
                "fehlerstatus",
                f"Server antwortet mit Fehler {seite['status_code']}",
                "Technik",
                "kritisch",
                30,
                f"Der Aufruf der Startseite liefert HTTP {seite['status_code']}.",
                "Besucher und Suchmaschinen sehen eine Fehlerseite statt des Angebots.",
                "Ursache im Server-Log klären und die Startseite wiederherstellen.",
                aufwand_h=2,
            )
        )

    html = seite["html"]
    parser = SeitenParser()
    try:
        parser.feed(html)
    except Exception:
        pass

    # Meta-Refresh aufloesen: Viele aeltere Auftritte liefern unter der
    # bekannten Adresse nur eine Weiterleitungsseite. Ohne diesen Schritt
    # bewertet das Audit eine leere Huelle und meldet lauter Falschbefunde.
    weiterleitungen: list[str] = []
    for _ in range(2):
        ziel = _refresh_ziel(parser.meta.get("refresh", ""),
                             seite.get("endgueltige_url") or url)
        if not ziel:
            break
        folge = seite_laden(ziel)
        if not folge.get("html"):
            break
        weiterleitungen.append(ziel)
        seite = folge
        html = folge["html"]
        parser = SeitenParser()
        try:
            parser.feed(html)
        except Exception:
            pass

    text = parser.text.lower()
    endgueltig = seite.get("endgueltige_url") or url
    header = seite.get("header", {})

    if weiterleitungen:
        befunde.append(
            Befund(
                "meta_weiterleitung",
                "Umweg über eine Weiterleitungsseite",
                "Technik",
                "niedrig",
                4,
                "Die bekannte Adresse leitet erst über eine Zwischenseite auf "
                f"{weiterleitungen[-1]}.",
                "Jeder Aufruf verliert dadurch Zeit, und Suchmaschinen "
                "verteilen die Bewertung auf zwei Adressen.",
                "Weiterleitung serverseitig als 301 einrichten statt über die "
                "Zwischenseite.",
                aufwand_h=0.5,
            )
        )

    # Geparkte oder gekaperte Domain. Beides beendet die Pruefung: Liegt dort
    # nicht der Auftritt des Betriebs, sind alle weiteren Befunde Rauschen -
    # ein Bericht, der einer gekaperten Domain "Meta-Beschreibung fehlt"
    # vorhaelt, verfehlt das Thema.
    spam_treffer = len(FREMDINHALT_MUSTER.findall(html))
    if PARKING_MUSTER.search(html):
        befunde.append(
            Befund(
                "domain_geparkt",
                "Domain zeigt nur eine Platzhalterseite",
                "Vertrauen",
                "kritisch",
                50,
                "Unter der Adresse liegt eine Parkseite, kein Auftritt des Betriebs.",
                "Wer die Adresse aufruft, findet den Betrieb nicht. Auf "
                "Fahrzeugen, Drucksachen und in Empfehlungen läuft die "
                "Adresse damit ins Leere.",
                "Domain wieder mit einem eigenen Auftritt belegen.",
                aufwand_h=12,
            )
        )
        return _zusammenfassen(url, seite, befunde, parser)

    if spam_treffer >= 5:
        befunde.append(
            Befund(
                "fremdinhalte",
                "Unter der Domain liegen fremde Inhalte",
                "Vertrauen",
                "kritisch",
                55,
                "Die Seite zeigt in großem Umfang Inhalte, die nichts mit dem "
                "Betrieb zu tun haben. Das deutet auf einen fremden Zugriff auf "
                "das System oder eine übernommene Domain hin.",
                "Kunden, die die Adresse aufrufen, landen bei einem fremden "
                "Angebot. Das schadet dem Ruf unmittelbar, und Suchmaschinen "
                "stufen betroffene Domains regelmäßig als unsicher ein.",
                "Zugänge zu Hosting und Domain zurücksetzen, System bereinigen "
                "und den Auftritt anschließend neu aufsetzen. Vorher sichern.",
                aufwand_h=16,
            )
        )
        return _zusammenfassen(url, seite, befunde, parser)

    # -- HTTPS -------------------------------------------------------------
    if not endgueltig.startswith("https://"):
        befunde.append(
            Befund(
                "kein_https",
                "Keine Verschlüsselung (kein HTTPS)",
                "Technik",
                "kritisch",
                30,
                "Die Seite wird unverschlüsselt über HTTP ausgeliefert.",
                "Chrome und Firefox markieren die Seite als „Nicht sicher“. "
                "Bei Kontaktformularen ist die unverschlüsselte Übertragung "
                "personenbezogener Daten zusätzlich ein Datenschutzproblem.",
                "TLS-Zertifikat einrichten (Let's Encrypt, kostenfrei) und alle "
                "HTTP-Aufrufe dauerhaft auf HTTPS umleiten.",
                aufwand_h=2,
            )
        )
    elif http_check:
        wl = http_weiterleitung_pruefen(endgueltig)
        if wl["erreichbar"] and not wl["leitet_auf_https"]:
            befunde.append(
                Befund(
                    "keine_https_umleitung",
                    "HTTP leitet nicht auf HTTPS um",
                    "Technik",
                    "hoch",
                    12,
                    "Die Seite ist parallel unverschlüsselt erreichbar.",
                    "Besucher landen je nach Einstiegspunkt auf der unsicheren "
                    "Variante. Suchmaschinen werten das als doppelten Inhalt.",
                    "Dauerhafte Weiterleitung (301) von HTTP auf HTTPS einrichten.",
                    aufwand_h=0.5,
                )
            )

    if endgueltig.startswith("https://"):
        unsicher = re.findall(r'(?:src|href)=["\']http://[^"\']+', html, re.I)
        unsicher = [u for u in unsicher if "w3.org" not in u and "schema.org" not in u]
        if unsicher:
            befunde.append(
                Befund(
                    "mixed_content",
                    "Unsichere Inhalte auf verschlüsselter Seite",
                    "Technik",
                    "mittel",
                    8,
                    f"{len(unsicher)} Ressource(n) werden unverschlüsselt eingebunden.",
                    "Browser blockieren solche Inhalte teilweise. Die Seite wirkt "
                    "dann kaputt, ohne dass es dem Betreiber auffällt.",
                    "Alle eingebundenen Adressen auf HTTPS umstellen.",
                    aufwand_h=1,
                )
            )

    # -- Mobil -------------------------------------------------------------
    viewport = parser.meta.get("viewport", "")
    if not viewport:
        befunde.append(
            Befund(
                "kein_viewport",
                "Nicht für Mobilgeräte optimiert",
                "Technik",
                "kritisch",
                28,
                "Es fehlt die Viewport-Angabe, die für die Darstellung auf "
                "Smartphones notwendig ist.",
                "Auf dem Handy erscheint die Seite verkleinert und muss "
                "gezoomt werden. Google bewertet Seiten seit der Umstellung "
                "auf Mobile-First primär in der mobilen Ansicht.",
                "Responsives Layout umsetzen: Viewport setzen, Breakpoints und "
                "tastbare Bedienelemente ergänzen.",
                aufwand_h=10,
            )
        )
    elif "width=device-width" not in viewport.replace(" ", ""):
        befunde.append(
            Befund(
                "viewport_fest",
                "Feste Breite statt flexibler Darstellung",
                "Technik",
                "hoch",
                14,
                f"Viewport-Angabe: „{viewport[:80]}“",
                "Die Seite passt sich der Bildschirmbreite nicht an.",
                "Viewport auf width=device-width umstellen und Layout prüfen.",
                aufwand_h=5,
            )
        )
    if "user-scalable=no" in viewport.replace(" ", "").lower() or "maximum-scale=1" in viewport.replace(" ", "").lower():
        befunde.append(
            Befund(
                "zoom_gesperrt",
                "Zoom auf Mobilgeräten gesperrt",
                "Barrierefreiheit",
                "mittel",
                6,
                "Die Seite verhindert das Vergrößern per Fingergeste.",
                "Menschen mit eingeschränkter Sehkraft können die Inhalte nicht "
                "lesen. Das widerspricht anerkannten Barrierefreiheitskriterien.",
                "Zoom-Sperre entfernen.",
                aufwand_h=0.25,
            )
        )

    # -- Geschwindigkeit ---------------------------------------------------
    ms = seite.get("ladezeit_ms") or 0
    if ms > 4000:
        befunde.append(
            Befund(
                "sehr_langsam",
                "Sehr lange Ladezeit",
                "Technik",
                "kritisch",
                22,
                f"Die Startseite antwortet erst nach {ms/1000:.1f} Sekunden.",
                "Ein großer Teil der mobilen Besucher bricht vor dem ersten "
                "Bildinhalt ab. Ladezeit ist zugleich ein Rankingfaktor.",
                "Bilder komprimieren, Zwischenspeicher aktivieren, Hosting prüfen.",
                aufwand_h=5,
            )
        )
    elif ms > 2200:
        befunde.append(
            Befund(
                "langsam",
                "Ladezeit über dem Richtwert",
                "Technik",
                "mittel",
                10,
                f"Die Startseite antwortet nach {ms/1000:.1f} Sekunden.",
                "Als guter Richtwert gelten unter 2,5 Sekunden bis zum "
                "größten sichtbaren Inhalt.",
                "Bilder und Skripte optimieren, Zwischenspeicher aktivieren.",
                aufwand_h=3,
            )
        )

    groesse = seite.get("seitengroesse") or 0
    if groesse > 2_500_000:
        befunde.append(
            Befund(
                "sehr_gross",
                "Sehr große Startseite",
                "Technik",
                "hoch",
                12,
                f"Die Startseite überträgt allein {groesse/1_000_000:.1f} MB.",
                "Im Mobilfunknetz kostet das spürbar Zeit und Datenvolumen.",
                "Bilder auf WebP umstellen und in passender Größe ausliefern.",
                aufwand_h=3,
            )
        )

    if not header.get("content-encoding"):
        if groesse > 100_000:
            befunde.append(
                Befund(
                    "keine_komprimierung",
                    "Keine Komprimierung aktiv",
                    "Technik",
                    "niedrig",
                    5,
                    "Der Server liefert unkomprimiert aus.",
                    "Ohne Komprimierung werden unnötig viele Daten übertragen; "
                    "die Umstellung ist eine reine Servereinstellung.",
                    "gzip oder brotli auf dem Webserver aktivieren.",
                    aufwand_h=0.5,
                )
            )

    # -- Rechtliches -------------------------------------------------------
    link_blob = " ".join(f"{h} {t}" for h, t in parser.links)
    hat_impressum = bool(IMPRESSUM_MUSTER.search(link_blob)) or bool(
        IMPRESSUM_MUSTER.search(text)
    )
    hat_datenschutz = bool(DATENSCHUTZ_MUSTER.search(link_blob)) or bool(
        DATENSCHUTZ_MUSTER.search(text)
    )

    if not hat_impressum:
        befunde.append(
            Befund(
                "kein_impressum",
                "Kein Impressum auffindbar",
                "Recht",
                "kritisch",
                26,
                "Auf der Startseite ist kein Verweis auf ein Impressum zu finden.",
                "Geschäftsmäßige Websites brauchen nach § 5 DDG eine leicht "
                "erkennbare Anbieterkennzeichnung. Fehlt sie, drohen "
                "kostenpflichtige Abmahnungen durch Mitbewerber oder Verbände.",
                "Impressum anlegen und aus der Fußzeile jeder Seite verlinken.",
                aufwand_h=1.5,
            )
        )
    if not hat_datenschutz:
        befunde.append(
            Befund(
                "keine_datenschutzerklaerung",
                "Keine Datenschutzerklärung auffindbar",
                "Recht",
                "kritisch",
                24,
                "Ein Verweis auf eine Datenschutzerklärung ist nicht erkennbar.",
                "Art. 13 DSGVO verlangt die Information über die Datenverarbeitung "
                "bei Erhebung - bei einer Website also ab dem ersten Aufruf.",
                "Datenschutzerklärung passend zu den eingesetzten Diensten "
                "erstellen und in der Fußzeile verlinken.",
                aufwand_h=2,
            )
        )

    hat_consent = bool(CONSENT_MUSTER.search(html))
    tracker = sorted({m.group(0) for m in TRACKING_MUSTER.finditer(html)})
    if tracker and not hat_consent:
        befunde.append(
            Befund(
                "tracking_ohne_einwilligung",
                "Tracking ohne erkennbare Einwilligung",
                "Recht",
                "kritisch",
                22,
                "Erkannte Dienste: " + ", ".join(tracker[:4]),
                "§ 25 TDDDG verlangt für das Speichern und Auslesen von "
                "Informationen auf dem Endgerät eine vorherige Einwilligung, "
                "soweit sie nicht technisch erforderlich sind. Ein "
                "Einwilligungsbanner ist im Quelltext nicht erkennbar.",
                "Einwilligungslösung einbauen, Dienste erst nach Zustimmung "
                "laden und die Datenschutzerklärung angleichen.",
                aufwand_h=4,
            )
        )
    if SCHRIFT_CDN_MUSTER.search(html):
        befunde.append(
            Befund(
                "schriften_extern",
                "Schriftarten werden extern nachgeladen",
                "Recht",
                "mittel",
                9,
                "Google Fonts werden direkt vom Google-Server eingebunden.",
                "Dabei wird die IP-Adresse des Besuchers ohne Einwilligung an "
                "einen Drittanbieter übermittelt. Genau dazu gab es in den "
                "vergangenen Jahren eine Abmahnwelle.",
                "Schriften lokal einbinden - Aufwand rund eine Stunde.",
                aufwand_h=1,
            )
        )
    if KARTEN_MUSTER.search(html) and not hat_consent:
        befunde.append(
            Befund(
                "karte_ohne_einwilligung",
                "Karte ohne vorgeschaltete Einwilligung",
                "Recht",
                "mittel",
                7,
                "Eine Google-Karte wird ohne erkennbare Zustimmung geladen.",
                "Beim Laden fließen Verbindungsdaten an einen Drittanbieter.",
                "Karte erst nach Klick laden (Zwei-Klick-Lösung) oder auf einen "
                "datensparsamen Kartendienst wechseln.",
                aufwand_h=1.5,
            )
        )

    # -- Sichtbarkeit ------------------------------------------------------
    titel = parser.titel.strip()
    if not titel:
        befunde.append(
            Befund(
                "kein_titel",
                "Kein Seitentitel",
                "Sichtbarkeit",
                "hoch",
                16,
                "Die Seite hat keinen Titel.",
                "Der Titel ist die Überschrift im Suchergebnis. Ohne ihn "
                "erfindet Google einen Ersatz.",
                "Titel nach dem Muster „Leistung + Ort + Betrieb“ setzen.",
                aufwand_h=0.5,
            )
        )
    elif PLATZHALTER_TITEL.match(titel):
        befunde.append(
            Befund(
                "titel_platzhalter",
                "Nichtssagender Seitentitel",
                "Sichtbarkeit",
                "hoch",
                14,
                f"Aktueller Titel: „{titel[:70]}“",
                "Ein Platzhaltertitel verschenkt den wichtigsten Text im "
                "Suchergebnis - und damit Klicks von Suchenden aus der Region.",
                "Titel mit Leistung und Ort formulieren, z. B. "
                "„Dachdecker in Musterstadt - Betrieb Mustermann“.",
                aufwand_h=0.5,
            )
        )
    elif len(titel) < 25:
        befunde.append(
            Befund(
                "titel_kurz",
                "Seitentitel zu knapp",
                "Sichtbarkeit",
                "mittel",
                8,
                f"Titel mit {len(titel)} Zeichen: „{titel}“",
                "Der verfügbare Platz im Suchergebnis wird nicht genutzt.",
                "Titel auf 50-60 Zeichen mit Leistung und Ort erweitern.",
                aufwand_h=0.5,
            )
        )
    elif len(titel) > 70:
        befunde.append(
            Befund(
                "titel_lang",
                "Seitentitel wird abgeschnitten",
                "Sichtbarkeit",
                "niedrig",
                4,
                f"Titel mit {len(titel)} Zeichen.",
                "Google kürzt die Anzeige, das Wichtige fällt hinten weg.",
                "Titel auf rund 60 Zeichen straffen.",
                aufwand_h=0.25,
            )
        )

    if titel and lead.get("ort") and lead["ort"].lower() not in titel.lower():
        befunde.append(
            Befund(
                "ort_fehlt_im_titel",
                "Ort fehlt im Seitentitel",
                "Sichtbarkeit",
                "mittel",
                9,
                f"„{lead['ort']}“ kommt im Titel nicht vor.",
                "Lokale Suchanfragen enthalten fast immer einen Ortsbezug. "
                "Ohne Ort im Titel fehlt das wichtigste Signal für die Region.",
                "Ort in Titel und Hauptüberschrift aufnehmen.",
                aufwand_h=0.5,
            )
        )

    beschreibung = parser.meta.get("description", "").strip()
    if not beschreibung:
        befunde.append(
            Befund(
                "keine_beschreibung",
                "Keine Meta-Beschreibung",
                "Sichtbarkeit",
                "mittel",
                9,
                "Es ist kein Beschreibungstext für das Suchergebnis hinterlegt.",
                "Der Beschreibungstext ist die Werbefläche im Suchergebnis und "
                "beeinflusst, wie viele Suchende tatsächlich klicken.",
                "Beschreibung mit 140-160 Zeichen inklusive Leistung, Ort und "
                "Handlungsaufforderung schreiben.",
                aufwand_h=0.5,
            )
        )
    elif len(beschreibung) < 70:
        befunde.append(
            Befund(
                "beschreibung_kurz",
                "Meta-Beschreibung zu kurz",
                "Sichtbarkeit",
                "niedrig",
                4,
                f"Beschreibung mit {len(beschreibung)} Zeichen.",
                "Der Platz im Suchergebnis bleibt ungenutzt.",
                "Beschreibung auf 140-160 Zeichen ausbauen.",
                aufwand_h=0.25,
            )
        )

    if not parser.h1:
        befunde.append(
            Befund(
                "keine_h1",
                "Keine Hauptüberschrift",
                "Sichtbarkeit",
                "mittel",
                8,
                "Auf der Startseite fehlt eine H1-Überschrift.",
                "Die Hauptüberschrift ordnet den Inhalt für Suchmaschinen und "
                "für Screenreader ein.",
                "Eine aussagekräftige H1 mit Leistung und Ort ergänzen.",
                aufwand_h=0.5,
            )
        )
    elif len(parser.h1) > 3:
        befunde.append(
            Befund(
                "viele_h1",
                "Überschriftenstruktur unklar",
                "Sichtbarkeit",
                "niedrig",
                3,
                f"{len(parser.h1)} H1-Überschriften auf einer Seite.",
                "Die Gewichtung des Inhalts wird dadurch unscharf.",
                "Auf eine H1 reduzieren, den Rest als H2/H3 gliedern.",
                aufwand_h=0.5,
            )
        )

    hat_localbusiness = any(
        re.search(r"localbusiness|organization|@type", j, re.I) for j in parser.jsonld
    )
    if not hat_localbusiness:
        befunde.append(
            Befund(
                "kein_markup",
                "Kein strukturiertes Markup",
                "Sichtbarkeit",
                "mittel",
                10,
                "Es sind keine maschinenlesbaren Angaben zum Betrieb hinterlegt.",
                "Mit LocalBusiness-Markup können Adresse, Öffnungszeiten und "
                "Bewertungen direkt im Suchergebnis erscheinen. Das macht den "
                "Eintrag größer und klickstärker als den der Mitbewerber.",
                "LocalBusiness-Markup mit Adresse, Telefon und Öffnungszeiten "
                "ergänzen.",
                aufwand_h=1.5,
            )
        )

    if not parser.html_lang:
        befunde.append(
            Befund(
                "keine_sprache",
                "Sprache nicht ausgezeichnet",
                "Barrierefreiheit",
                "niedrig",
                3,
                "Im HTML fehlt die Sprachangabe.",
                "Vorleseprogramme wählen ohne diese Angabe die falsche "
                "Aussprache.",
                "lang=\"de\" im HTML-Tag ergänzen.",
                aufwand_h=0.1,
            )
        )

    # -- Vertrauen ---------------------------------------------------------
    if not parser.hat_favicon:
        befunde.append(
            Befund(
                "kein_favicon",
                "Kein Symbol im Browsertab",
                "Vertrauen",
                "niedrig",
                3,
                "Es ist kein Favicon hinterlegt.",
                "In der Tableiste und in den Lesezeichen bleibt der Betrieb "
                "namenlos - ein kleines, aber sichtbares Detail.",
                "Favicon aus dem Logo erzeugen und einbinden.",
                aufwand_h=0.5,
            )
        )

    hat_tel_link = any(h.lower().startswith("tel:") for h, _ in parser.links)
    telefon_im_text = re.search(r"\b0[\d\s/().-]{7,}\b", parser.text)
    if not hat_tel_link and not telefon_im_text:
        befunde.append(
            Befund(
                "keine_telefonnummer",
                "Keine Telefonnummer auf der Startseite",
                "Vertrauen",
                "hoch",
                14,
                "Auf der Startseite ist keine Rufnummer erkennbar.",
                "Bei lokalen Dienstleistern ist der Anruf der häufigste Weg zur "
                "Anfrage. Wer die Nummer suchen muss, ruft oft beim nächsten "
                "Treffer an.",
                "Rufnummer im Kopfbereich anzeigen und als Anruf-Link hinterlegen.",
                aufwand_h=0.5,
            )
        )
    elif not hat_tel_link and telefon_im_text:
        befunde.append(
            Befund(
                "telefon_nicht_klickbar",
                "Telefonnummer nicht anklickbar",
                "Vertrauen",
                "mittel",
                7,
                "Die Rufnummer steht als Text ohne Anruf-Link.",
                "Auf dem Smartphone kostet das den Besucher zusätzliche "
                "Schritte - und den Betrieb Anrufe.",
                "Rufnummer als tel:-Link auszeichnen.",
                aufwand_h=0.25,
            )
        )

    if parser.formulare == 0 and not re.search(r"mailto:", link_blob, re.I):
        befunde.append(
            Befund(
                "kein_kontaktweg",
                "Kein digitaler Kontaktweg",
                "Vertrauen",
                "mittel",
                9,
                "Weder Formular noch E-Mail-Adresse sind auf der Startseite "
                "erkennbar.",
                "Anfragen außerhalb der Geschäftszeiten gehen verloren.",
                "Schlankes Kontaktformular mit Datenschutzhinweis ergänzen.",
                aufwand_h=2,
            )
        )

    jahr_treffer = re.findall(r"(?:©|&copy;|copyright)\s*(?:\d{4}\s*[-–]\s*)?(\d{4})", html, re.I)
    if jahr_treffer:
        neuestes = max(int(j) for j in jahr_treffer)
        alter = date.today().year - neuestes
        if alter >= 2:
            befunde.append(
                Befund(
                    "verwaist",
                    "Seite wirkt ungepflegt",
                    "Vertrauen",
                    "mittel",
                    9,
                    f"Die Fußzeile nennt als Jahr noch {neuestes}.",
                    "Besucher schließen daraus, dass der Betrieb die Seite - und "
                    "womöglich auch Anfragen darüber - nicht mehr verfolgt.",
                    "Inhalte auffrischen und die Jahresangabe automatisch setzen.",
                    aufwand_h=1,
                )
            )

    for muster, bezeichnung in ALTE_TECHNIK:
        if muster.search(html):
            befunde.append(
                Befund(
                    "alte_technik",
                    "Veraltete Technik im Einsatz",
                    "Technik",
                    "mittel",
                    8,
                    f"Erkannt: {bezeichnung}.",
                    "Nicht mehr gepflegte Bausteine erhalten keine "
                    "Sicherheitsaktualisierungen mehr.",
                    "Betroffene Bausteine auf aktuelle Versionen heben.",
                    aufwand_h=3,
                )
            )
            break

    if parser.frames:
        befunde.append(
            Befund(
                "frames",
                "Seitenaufbau mit Frames",
                "Technik",
                "hoch",
                12,
                "Die Seite arbeitet mit Framesets.",
                "Diese Bauweise stammt aus den 1990er-Jahren, ist auf "
                "Mobilgeräten unbrauchbar und für Suchmaschinen problematisch.",
                "Seite auf eine zeitgemäße Struktur umbauen.",
                aufwand_h=12,
            )
        )

    # -- Barrierefreiheit --------------------------------------------------
    ohne_alt = [b for b in parser.bilder if b["alt"] == "__FEHLT__"]
    if parser.bilder and len(ohne_alt) >= max(2, len(parser.bilder) // 3):
        befunde.append(
            Befund(
                "bilder_ohne_alt",
                "Bilder ohne Alternativtext",
                "Barrierefreiheit",
                "mittel",
                10,
                f"{len(ohne_alt)} von {len(parser.bilder)} Bildern haben keinen "
                "Alternativtext.",
                "Vorleseprogramme können die Bilder nicht beschreiben. "
                "Seit dem 28.06.2025 gelten über das Barrierefreiheits"
                "stärkungsgesetz für viele Dienstleistungen im elektronischen "
                "Geschäftsverkehr verbindliche Anforderungen - ob der Betrieb "
                "unter die Kleinstunternehmer-Ausnahme fällt, gehört geprüft.",
                "Alternativtexte ergänzen und Kontraste sowie Tastaturbedienung "
                "nachziehen.",
                aufwand_h=3,
            )
        )

    if parser.eingabefelder > 0 and parser.labels == 0:
        befunde.append(
            Befund(
                "formular_ohne_label",
                "Formularfelder ohne Beschriftung",
                "Barrierefreiheit",
                "mittel",
                6,
                f"{parser.eingabefelder} Eingabefeld(er) ohne zugehöriges Label.",
                "Vorleseprogramme können die Felder nicht zuordnen; das Formular "
                "ist für blinde Nutzer praktisch nicht bedienbar.",
                "Jedem Feld ein verknüpftes Label geben.",
                aufwand_h=1,
            )
        )

    return _zusammenfassen(url, seite, befunde, parser)


def _zusammenfassen(
    url: str,
    seite: dict[str, Any],
    befunde: list[Befund],
    parser: SeitenParser | None,
) -> dict[str, Any]:
    reihenfolge = {"kritisch": 0, "hoch": 1, "mittel": 2, "niedrig": 3}
    befunde.sort(key=lambda b: (reihenfolge[b.schwere], -b.punkte))

    roh_score = sum(b.punkte * SCHWERE_GEWICHT[b.schwere] for b in befunde)
    score = int(min(100, round(roh_score)))
    aufwand = round(sum(b.aufwand_h for b in befunde), 1)

    return {
        "url": url,
        "erreichbar": seite.get("erreichbar", False),
        "status_code": seite.get("status_code"),
        "endgueltige_url": seite.get("endgueltige_url"),
        "ladezeit_ms": seite.get("ladezeit_ms"),
        "seitengroesse": seite.get("seitengroesse"),
        "fehler": seite.get("fehler"),
        "schmerz_score": score,
        "aufwand_h": aufwand,
        "befunde": [b.as_dict() for b in befunde],
        "rohdaten": {
            "titel": parser.titel.strip() if parser else "",
            "beschreibung": parser.meta.get("description", "") if parser else "",
            "h1": parser.h1[:3] if parser else [],
            "generator": parser.generator if parser else "",
            "anzahl_bilder": len(parser.bilder) if parser else 0,
            "anzahl_skripte": len(parser.skripte) if parser else 0,
            "server": (seite.get("header") or {}).get("server", ""),
        },
    }
