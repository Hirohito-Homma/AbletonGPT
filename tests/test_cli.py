import argparse
from ableton_gpt.cli import main


def test_cli_help(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["ableton-gpt", "MySong", "Generate a bassline"])
    main()
    captured = capsys.readouterr()
    assert "Synthesized output" in captured.out
