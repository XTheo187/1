"""Absenderdaten und Voreinstellungen, gespeichert als JSON neben der Datenbank."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

DEFAULT_PFAD = Path("standortcheck.json")

VORGABE: dict[str, Any] = {
    "absender": {
        "name": "",
        "strasse": "",
        "ort": "",
        "telefon": "",
        "email": "",
    },
    "stundensatz": 75.0,
    "startkapital": 500.0,
    "stunden_pro_woche": 20.0,
}


def laden(pfad: Path | str = DEFAULT_PFAD) -> dict[str, Any]:
    p = Path(pfad)
    if not p.exists():
        return json.loads(json.dumps(VORGABE))
    daten = json.loads(p.read_text(encoding="utf-8"))
    zusammen = json.loads(json.dumps(VORGABE))
    zusammen.update(daten)
    zusammen["absender"] = {**VORGABE["absender"], **daten.get("absender", {})}
    return zusammen


def speichern(daten: dict[str, Any], pfad: Path | str = DEFAULT_PFAD) -> Path:
    p = Path(pfad)
    p.write_text(json.dumps(daten, indent=2, ensure_ascii=False), encoding="utf-8")
    return p


def absender_vollstaendig(daten: dict[str, Any]) -> bool:
    a = daten.get("absender", {})
    return all(a.get(f) for f in ("name", "strasse", "ort", "telefon", "email"))
