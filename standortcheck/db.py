"""SQLite-Persistenz für Leads, Audits und Pipeline.

Bewusst nur Standardbibliothek: keine Lizenz-, Hosting- oder Abokosten,
läuft auf jedem Rechner mit Python 3.9+.
"""

from __future__ import annotations

import json
import sqlite3
from contextlib import contextmanager
from datetime import date, datetime
from pathlib import Path
from typing import Any, Iterable, Iterator

DEFAULT_DB = Path("standortcheck.db")

# Pipeline-Stufen in Verkaufsreihenfolge. Der Index ist die Fortschrittsstufe.
STAGES = [
    "neu",  # entdeckt, noch nichts passiert
    "geprueft",  # Audit liegt vor
    "kontaktiert",  # Erstansprache raus
    "gespraech",  # Termin/Telefonat gelaufen
    "angebot",  # Angebot verschickt
    "gewonnen",  # Auftrag erteilt
    "verloren",  # abgesagt oder aussortiert
]

SCHEMA = """
CREATE TABLE IF NOT EXISTS leads (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    name            TEXT    NOT NULL,
    branche         TEXT,
    ort             TEXT,
    plz             TEXT,
    strasse         TEXT,
    telefon         TEXT,
    email           TEXT,
    website         TEXT,
    quelle          TEXT,
    quelle_id       TEXT,
    lat             REAL,
    lon             REAL,
    stage           TEXT    NOT NULL DEFAULT 'neu',
    deal_wert       REAL,
    umsatz          REAL    NOT NULL DEFAULT 0,
    naechster_schritt TEXT,
    faellig_am      TEXT,
    notiz           TEXT,
    angelegt_am     TEXT    NOT NULL,
    geaendert_am    TEXT    NOT NULL,
    UNIQUE (quelle, quelle_id)
);

CREATE TABLE IF NOT EXISTS audits (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    lead_id         INTEGER NOT NULL REFERENCES leads(id) ON DELETE CASCADE,
    geprueft_am     TEXT    NOT NULL,
    erreichbar      INTEGER NOT NULL DEFAULT 0,
    endgueltige_url TEXT,
    ladezeit_ms     INTEGER,
    seitengroesse   INTEGER,
    status_code     INTEGER,
    schmerz_score   INTEGER NOT NULL DEFAULT 0,
    befunde_json    TEXT    NOT NULL DEFAULT '[]',
    rohdaten_json   TEXT    NOT NULL DEFAULT '{}'
);

CREATE TABLE IF NOT EXISTS aktivitaeten (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    lead_id     INTEGER REFERENCES leads(id) ON DELETE CASCADE,
    am          TEXT NOT NULL,
    art         TEXT NOT NULL,
    minuten     INTEGER NOT NULL DEFAULT 0,
    notiz       TEXT
);

CREATE TABLE IF NOT EXISTS ausgaben (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    am          TEXT NOT NULL,
    posten      TEXT NOT NULL,
    betrag      REAL NOT NULL,
    kategorie   TEXT
);

CREATE INDEX IF NOT EXISTS idx_audits_lead ON audits(lead_id);
CREATE INDEX IF NOT EXISTS idx_leads_stage ON leads(stage);
CREATE INDEX IF NOT EXISTS idx_akt_lead ON aktivitaeten(lead_id);
"""


def jetzt() -> str:
    return datetime.now().isoformat(timespec="seconds")


def heute() -> str:
    return date.today().isoformat()


def connect(pfad: Path | str = DEFAULT_DB) -> sqlite3.Connection:
    con = sqlite3.connect(str(pfad))
    con.row_factory = sqlite3.Row
    con.execute("PRAGMA foreign_keys = ON")
    con.executescript(SCHEMA)
    return con


@contextmanager
def session(pfad: Path | str = DEFAULT_DB) -> Iterator[sqlite3.Connection]:
    con = connect(pfad)
    try:
        yield con
        con.commit()
    finally:
        con.close()


# --------------------------------------------------------------------------
# Leads
# --------------------------------------------------------------------------


def lead_speichern(con: sqlite3.Connection, daten: dict[str, Any]) -> tuple[int, bool]:
    """Legt einen Lead an oder ergänzt einen vorhandenen.

    Gibt ``(lead_id, neu_angelegt)`` zurück. Bereits gepflegte Felder werden
    nicht überschrieben - manuelle Recherche schlägt Automatik.
    """
    felder = (
        "name branche ort plz strasse telefon email website "
        "quelle quelle_id lat lon"
    ).split()
    werte = {f: daten.get(f) for f in felder}

    vorhanden = None
    if werte["quelle"] and werte["quelle_id"]:
        vorhanden = con.execute(
            "SELECT * FROM leads WHERE quelle = ? AND quelle_id = ?",
            (werte["quelle"], werte["quelle_id"]),
        ).fetchone()
    if vorhanden is None:
        vorhanden = con.execute(
            "SELECT * FROM leads WHERE lower(name) = lower(?) AND ifnull(ort,'') = ifnull(?,'')",
            (werte["name"], werte["ort"]),
        ).fetchone()

    if vorhanden is not None:
        nachtrag = {
            k: v for k, v in werte.items() if v and not vorhanden[k] and k != "name"
        }
        if nachtrag:
            setzt = ", ".join(f"{k} = ?" for k in nachtrag)
            con.execute(
                f"UPDATE leads SET {setzt}, geaendert_am = ? WHERE id = ?",
                (*nachtrag.values(), jetzt(), vorhanden["id"]),
            )
        return int(vorhanden["id"]), False

    spalten = ", ".join(felder) + ", angelegt_am, geaendert_am"
    platzhalter = ", ".join("?" * (len(felder) + 2))
    cur = con.execute(
        f"INSERT INTO leads ({spalten}) VALUES ({platzhalter})",
        (*werte.values(), jetzt(), jetzt()),
    )
    return int(cur.lastrowid), True


def lead_holen(con: sqlite3.Connection, lead_id: int) -> sqlite3.Row | None:
    return con.execute("SELECT * FROM leads WHERE id = ?", (lead_id,)).fetchone()


def leads_holen(
    con: sqlite3.Connection,
    stage: str | None = None,
    ort: str | None = None,
    nur_mit_website: bool = False,
    ungeprueft: bool = False,
    limit: int | None = None,
) -> list[sqlite3.Row]:
    sql = "SELECT * FROM leads WHERE 1=1"
    args: list[Any] = []
    if stage:
        sql += " AND stage = ?"
        args.append(stage)
    if ort:
        sql += " AND lower(ort) = lower(?)"
        args.append(ort)
    if nur_mit_website:
        sql += " AND website IS NOT NULL AND website != ''"
    if ungeprueft:
        sql += " AND id NOT IN (SELECT lead_id FROM audits)"
    sql += " ORDER BY id"
    if limit:
        sql += f" LIMIT {int(limit)}"
    return list(con.execute(sql, args).fetchall())


def lead_aktualisieren(con: sqlite3.Connection, lead_id: int, **felder: Any) -> None:
    erlaubt = {
        "stage",
        "deal_wert",
        "umsatz",
        "naechster_schritt",
        "faellig_am",
        "notiz",
        "telefon",
        "email",
        "website",
        "branche",
    }
    setzbar = {k: v for k, v in felder.items() if k in erlaubt}
    if not setzbar:
        return
    setzt = ", ".join(f"{k} = ?" for k in setzbar)
    con.execute(
        f"UPDATE leads SET {setzt}, geaendert_am = ? WHERE id = ?",
        (*setzbar.values(), jetzt(), lead_id),
    )


# --------------------------------------------------------------------------
# Audits
# --------------------------------------------------------------------------


def audit_speichern(con: sqlite3.Connection, lead_id: int, ergebnis: dict[str, Any]) -> int:
    cur = con.execute(
        """INSERT INTO audits
           (lead_id, geprueft_am, erreichbar, endgueltige_url, ladezeit_ms,
            seitengroesse, status_code, schmerz_score, befunde_json, rohdaten_json)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (
            lead_id,
            jetzt(),
            int(bool(ergebnis.get("erreichbar"))),
            ergebnis.get("endgueltige_url"),
            ergebnis.get("ladezeit_ms"),
            ergebnis.get("seitengroesse"),
            ergebnis.get("status_code"),
            int(ergebnis.get("schmerz_score", 0)),
            json.dumps(ergebnis.get("befunde", []), ensure_ascii=False),
            json.dumps(ergebnis.get("rohdaten", {}), ensure_ascii=False),
        ),
    )
    return int(cur.lastrowid)


def letztes_audit(con: sqlite3.Connection, lead_id: int) -> dict[str, Any] | None:
    row = con.execute(
        "SELECT * FROM audits WHERE lead_id = ? ORDER BY geprueft_am DESC, id DESC LIMIT 1",
        (lead_id,),
    ).fetchone()
    if row is None:
        return None
    d = dict(row)
    d["befunde"] = json.loads(d.pop("befunde_json") or "[]")
    d["rohdaten"] = json.loads(d.pop("rohdaten_json") or "{}")
    # Aus den Befunden ableiten, damit gespeicherte und frisch berechnete
    # Audits identisch bewertet werden.
    d["aufwand_h"] = round(sum(b.get("aufwand_h", 0) for b in d["befunde"]), 1)
    return d


# --------------------------------------------------------------------------
# Aktivitäten und Ausgaben
# --------------------------------------------------------------------------


def aktivitaet_buchen(
    con: sqlite3.Connection,
    art: str,
    minuten: int = 0,
    lead_id: int | None = None,
    notiz: str | None = None,
    am: str | None = None,
) -> int:
    cur = con.execute(
        "INSERT INTO aktivitaeten (lead_id, am, art, minuten, notiz) VALUES (?, ?, ?, ?, ?)",
        (lead_id, am or heute(), art, int(minuten), notiz),
    )
    return int(cur.lastrowid)


def ausgabe_buchen(
    con: sqlite3.Connection,
    posten: str,
    betrag: float,
    kategorie: str | None = None,
    am: str | None = None,
) -> int:
    cur = con.execute(
        "INSERT INTO ausgaben (am, posten, betrag, kategorie) VALUES (?, ?, ?, ?)",
        (am or heute(), posten, float(betrag), kategorie),
    )
    return int(cur.lastrowid)


def summe(con: sqlite3.Connection, sql: str, args: Iterable[Any] = ()) -> float:
    wert = con.execute(sql, tuple(args)).fetchone()[0]
    return float(wert or 0)
