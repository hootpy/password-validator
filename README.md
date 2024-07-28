# Password Validation

## Description

This is a simple password validation program that checks if a password is valid or not. The password is considered valid if it meets the following criteria:

- At least 1 letter between [a-z]
- At least 1 number between [0-9]
- At least 1 letter between [A-Z]
- At least 1 character from [$#@]
- Minimum length of 8 characters

## Installation

```bash
poetry install
```

## Usage

```bash
from password_validation import validate_pw
...

validate_pw('Password123#') # True
```

## Tests

```bash
pytest --tb=no -v
```

## Built with Poetry
