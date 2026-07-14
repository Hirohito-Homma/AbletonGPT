"""Utility helpers for AbletonGPT."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def save_json(path: str | Path, data: Any) -> None:
    path_obj = Path(path)
    path_obj.parent.mkdir(parents=True, exist_ok=True)
    with path_obj.open("w", encoding="utf-8") as handle:
        json.dump(data, handle, indent=2)
