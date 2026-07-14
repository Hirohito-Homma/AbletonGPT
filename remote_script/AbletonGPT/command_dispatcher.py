"""Command dispatcher for the AbletonGPT Remote Script."""

from __future__ import annotations

import logging
from typing import Any, Final

from .commands.transport import TransportCommands
from .live_adapter import LiveAdapter, MockLiveAdapter
from .registry import CommandRegistry

logger: Final[logging.Logger] = logging.getLogger(__name__)


class CommandDispatcher:
    """Dispatch commands through a registry of handlers."""

    def __init__(self, adapter: LiveAdapter | None = None) -> None:
        self._logger = logger
        self._registry = CommandRegistry()
        self._adapter = adapter or MockLiveAdapter()
        self._transport_commands = TransportCommands(self._adapter)
        self._register_defaults()

    def _register_defaults(self) -> None:
        self._registry.register("play", self._transport_commands.play)
        self._registry.register("stop", self._transport_commands.stop)
        self._registry.register("get_tempo", self._transport_commands.get_tempo)
        self._registry.register("set_tempo", self._transport_commands.set_tempo)

    def dispatch(self, command: str, payload: dict[str, Any] | None = None) -> dict[str, Any]:
        """Handle a command and return a placeholder response."""
        self._logger.info("CommandDispatcher: command name=%s", command)
        try:
            handler = self._registry._handlers.get(command)
            if handler is not None:
                self._logger.info("CommandDispatcher: handler selected for %s", command)
            result = self._registry.dispatch(command, payload)
            self._logger.info("CommandDispatcher: handler completed for %s", command)
            return result
        except Exception as exc:
            self._logger.exception("CommandDispatcher: exception in %s: %s", command, exc)
            raise
