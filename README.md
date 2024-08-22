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
make test
```

## Build

The package can be built using the following command:

```bash
make build
```

Package will be built in the `dist/` directory.

After building the package, it can be installed using the following command:

```bash
pip install ./password_validator-0.1.0.tar.gz

# or if using poetry as package manager

poetry add ./password_validator-0.1.0.tar.gz
```

## License
For more information on the license, please refer to the `LICENSE` file in the root directory of this project.
