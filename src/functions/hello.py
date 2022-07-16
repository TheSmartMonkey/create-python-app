from src.models.helloModel import HttpMessageModel


def message() -> str:
    print("hello world !")


def inc(x: int) -> int:
    return x + 1


def http_message(message: str) -> HttpMessageModel:
    return {
        "message": message,
        "code": 200,
    }
