from math import gcd

import pytest


@pytest.mark.parametrize(
    "a, b, mod, expected",
    [
        (3, 4, 5, 2),
        (0, 0, 7, 0),
        (6, 6, 6, 0),
        (1, 1, 2, 0),
        (10, 15, 7, 4),
        (0, 5, 3, 2),
        (999, 1, 1000, 0),
        (7, 3, 10, 0),
    ],
)
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


@pytest.mark.parametrize(
    "a, b, mod, expected",
    [
        (7, 3, 5, 4),
        (0, 0, 7, 0),
        (6, 6, 6, 0),
        (1, 1, 2, 0),
        (15, 10, 7, 5),
        (5, 0, 3, 2),
        (1000, 1, 1000, 999),
        (3, 7, 10, 6),
    ],
)
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


@pytest.mark.parametrize(
    "a, b, mod, expected",
    [
        (3, 4, 5, 2),
        (0, 5, 7, 0),
        (6, 6, 6, 0),
        (1, 1, 2, 1),
        (3, 5, 7, 1),
        (9, 9, 10, 1),
        (999, 2, 1000, 998),
        (7, 3, 10, 1),
    ],
)
def test_modulo_multiplication(a, b, mod, expected):
    assert (a * b) % mod == expected


def test_modulo_multiplication_commutativity():
    assert (3 * 5) % 7 == (5 * 3) % 7


def test_modulo_multiplication_identity():
    assert (42 * 1) % 13 == 42 % 13


def test_modulo_multiplication_zero():
    assert (42 * 0) % 13 == 0


def test_modulo_multiplication_associativity():
    mod = 11
    a, b, c = 5, 7, 9
    assert ((a * b) % mod * c) % mod == (a * ((b * c) % mod)) % mod


def test_modulo_multiplication_distributive():
    mod = 13
    a, b, c = 5, 7, 9
    assert (a * (b + c)) % mod == ((a * b) % mod + (a * c) % mod) % mod


def test_modulo_multiplication_large_numbers():
    a = 10**18
    b = 10**18
    mod = 10**9 + 7
    assert (a * b) % mod == (a % mod * (b % mod)) % mod


@pytest.mark.parametrize(
    "base, exp, mod, expected",
    [
        (2, 3, 5, 3),
        (3, 4, 7, 4),
        (2, 10, 1000, 24),
        (5, 0, 7, 1),
        (0, 5, 3, 0),
        (7, 1, 10, 7),
        (2, 8, 255, 1),
        (10, 3, 6, 4),
    ],
)
def test_modulo_exponentiation(base, exp, mod, expected):
    assert pow(base, exp, mod) == expected


def test_modulo_exponentiation_matches_naive():
    assert pow(3, 5, 7) == (3**5) % 7


def test_modulo_exponentiation_identity():
    assert pow(42, 1, 13) == 42 % 13


def test_modulo_exponentiation_zero_exponent():
    assert pow(99, 0, 13) == 1


def test_modulo_exponentiation_fermats_little_theorem():
    p = 17
    for a in range(1, p):
        assert pow(a, p - 1, p) == 1


def test_modulo_exponentiation_large_numbers():
    base = 10**18
    exp = 10**18
    mod = 10**9 + 7
    assert pow(base, exp, mod) == pow(base % mod, exp, mod)


@pytest.mark.parametrize(
    "a, mod, expected",
    [
        (2, 5, 3),
        (3, 7, 5),
        (4, 11, 3),
        (1, 13, 1),
        (10, 17, 12),
        (6, 13, 11),
        (2, 1000000007, 500000004),
    ],
)
def test_modulo_inverse(a, mod, expected):
    assert pow(a, -1, mod) == expected


def test_modulo_inverse_verify():
    mod = 17
    for a in range(1, mod):
        inv = pow(a, -1, mod)
        assert (a * inv) % mod == 1


def test_modulo_inverse_via_fermats_little_theorem():
    p = 19
    for a in range(1, p):
        assert pow(a, -1, p) == pow(a, p - 2, p)


def test_modulo_inverse_self_inverse():
    mod = 17
    assert pow(1, -1, mod) == 1
    assert pow(mod - 1, -1, mod) == mod - 1


def test_modulo_inverse_product():
    mod = 13
    a, b = 3, 5
    inv_a = pow(a, -1, mod)
    inv_b = pow(b, -1, mod)
    inv_ab = pow(a * b, -1, mod)
    assert inv_ab == (inv_a * inv_b) % mod


def test_modulo_inverse_no_inverse():
    with pytest.raises(ValueError):
        pow(2, -1, 4)
    with pytest.raises(ValueError):
        pow(6, -1, 9)


def test_modulo_inverse_large_number():
    a = 10**18
    mod = 10**9 + 7
    inv = pow(a, -1, mod)
    assert (a * inv) % mod == 1


def crt(remainders, moduli):
    """Solve a system of congruences using the Chinese Remainder Theorem.

    Given x ≡ r_i (mod m_i) for pairwise coprime m_i,
    returns (x, M) where x is the unique solution mod M = prod(m_i).
    """
    M = 1
    for m in moduli:
        M *= m
    x = 0
    for r, m in zip(remainders, moduli):
        Mi = M // m
        x += r * Mi * pow(Mi, -1, m)
    return x % M, M


@pytest.mark.parametrize(
    "remainders, moduli, expected",
    [
        ([2, 3, 2], [3, 5, 7], 23),
        ([0, 0], [3, 5], 0),
        ([1, 1, 1], [2, 3, 5], 1),
        ([1, 2, 3], [5, 7, 11], 366),
        ([2, 3], [3, 7], 17),
        ([0, 1], [2, 3], 4),
        ([3, 4, 5], [7, 11, 13], 213),
        ([1, 2, 3, 4], [5, 7, 9, 11], 1731),
    ],
)
def test_crt(remainders, moduli, expected):
    x, _ = crt(remainders, moduli)
    assert x == expected


def test_crt_satisfies_congruences():
    remainders = [2, 3, 2]
    moduli = [3, 5, 7]
    x, _ = crt(remainders, moduli)
    for r, m in zip(remainders, moduli):
        assert x % m == r


def test_crt_uniqueness():
    remainders = [1, 2, 3]
    moduli = [5, 7, 11]
    x, M = crt(remainders, moduli)
    assert M == 5 * 7 * 11
    assert 0 <= x < M


def test_crt_two_moduli():
    x, M = crt([2, 3], [5, 7])
    assert M == 35
    assert x % 5 == 2
    assert x % 7 == 3


def test_crt_all_zero_remainders():
    x, M = crt([0, 0, 0], [3, 5, 7])
    assert x == 0
    assert M == 105


def test_crt_single_congruence():
    x, M = crt([4], [7])
    assert x == 4
    assert M == 7


def test_crt_large_moduli():
    moduli = [1000000007, 1000000009, 998244353]
    remainders = [123456789, 987654321, 111111111]
    x, M = crt(remainders, moduli)
    for r, m in zip(remainders, moduli):
        assert x % m == r
    assert M == moduli[0] * moduli[1] * moduli[2]


def test_crt_coprime_requirement():
    """CRT requires pairwise coprime moduli; non-coprime may give wrong results."""
    moduli = [6, 10]
    assert gcd(moduli[0], moduli[1]) != 1


def mod_div(a, b, mod):
    return (a * pow(b, -1, mod)) % mod


@pytest.mark.parametrize(
    "a, b, mod, expected",
    [
        (6, 3, 7, 2),
        (10, 5, 13, 2),
        (0, 3, 7, 0),
        (1, 1, 11, 1),
        (15, 5, 17, 3),
        (8, 4, 5, 2),
        (7, 7, 13, 1),
        (9, 3, 11, 3),
    ],
)
def test_modulo_division(a, b, mod, expected):
    assert mod_div(a, b, mod) == expected


def test_modulo_division_verify():
    mod = 17
    a, b = 10, 3
    result = mod_div(a, b, mod)
    assert (result * b) % mod == a % mod


def test_modulo_division_self():
    mod = 13
    for a in range(1, mod):
        assert mod_div(a, a, mod) == 1


def test_modulo_division_by_one():
    mod = 11
    for a in range(mod):
        assert mod_div(a, 1, mod) == a % mod


def test_modulo_division_zero_numerator():
    assert mod_div(0, 5, 13) == 0
    assert mod_div(0, 99, 17) == 0


def test_modulo_division_no_inverse():
    with pytest.raises(ValueError):
        mod_div(6, 4, 8)
    with pytest.raises(ValueError):
        mod_div(10, 6, 9)


def test_modulo_division_large_numbers():
    a = 10**18
    b = 10**9 + 3
    mod = 10**9 + 7
    result = mod_div(a, b, mod)
    assert (result * b) % mod == a % mod
