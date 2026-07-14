import json
import sys
from pathlib import Path
from unittest.mock import Mock, patch

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from abletongpt.socket_transport import SocketTransport


def test_connect_uses_tcp_socket_and_timeout() -> None:
    mock_socket = Mock()
    with patch("abletongpt.socket_transport.socket.create_connection", return_value=mock_socket) as create_connection:
        transport = SocketTransport(timeout=2.5)
        transport.connect("127.0.0.1", 8765)

    create_connection.assert_called_once_with(("127.0.0.1", 8765), timeout=2.5)
    mock_socket.settimeout.assert_called_once_with(2.5)
    assert transport.is_connected() is True


def test_send_serializes_json_payload() -> None:
    mock_socket = Mock()
    transport = SocketTransport()
    transport._socket = mock_socket
    transport._connected = True

    transport.send({"command": "play"})

    mock_socket.sendall.assert_called_once_with(b'{"command": "play"}')


def test_receive_deserializes_json_payload() -> None:
    mock_socket = Mock()
    mock_socket.recv.return_value = b'{"command": "stop"}'
    transport = SocketTransport()
    transport._socket = mock_socket
    transport._connected = True

    payload = transport.receive()

    assert payload == {"command": "stop"}
    mock_socket.recv.assert_called_once_with(4096)


def test_disconnect_closes_socket_and_clears_state() -> None:
    mock_socket = Mock()
    transport = SocketTransport()
    transport._socket = mock_socket
    transport._connected = True

    transport.disconnect()

    mock_socket.close.assert_called_once_with()
    assert transport.is_connected() is False
