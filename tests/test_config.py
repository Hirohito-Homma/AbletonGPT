from pathlib import Path

from ableton_gpt.config import load_config


def test_load_config_missing_file() -> None:
    result = load_config("does_not_exist.toml")
    assert result == {}


def test_load_config_existing_file(tmp_path: Path) -> None:
    config_file = tmp_path / "config.txt"
    config_file.write_text("test=1", encoding="utf-8")
    result = load_config(str(config_file))
    assert result["path"] == str(config_file)
    assert "test=1" in result["content"]
