"""Core library for AbletonGPT."""

from __future__ import annotations

from typing import Any


class AbletonGPT:
    """A small proof-of-concept core class for AbletonGPT."""

    def __init__(self, model: str = "gpt-4o-mini") -> None:
        self.model = model

    def generate_prompt(self, project_name: str, instructions: str) -> str:
        return f"Create an Ableton Live project for {project_name}: {instructions}"

    def synthesize(self, prompt: str, **kwargs: Any) -> str:
        return f"[Synthesized output for prompt: {prompt}]"
