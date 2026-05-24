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
