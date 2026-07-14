"""Live API adapter abstractions for the Remote Script package."""

from __future__ import annotations

from typing import Any

from .ableton_song_adapter import AbletonSongAdapter
from .song_adapter import SongAdapter


class LiveAdapter:
    """Abstract adapter for interacting with the Ableton Live API."""

    def __init__(self, control_surface: Any | None = None) -> None:
        self._control_surface = control_surface

    def song(self) -> SongAdapter:
        if self._control_surface is None:
            raise NotImplementedError("song() is not implemented")
        return AbletonSongAdapter(self._control_surface)

    def play(self) -> None:
        self.song().play()

    def stop(self) -> None:
        self.song().stop()

    def get_tempo(self) -> int:
        return self.song().get_tempo()

    def set_tempo(self, bpm: int) -> None:
        self.song().set_tempo(bpm)


class MockLiveAdapter(LiveAdapter):
    """Simple in-memory adapter used by unit tests."""

    def __init__(self) -> None:
        self.tempo = 120
        self.playing = False
        self._song = MockSongAdapter(self)

    def song(self) -> SongAdapter:
        return self._song


class MockSongAdapter(SongAdapter):
    """Simple in-memory song adapter used by unit tests."""

    def __init__(self, owner: MockLiveAdapter) -> None:
        self._owner = owner

    def play(self) -> None:
        self._owner.playing = True

    def stop(self) -> None:
        self._owner.playing = False

    def get_tempo(self) -> int:
        return self._owner.tempo

    def set_tempo(self, bpm: int) -> None:
        self._owner.tempo = bpm
