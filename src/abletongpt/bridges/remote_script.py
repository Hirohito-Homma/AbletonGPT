"""Concrete bridge implementation for a Remote Script style Ableton integration."""

from __future__ import annotations

import json
import logging
from typing import Any, Final

from abletongpt.bridge import AbletonBridge
from abletongpt.socket_transport import SocketTransport

logger: Final[logging.Logger] = logging.getLogger(__name__)


class RemoteScriptBridge(AbletonBridge):
    """Socket-backed bridge implementation that talks to the Remote Script server."""

    def __init__(self, transport: SocketTransport | None = None) -> None:
        super().__init__()
        self._transport = transport or SocketTransport()
        self._connected = False

    def connect(self, host: str = "127.0.0.1", port: int = 8765) -> None:
        """Connect to the Remote Script socket server."""
        self._transport.connect(host=host, port=port)
        self._connected = True
        self._logger.info("RemoteScriptBridge connected")

    def disconnect(self) -> None:
        """Disconnect from the Remote Script socket server."""
        self._transport.disconnect()
        self._connected = False
        self._logger.info("RemoteScriptBridge disconnected")

    def is_connected(self) -> bool:
        """Return the current connection state."""
        return self._connected

    def play(self) -> dict[str, Any]:
        """Start playback through the remote script bridge."""
        return self._send_command({"command": "play"})

    def stop(self) -> dict[str, Any]:
        """Stop playback through the remote script bridge."""
        return self._send_command({"command": "stop"})

    def get_tempo(self) -> dict[str, Any]:
        """Read tempo from the remote script bridge."""
        return self._send_command({"command": "get_tempo"})

    def set_tempo(self, bpm: int) -> dict[str, Any]:
        """Set tempo on the remote script bridge."""
        return self._send_command({"command": "set_tempo", "bpm": bpm})

    def _send_command(self, command: dict[str, Any]) -> dict[str, Any]:
        if not self._transport.is_connected():
            raise ConnectionError("RemoteScriptBridge is not connected")

        try:
            self._transport.send(command)
            response = self._transport.receive()
        except (ConnectionError, TimeoutError, json.JSONDecodeError) as exc:
            self._logger.error("Socket command failed: %s", exc)
            raise

        return response
