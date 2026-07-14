from remote_script.AbletonGPT.command_dispatcher import CommandDispatcher
from remote_script.AbletonGPT.live_adapter import MockLiveAdapter


def test_song_adapter_is_exposed_via_live_adapter() -> None:
    adapter = MockLiveAdapter()

    song = adapter.song()
    song.play()
    assert adapter.playing is True

    song.stop()
    assert adapter.playing is False

    song.set_tempo(150)
    assert song.get_tempo() == 150


def test_dispatcher_uses_song_adapter_via_live_adapter() -> None:
    adapter = MockLiveAdapter()
    dispatcher = CommandDispatcher(adapter=adapter)

    dispatcher.dispatch("play")
    assert adapter.playing is True

    response = dispatcher.dispatch("get_tempo")
    assert response["tempo"] == 120
