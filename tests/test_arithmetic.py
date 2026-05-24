import pytest

from arithmetic import add16, full_adder, half_adder, inc16

# Test helpers. These use Python bitwise ops because they are
# scaffolding for tests, not part of the gate-built arithmetic.


def bits(n: int) -> list[int]:
    """int → 16-bit LSB-first list."""
    return [(n >> i) & 1 for i in range(16)]


def num(b: list[int]) -> int:
    """16-bit LSB-first list → int (unsigned)."""
    return sum(bit << i for i, bit in enumerate(b))


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (0, 0, (0, 0)),
        (0, 1, (1, 0)),
        (1, 0, (1, 0)),
        (1, 1, (0, 1)),
    ],
)
def test_half_adder(a, b, expected):
    assert half_adder(a, b) == expected


@pytest.mark.parametrize(
    "a,b,c,expected",
    [
        (0, 0, 0, (0, 0)),
        (0, 0, 1, (1, 0)),
        (0, 1, 0, (1, 0)),
        (0, 1, 1, (0, 1)),
        (1, 0, 0, (1, 0)),
        (1, 0, 1, (0, 1)),
        (1, 1, 0, (0, 1)),
        (1, 1, 1, (1, 1)),
    ],
)
def test_full_adder(a, b, c, expected):
    assert full_adder(a, b, c) == expected


@pytest.mark.parametrize(
    "x,y,expected",
    [
        (0, 0, 0),
        (1, 0, 1),
        (1, 1, 2),
        (7, 3, 10),
        (1234, 5678, 6912),
        (0xFFFF, 1, 0),  # overflow wraps
        (0xFFFF, 0xFFFF, 0xFFFE),
    ],
)
def test_add16(x, y, expected):
    assert num(add16(bits(x), bits(y))) == expected


@pytest.mark.parametrize(
    "x,expected",
    [
        (0, 1),
        (1, 2),
        (41, 42),
        (0xFFFE, 0xFFFF),
        (0xFFFF, 0),  # overflow wraps
    ],
)
def test_inc16(x, expected):
    assert num(inc16(bits(x))) == expected
