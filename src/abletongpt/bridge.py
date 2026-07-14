"""Bridge abstractions for connecting the MCP layer to Ableton transport implementations."""

from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from typing import Protocol

logger = logging.getLogger(__name__)


class AbletonBridge(ABC):
    """Abstract interface for Ableton transport implementations."""

    def __init__(self) -> None:
        self._logger = logger

    @abstractmethod
    def connect(self) -> None:
        """Establish a connection to the underlying Ableton transport."""

    @abstractmethod
    def disconnect(self) -> None:
        """Disconnect from the underlying Ableton transport."""

    @abstractmethod
    def is_connected(self) -> bool:
        """Return whether the bridge currently has an active connection."""

    def play(self) -> None:
        """Start playback through the transport implementation."""
        self._logger.warning("NotImplementedError: play() is not implemented for %s", self.__class__.__name__)
        raise NotImplementedError("play() is not implemented")

    def stop(self) -> None:
        """Stop playback through the transport implementation."""
        self._logger.warning("NotImplementedError: stop() is not implemented for %s", self.__class__.__name__)
        raise NotImplementedError("stop() is not implemented")

    def get_tempo(self) -> int:
        """Read the current tempo from the transport implementation."""
        self._logger.warning("NotImplementedError: get_tempo() is not implemented for %s", self.__class__.__name__)
        raise NotImplementedError("get_tempo() is not implemented")

    def set_tempo(self, bpm: int) -> None:
        """Set the current tempo on the transport implementation."""
        self._logger.warning("NotImplementedError: set_tempo() is not implemented for %s", self.__class__.__name__)
        raise NotImplementedError("set_tempo() is not implemented")
