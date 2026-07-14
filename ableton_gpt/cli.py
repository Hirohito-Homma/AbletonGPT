"""CLI entrypoint for AbletonGPT."""

from __future__ import annotations

import argparse

from .core import AbletonGPT


def main() -> None:
    parser = argparse.ArgumentParser(description="AbletonGPT CLI")
    parser.add_argument("project_name", help="Name of the Ableton project")
    parser.add_argument(
        "instructions",
        help="Instructions for creating the Ableton project",
    )
    args = parser.parse_args()

    agent = AbletonGPT()
    prompt = agent.generate_prompt(args.project_name, args.instructions)
    result = agent.synthesize(prompt)
    print(result)
