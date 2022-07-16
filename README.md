# create-python-app

Simple python app with typing, linting, formating and venv

This template has been created following this article : [python-best-practices](https://sourcery.ai/blog/python-best-practices/#pipenv)

## Installation

```sh
npx degit https://github.com/TheSmartMonkey/create-python-app app
```

## Getting started

1. Install pipx : https://pypa.github.io/pipx/

1. Avalable commands with `npm run`

```sh
start
    py main.py
test
    python -m pipenv run pytest
lint
    python -m pipenv run mypy .
format
    python -m black . && python -m isort
format:check
    python -m black --check . && python -m isort --check-only
```

## Annexe

1. Python type cheat sheet : [mypy-types-cheat-sheet](https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html)
