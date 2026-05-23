"""
Project 1: Basic logic gates.
Rule: nand() is the only primitive. Do NOT use Python's logical
      operators (and, or, not, ^, &, |, conditional tricks).
      Build everything by composing gates you already defined.
"""


def nand(a: int, b: int) -> int:
    """The only primitive gate. Defined by its truth table."""
    table = {(0, 0): 1, (0, 1): 1, (1, 0): 1, (1, 1): 0}
    return table[(a, b)]


# ---- Worked examples ----

def not_(a: int) -> int:
    return nand(a, a)


def and_(a: int, b: int) -> int:
    return not_(nand(a, b))


# ---- Your turn ----

def or_(a: int, b: int) -> int:
    # Hint: De Morgan. a or b == not (not a and not b)
    raise NotImplementedError


def xor(a: int, b: int) -> int:
    raise NotImplementedError


def mux(a: int, b: int, sel: int) -> int:
    """Return a if sel==0, else b."""
    raise NotImplementedError


def dmux(x: int, sel: int) -> tuple[int, int]:
    """Return (x, 0) if sel==0, else (0, x)."""
    raise NotImplementedError


# ---- Tests ----

def test():
    # nand
    assert nand(0, 0) == 1
    assert nand(1, 1) == 0

    # not
    assert not_(0) == 1
    assert not_(1) == 0

    # and
    assert and_(0, 0) == 0
    assert and_(0, 1) == 0
    assert and_(1, 0) == 0
    assert and_(1, 1) == 1

    # or
    assert or_(0, 0) == 0
    assert or_(0, 1) == 1
    assert or_(1, 0) == 1
    assert or_(1, 1) == 1

    # xor
    assert xor(0, 0) == 0
    assert xor(0, 1) == 1
    assert xor(1, 0) == 1
    assert xor(1, 1) == 0

    # mux
    assert mux(0, 1, 0) == 0
    assert mux(0, 1, 1) == 1
    assert mux(1, 0, 0) == 1
    assert mux(1, 0, 1) == 0

    # dmux
    assert dmux(1, 0) == (1, 0)
    assert dmux(1, 1) == (0, 1)
    assert dmux(0, 0) == (0, 0)

    print("All gates passed!")


if __name__ == "__main__":
    test()
