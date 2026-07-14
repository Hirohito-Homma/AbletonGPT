"""Song adapter abstraction for Ableton Live song-level operations."""

from __future__ import annotations


class SongAdapter:
    """Abstract adapter for interacting with Ableton Live's song object."""

    def play(self) -> None:
        raise NotImplementedError("play() is not implemented")

    def stop(self) -> None:
        raise NotImplementedError("stop() is not implemented")

    def get_tempo(self) -> int:
        raise NotImplementedError("get_tempo() is not implemented")

    def set_tempo(self, bpm: int) -> None:
        raise NotImplementedError("set_tempo() is not implemented")
