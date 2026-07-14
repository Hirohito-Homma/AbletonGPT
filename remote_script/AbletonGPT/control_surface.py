"""Placeholder control surface for the Ableton Remote Script package."""

from __future__ import annotations

import logging
from typing import Any, Final

logger: Final[logging.Logger] = logging.getLogger(__name__)


class ControlSurfacePlaceholder:
    """Fallback placeholder when Live's ControlSurface is unavailable."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        self._logger = logger


try:
    from ableton.v2.control_surface import ControlSurface  # type: ignore
except ImportError:  # pragma: no cover - environment dependent
    ControlSurface = ControlSurfacePlaceholder  # type: ignore[misc,assignment]


class AbletonGPTControlSurface(ControlSurface):
    """Minimal control surface that wires up socket handling and command dispatch."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self._logger = logger
        self._command_dispatcher = None
        self._socket_server = None
        self._live_adapter = None
        self._init_components()

    def _init_components(self) -> None:
        from .command_dispatcher import CommandDispatcher
        from .live_adapter import MockLiveAdapter
        from .socket_server import SocketServer

        self._logger.info("AbletonGPT loaded")
        self._live_adapter = MockLiveAdapter()
        self._command_dispatcher = CommandDispatcher(adapter=self._live_adapter)
        self._socket_server = SocketServer(self._command_dispatcher)
        self._socket_server.start(host="127.0.0.1", port=8765)

    def disconnect(self) -> None:
        """Stop the socket server and clean up resources."""
        if self._socket_server is not None:
            self._socket_server.stop()
