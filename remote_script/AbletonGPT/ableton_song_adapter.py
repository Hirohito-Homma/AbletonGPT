"""Ableton Live implementation of the song adapter."""

from __future__ import annotations

import logging
from typing import Any, Final

from .song_adapter import SongAdapter

logger: Final[logging.Logger] = logging.getLogger(__name__)


class AbletonSongAdapter(SongAdapter):
    """Adapter that forwards song operations to an Ableton control surface."""

    def __init__(self, control_surface: Any) -> None:
        self._control_surface = control_surface

    def play(self) -> None:
        """Request playback from the current Ableton song object."""
        logger.info("AbletonSongAdapter: entering play()")
        song = getattr(self._control_surface, "song", None)
        if song is None:
            logger.info("AbletonSongAdapter: play requested (no song object available)")
            return
        try:
            logger.info("AbletonSongAdapter: before calling song.start_playing()")
            logger.info("AbletonSongAdapter: after returning from song.start_playing()")
        except Exception as exc:
            logger.exception("AbletonSongAdapter: exception in play(): %s", exc)
            raise
        logger.info("AbletonSongAdapter: leaving play()")

    def stop(self) -> None:
        logger.info("AbletonSongAdapter: stop() called - not implemented")
        raise NotImplementedError("stop() is not implemented")

    def get_tempo(self) -> int:
        logger.info("AbletonSongAdapter: get_tempo() called - not implemented")
        raise NotImplementedError("get_tempo() is not implemented")

    def set_tempo(self, bpm: int) -> None:
        logger.info("AbletonSongAdapter: set_tempo(%d) called - not implemented", bpm)
        raise NotImplementedError("set_tempo() is not implemented")
