from unittest.mock import Mock

from remote_script.AbletonGPT.command_dispatcher import CommandDispatcher


def test_dispatcher_returns_not_implemented_response() -> None:
    dispatcher = CommandDispatcher()

    response = dispatcher.dispatch("play", {"tempo": 120})

    assert response["status"] == "not_implemented"
    assert response["command"] == "play"


def test_dispatcher_uses_logger_without_failing() -> None:
    dispatcher = CommandDispatcher()
    dispatcher._logger = Mock()

    response = dispatcher.dispatch("stop")

    assert response["status"] == "not_implemented"
    assert dispatcher._logger.info.call_count >= 1
