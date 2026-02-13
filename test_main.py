import pytest


@pytest.mark.parametrize("a, b, mod, expected", [
    (3, 4, 5, 2),
    (0, 0, 7, 0),
    (6, 6, 6, 0),
    (1, 1, 2, 0),
    (10, 15, 7, 4),
    (0, 5, 3, 2),
    (999, 1, 1000, 0),
    (7, 3, 10, 0),
])
def test_modulo_addition(a, b, mod, expected):
    assert (a + b) % mod == expected


def test_modulo_addition_commutativity():
    assert (3 + 5) % 7 == (5 + 3) % 7


def test_modulo_addition_identity():
    assert (42 + 0) % 13 == 42 % 13


def test_modulo_addition_associativity():
    mod = 11
    a, b, c = 5, 7, 9
    assert ((a + b) % mod + c) % mod == (a + (b + c) % mod) % mod


def test_modulo_addition_large_numbers():
    a = 10**18
    b = 10**18
    mod = 10**9 + 7
    assert (a + b) % mod == (a % mod + b % mod) % mod


@pytest.mark.parametrize("a, b, mod, expected", [
    (7, 3, 5, 4),
    (0, 0, 7, 0),
    (6, 6, 6, 0),
    (1, 1, 2, 0),
    (15, 10, 7, 5),
    (5, 0, 3, 2),
    (1000, 1, 1000, 999),
    (3, 7, 10, 6),
])
def test_modulo_subtraction(a, b, mod, expected):
    assert (a - b) % mod == expected


def test_modulo_subtraction_self():
    assert (42 - 42) % 13 == 0


def test_modulo_subtraction_identity():
    assert (42 - 0) % 13 == 42 % 13


def test_modulo_subtraction_negative_result():
    assert (3 - 8) % 5 == 0
    assert (1 - 10) % 7 == 5


def test_modulo_subtraction_large_numbers():
    a = 10**18
    b = 10**18 - 1
    mod = 10**9 + 7
    assert (a - b) % mod == (a % mod - b % mod) % mod
