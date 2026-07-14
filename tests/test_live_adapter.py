from remote_script.AbletonGPT.command_dispatcher import CommandDispatcher
from remote_script.AbletonGPT.live_adapter import MockLiveAdapter


def test_mock_live_adapter_tracks_state() -> None:
    adapter = MockLiveAdapter()

    adapter.play()
    assert adapter.playing is True

    adapter.stop()
    assert adapter.playing is False

    adapter.set_tempo(140)
    assert adapter.get_tempo() == 140


def test_dispatcher_uses_adapter_for_transport_commands() -> None:
    adapter = MockLiveAdapter()
    dispatcher = CommandDispatcher(adapter=adapter)

    response = dispatcher.dispatch("play")
    assert response["status"] == "not_implemented"
    assert adapter.playing is True

    response = dispatcher.dispatch("get_tempo")
    assert response["tempo"] == 120

    response = dispatcher.dispatch("set_tempo", {"bpm": 130})
    assert response["tempo"] == 130
    assert adapter.get_tempo() == 130
