from pathlib import Path

from ableton_gpt.utils import save_json


def test_save_json(tmp_path: Path) -> None:
    file_path = tmp_path / "out" / "data.json"
    save_json(file_path, {"demo": 123})
    assert file_path.exists()
    assert file_path.read_text(encoding="utf-8")
    assert "demo" in file_path.read_text(encoding="utf-8")
