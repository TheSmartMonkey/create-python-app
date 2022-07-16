from src.functions.hello import inc


def test_answer() -> None:
    assert inc(3) == 4
