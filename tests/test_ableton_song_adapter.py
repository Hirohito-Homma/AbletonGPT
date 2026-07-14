from remote_script.AbletonGPT.ableton_song_adapter import AbletonSongAdapter
from remote_script.AbletonGPT.live_adapter import LiveAdapter, MockLiveAdapter


class DummySong:
    def __init__(self) -> None:
        self.is_playing = False
        self.tempo = 120

    def start_playing(self) -> None:
        self.is_playing = True

    def stop_playing(self) -> None:
        self.is_playing = False


class DummyControlSurface:
    def __init__(self) -> None:
        self.song = DummySong()


def test_ableton_song_adapter_play_starts_song() -> None:
    surface = DummyControlSurface()
    adapter = AbletonSongAdapter(surface)

    adapter.play()

    assert surface.song.is_playing is True


def test_live_adapter_uses_ableton_song_adapter_when_control_surface_is_present() -> None:
    adapter = LiveAdapter(control_surface=DummyControlSurface())

    song = adapter.song()

    assert isinstance(song, AbletonSongAdapter)


def test_mock_live_adapter_remains_available_for_tests() -> None:
    adapter = MockLiveAdapter()

    assert adapter.song() is not None
