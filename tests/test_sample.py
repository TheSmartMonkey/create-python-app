from src.functions.hello import http_message, inc, message


def test_inc() -> None:
    assert inc(3) == 4


def test_http_message() -> None:
    message = "test message"
    assert http_message("").code == 200
    assert http_message(message).message == message
