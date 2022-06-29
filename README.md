TODO
====

[![Build Status](https://travis-ci.com/afaulconbridge/todo.svg?branch=master)](https://travis-ci.com/afaulconbridge/todo)
[![PyPI version](https://badge.fury.io/py/todo.svg)](https://badge.fury.io/py/todo)

development
-----------

```sh
# Create virtual environment
python3 -m venv venv
# Activate virtual environment
source venv/bin/activate

# Install editable with development extras
pip install -e '.[dev]'
# Enable pre-commit hooks
pre-commit install
# Run pre-commit hooks without committing
pre-commit run --all-files
# Note pre-commit is configured to use:
# - isort to sort imports
# - black to format code

# Freeze dependencies
pip-compile
# Freeze dev dependencies
pip-compile requirements-dev.in
# Install exact requirements
pip-sync requirements.txt requirements-dev.txt
# Print dependencies
pipdeptree

# Run tests
pytest
# Run tests, print coverage
coverage run -m pytest && coverage report -m
# Type checking
mypy TODO
```

Global git ignores per https://help.github.com/en/github/using-git/ignoring-files#configuring-ignored-files-for-all-repositories-on-your-computer

For release to PyPI see https://packaging.python.org/tutorials/packaging-projects/

To add a new development dependency, add to `requirements-dev.in` then run `pip-compile requirements-dev.in`

To add a new dependency, add to `requirements.in` then run `pip-compile`
