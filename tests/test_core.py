from ableton_gpt.core import AbletonGPT


def test_generate_prompt() -> None:
    agent = AbletonGPT()
    prompt = agent.generate_prompt("Demo", "Make a drum rack")

    assert "Demo" in prompt
    assert "drum rack" in prompt


def test_synthesize() -> None:
    agent = AbletonGPT()
    output = agent.synthesize("Hello world")

    assert "Synthesized output" in output
