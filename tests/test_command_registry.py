from remote_script.AbletonGPT.command_dispatcher import CommandDispatcher
from remote_script.AbletonGPT.registry import CommandRegistry


def test_registry_dispatches_known_commands() -> None:
    registry = CommandRegistry()
    registry.register("play", lambda payload: {"status": "ok"})

    response = registry.dispatch("play", {"foo": "bar"})

    assert response == {"status": "ok"}


def test_registry_returns_unknown_command_error() -> None:
    registry = CommandRegistry()

    response = registry.dispatch("missing")

    assert response == {"status": "error", "message": "unknown command"}


def test_dispatcher_uses_registry_for_supported_commands() -> None:
    dispatcher = CommandDispatcher()

    response = dispatcher.dispatch("play", {"tempo": 120})

    assert response["status"] == "not_implemented"
    assert response["command"] == "play"
