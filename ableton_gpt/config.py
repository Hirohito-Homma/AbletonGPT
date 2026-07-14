"""Configuration helpers for AbletonGPT."""

from __future__ import annotations

from pathlib import Path
from typing import Any


def load_config(path: str | Path) -> dict[str, Any]:
    config_path = Path(path)
    if not config_path.exists():
        return {}

    with config_path.open("r", encoding="utf-8") as handle:
        return {"path": str(config_path), "content": handle.read()}
