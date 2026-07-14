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

    def _get_song(self) -> Any:
        song = getattr(self._control_surface, "song", None)

        if song is None:
            raise RuntimeError("Ableton song object is unavailable")

        return song

    def play(self) -> None:
        """Start Ableton playback."""
        logger.info("AbletonSongAdapter: entering play()")

        song = self._get_song()

        try:
            song.start_playing()
            logger.info("AbletonSongAdapter: playback started")
        except Exception:
            logger.exception("AbletonSongAdapter: play() failed")
            raise

    def stop(self) -> None:
        """Stop Ableton playback."""
        logger.info("AbletonSongAdapter: entering stop()")

        song = self._get_song()

        try:
            song.stop_playing()
            logger.info("AbletonSongAdapter: playback stopped")
        except Exception:
            logger.exception("AbletonSongAdapter: stop() failed")
            raise

    def get_tempo(self) -> int:
        """Return current Ableton tempo."""
        song = self._get_song()

        return int(song.tempo)

    def set_tempo(self, bpm: int) -> None:
        """Set Ableton tempo."""
        song = self._get_song()

        song.tempo = bpm