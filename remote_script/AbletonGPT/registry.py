"""Command registry for dispatching Remote Script actions."""

from __future__ import annotations

from typing import Any, Callable


class CommandRegistry:
    """Registry that maps command names to callable handlers."""

    def __init__(self) -> None:
        self._handlers: dict[str, Callable[[dict[str, Any] | None], dict[str, Any]]] = {}

    def register(self, name: str, handler: Callable[[dict[str, Any] | None], dict[str, Any]]) -> None:
        """Register a handler for a command name."""
        self._handlers[name] = handler

    def dispatch(self, name: str, payload: dict[str, Any] | None = None) -> dict[str, Any]:
        """Dispatch a command to a registered handler or return an error response."""
        handler = self._handlers.get(name)
        if handler is None:
            return {"status": "error", "message": "unknown command"}
        return handler(payload)
