"""TCP socket transport for messaging with an Ableton Remote Script."""

from __future__ import annotations

import json
import logging
import socket
from typing import Any, Final

logger: Final[logging.Logger] = logging.getLogger(__name__)


class SocketTransport:
    """A simple JSON-over-TCP transport that is mockable in tests."""

    def __init__(self, timeout: float | None = None) -> None:
        self._timeout = timeout
        self._connected = False
        self._socket: socket.socket | None = None
        self._logger = logger

    def connect(self, host: str = "127.0.0.1", port: int = 8765) -> None:
        """Open a TCP connection to the supplied host and port."""
        self._socket = socket.create_connection((host, port), timeout=self._timeout)
        if self._timeout is not None:
            self._socket.settimeout(self._timeout)
        self._connected = True
        self._logger.info("Connected to %s:%s", host, port)

    def disconnect(self) -> None:
        """Close the TCP connection if it exists."""
        if self._socket is not None:
            self._socket.close()
        self._socket = None
        self._connected = False
        self._logger.info("Disconnected from socket transport")

    def send(self, command: dict[str, Any]) -> None:
        """Serialize a dictionary to JSON and send it over the socket."""
        if not self._connected or self._socket is None:
            raise ConnectionError("Socket transport is not connected")
        payload = json.dumps(command)
        self._socket.sendall(payload.encode("utf-8"))
        self._logger.debug("Sent message: %s", payload)

    def receive(self) -> dict[str, Any]:
        """Receive a JSON payload from the socket and deserialize it."""
        if not self._connected or self._socket is None:
            raise ConnectionError("Socket transport is not connected")
        raw_payload = self._socket.recv(4096)
        if not raw_payload:
            raise ConnectionError("Socket transport closed")
        payload = json.loads(raw_payload.decode("utf-8"))
        self._logger.debug("Received message: %s", payload)
        return payload

    def is_connected(self) -> bool:
        """Return whether the transport is currently connected."""
        return self._connected
