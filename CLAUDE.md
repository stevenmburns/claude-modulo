# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A Python project exploring modular arithmetic operations. The main entry point (`main.py`) is a stub; the core content lives in the test suite (`test_main.py`), which validates modular addition, subtraction, multiplication, exponentiation, inverse, and division using Python builtins and `pow()`.

## Commands

- **Run all tests:** `pytest`
- **Run a single test by name:** `pytest -k test_modulo_addition`
- **Run with verbose output:** `pytest -v`

## Environment

- Python 3.14, managed via a local `venv/` virtualenv
- Only dependency: `pytest`
- Activate venv: `source venv/bin/activate`
