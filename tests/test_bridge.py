import logging
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from abletongpt.bridge import AbletonBridge


class DummyBridge(AbletonBridge):
    def __init__(self) -> None:
        super().__init__()
        self._connected = False

    def connect(self) -> None:
        self._connected = True

    def disconnect(self) -> None:
        self._connected = False

    def is_connected(self) -> bool:
        return self._connected


def test_bridge_is_abstract() -> None:
    assert AbletonBridge.__abstractmethods__ == frozenset({"connect", "disconnect", "is_connected"})


def test_transport_methods_raise_not_implemented(caplog: pytest.LogCaptureFixture) -> None:
    bridge = DummyBridge()

    with caplog.at_level(logging.WARNING):
        with pytest.raises(NotImplementedError):
            bridge.play()

        with pytest.raises(NotImplementedError):
            bridge.stop()

        with pytest.raises(NotImplementedError):
            bridge.get_tempo()

        with pytest.raises(NotImplementedError):
            bridge.set_tempo(120)

    assert "NotImplementedError" in caplog.text
