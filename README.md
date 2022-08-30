# create-python-app

Simple python app with typing, linting, formating and venv

This template has been created following this article : [set-up-perfect-python-project](https://sourcery.ai/blog/python-best-practices)

## Installation

```sh
npx degit https://github.com/TheSmartMonkey/create-python-app app
```

## Getting started

1. Install pipx : https://pypa.github.io/pipx/

1. Avalable commands with `npm run` (`npm run start` runes your code)

```
start
    py main.py
test
    python -m pipenv run pytest
lint
    python -m pipenv run mypy .
format
    python -m black . && python -m isort -y
format:check
    python -m black --check . && python -m isort --check-only
coverage
    python -m pipenv run pytest --cov --cov-fail-under=90
```

## Annexe

1. Python type cheat sheet : [mypy-types-cheat-sheet](https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html)

## Folder tree

```
│   .vscode
│   .gitignore
│   LICENSE
│   main.py
│   package.json
│   Pipfile
│   Pipfile.lock
│   README.md
│   setup.cfg
│   tree.txt
│
+---src
│   +---functions
│   │   │   __init__.py
│   │   │   hello.py
│   │   │   README.md
│   │           
│   +---lib
│   │       __init__.py
│   │       README.md
│   │       utils.py
│   │       
│   +---models
│       │   __init__.py
│       │   hello_model.py
│
+---tests
        __init__.py
        test_sample.py
```
