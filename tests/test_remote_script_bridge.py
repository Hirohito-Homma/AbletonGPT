import logging
from unittest.mock import Mock

import pytest

from abletongpt.bridges import RemoteScriptBridge
from abletongpt.socket_transport import SocketTransport


def test_remote_script_bridge_connection_state() -> None:
    transport = Mock(spec=SocketTransport)
    transport.is_connected.side_effect = [False, True, False]

    bridge = RemoteScriptBridge(transport=transport)

    assert bridge.is_connected() is False

    bridge.connect()
    assert bridge.is_connected() is True

    bridge.disconnect()
    assert bridge.is_connected() is False


def test_remote_script_transport_methods_send_commands_and_return_response() -> None:
    transport = Mock(spec=SocketTransport)
    transport.is_connected.return_value = True
    transport.receive.return_value = {"status": "ok"}

    bridge = RemoteScriptBridge(transport=transport)
    response = bridge.play()

    transport.send.assert_called_once_with({"command": "play"})
    assert response == {"status": "ok"}


def test_remote_script_bridge_propagates_connection_errors() -> None:
    transport = Mock(spec=SocketTransport)
    transport.is_connected.return_value = False

    bridge = RemoteScriptBridge(transport=transport)

    with pytest.raises(ConnectionError):
        bridge.play()


def test_remote_script_bridge_handles_transport_json_errors() -> None:
    transport = Mock(spec=SocketTransport)
    transport.is_connected.return_value = True
    transport.receive.side_effect = ValueError("invalid json")

    bridge = RemoteScriptBridge(transport=transport)

    with pytest.raises(ValueError):
        bridge.play()
