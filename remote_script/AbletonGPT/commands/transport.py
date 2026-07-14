"""Transport command handlers for the Remote Script package."""

from __future__ import annotations

import logging
from typing import Any, Final

from ..live_adapter import LiveAdapter

logger: Final[logging.Logger] = logging.getLogger(__name__)


class TransportCommands:
    """Command handlers that delegate transport actions to a LiveAdapter."""

    def __init__(self, adapter: LiveAdapter) -> None:
        self._adapter = adapter
        self._logger = logger

    def play(self, payload: dict[str, Any] | None = None) -> dict[str, Any]:
        self._logger.info("TransportCommands: entering play()")
        self._adapter.song().play()
        self._logger.info("TransportCommands: leaving play()")
        return {"status": "not_implemented", "command": "play"}

    def stop(self, payload: dict[str, Any] | None = None) -> dict[str, Any]:
        self._logger.info("TransportCommands: entering stop()")
        self._adapter.song().stop()
        self._logger.info("TransportCommands: leaving stop()")
        return {"status": "not_implemented", "command": "stop"}

    def get_tempo(self, payload: dict[str, Any] | None = None) -> dict[str, Any]:
        self._logger.info("TransportCommands: entering get_tempo()")
        tempo = self._adapter.song().get_tempo()
        self._logger.info("TransportCommands: leaving get_tempo()")
        return {"status": "not_implemented", "command": "get_tempo", "tempo": tempo}

    def set_tempo(self, payload: dict[str, Any] | None = None) -> dict[str, Any]:
        self._logger.info("TransportCommands: entering set_tempo()")
        bpm = int(payload.get("bpm", 0)) if payload else 0
        self._adapter.song().set_tempo(bpm)
        self._logger.info("TransportCommands: leaving set_tempo()")
        return {"status": "not_implemented", "command": "set_tempo", "tempo": bpm}
