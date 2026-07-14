"""Lightweight socket server for handling JSON commands."""

from __future__ import annotations

import json
import logging
import socket
import threading
from typing import Any, Final

from .command_dispatcher import CommandDispatcher

logger: Final[logging.Logger] = logging.getLogger(__name__)


class SocketServer:
    """A simple threaded TCP socket server that dispatches JSON commands."""

    def __init__(self, dispatcher: CommandDispatcher) -> None:
        self._dispatcher = dispatcher
        self._logger = logger
        self._server_socket: socket.socket | None = None
        self._thread: threading.Thread | None = None
        self._running = False

    def start(self, host: str = "127.0.0.1", port: int = 8765) -> None:
        """Start the socket server in a background thread."""
        if self._running:
            return

        self._server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._server_socket.bind((host, port))
        self._server_socket.listen(1)
        self._running = True

        self._thread = threading.Thread(target=self._serve, daemon=True)
        self._thread.start()
        self._logger.info("Socket server listening on %s:%s", host, port)

    def stop(self) -> None:
        """Stop the socket server."""
        self._running = False
        if self._server_socket is not None:
            self._server_socket.close()
            self._server_socket = None
        if self._thread is not None:
            self._thread.join(timeout=0.5)
            self._thread = None

    def _serve(self) -> None:
        while self._running:
            try:
                client_socket, client_addr = self._server_socket.accept()  # type: ignore[union-attr]
                self._logger.info("Client connected from %s", client_addr)
            except OSError:
                break

            with client_socket:
                data = b""
                while self._running:
                    chunk = client_socket.recv(4096)
                    if not chunk:
                        break
                    data += chunk
                    if b"\n" in chunk:
                        break

                if data:
                    try:
                        message = json.loads(data.decode("utf-8"))
                        self._logger.info("Raw JSON received: %s", message)
                        command = message.get("command", "")
                        self._logger.info("Command dispatched: %s", command)
                        response = self._dispatcher.dispatch(command, message)
                        self._logger.info("Response generated: %s", response)
                        response_payload = json.dumps(response).encode("utf-8")
                        client_socket.sendall(response_payload)
                        self._logger.info("Response sent: %s", response)
                    except (json.JSONDecodeError, UnicodeDecodeError) as exc:
                        self._logger.warning("Invalid JSON payload: %s", exc)
                        client_socket.sendall(b'{"status":"error"}')

                self._logger.info("Client disconnected from %s", client_addr)

