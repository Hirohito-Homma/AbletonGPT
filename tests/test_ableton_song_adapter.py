from remote_script.AbletonGPT.ableton_song_adapter import AbletonSongAdapter
from remote_script.AbletonGPT.live_adapter import LiveAdapter, MockLiveAdapter


class DummyControlSurface:
    def __init__(self) -> None:
        self.song = object()


def test_ableton_song_adapter_play_logs_and_does_not_raise() -> None:
    adapter = AbletonSongAdapter(DummyControlSurface())

    adapter.play()


def test_live_adapter_uses_ableton_song_adapter_when_control_surface_is_present() -> None:
    adapter = LiveAdapter(control_surface=DummyControlSurface())

    song = adapter.song()

    assert isinstance(song, AbletonSongAdapter)


def test_mock_live_adapter_remains_available_for_tests() -> None:
    adapter = MockLiveAdapter()

    assert adapter.song() is not None
