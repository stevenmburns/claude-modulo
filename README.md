# claude-modulo

[![CI](https://github.com/stevenmburns/claude-modulo/actions/workflows/ci.yml/badge.svg)](https://github.com/stevenmburns/claude-modulo/actions/workflows/ci.yml)

A Python project exploring modular arithmetic operations, with a comprehensive test suite covering:

- **Addition** – commutativity, identity, associativity
- **Subtraction** – identity, negative results
- **Multiplication** – commutativity, identity, zero, associativity, distributive property
- **Exponentiation** – identity, zero exponent, Fermat's little theorem
- **Modular inverse** – verification, Fermat's little theorem equivalence, non-existent inverses
- **Modular division** – verification, self-division, division by one, non-existent inverses
- **Chinese Remainder Theorem** – congruence satisfaction, uniqueness, large moduli, coprime requirement

All operations are tested with large numbers (10^18) to verify correctness at scale.

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install pytest ruff
```

## Running tests

```bash
pytest
pytest -v          # verbose output
pytest -k test_modulo_addition   # run a specific test
```

## Linting

```bash
ruff check .            # lint
ruff format --check .   # check formatting
ruff format .           # auto-format
```
