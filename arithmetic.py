"""
Project 2: Arithmetic from logic gates.

Convention: 16-bit values are represented as list[int] of length 16,
            index 0 is the least significant bit (LSB-first).

Rule: Build everything from gates.py. No Python +, -, *, &, |, ^, <<, >>.
"""

from gates import and_, or_, xor


def half_adder(a: int, b: int) -> tuple[int, int]:
    """Add two bits. Returns (sum, carry)."""
    return (xor(a, b), and_(a, b))


def full_adder(a: int, b: int, c: int) -> tuple[int, int]:
    """Add three bits. Returns (sum, carry)."""
    s1, c1 = half_adder(a, b)
    sum_, c2 = half_adder(s1, c)
    return (sum_, or_(c1, c2))


def add16(a: list[int], b: list[int]) -> list[int]:
    """Add two 16-bit numbers. Overflow out of the top bit wraps."""
    result = []
    carry = 0
    for i in range(16):
        s, carry = full_adder(a[i], b[i], carry)
        result.append(s)
    return result


def inc16(a: list[int]) -> list[int]:
    """Return a + 1 as 16 bits."""
    return add16(a, [1] + [0] * 15)
