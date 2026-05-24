import pytest

from gates import and_, dmux, mux, nand, not_, or_, xor


@pytest.mark.parametrize(
    "a,b,expected",
    [(0, 0, 1), (0, 1, 1), (1, 0, 1), (1, 1, 0)],
)
def test_nand(a, b, expected):
    assert nand(a, b) == expected


@pytest.mark.parametrize("a,expected", [(0, 1), (1, 0)])
def test_not(a, expected):
    assert not_(a) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [(0, 0, 0), (0, 1, 0), (1, 0, 0), (1, 1, 1)],
)
def test_and(a, b, expected):
    assert and_(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 1)],
)
def test_or(a, b, expected):
    assert or_(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0)],
)
def test_xor(a, b, expected):
    assert xor(a, b) == expected


@pytest.mark.parametrize(
    "a,b,sel,expected",
    [
        (0, 1, 0, 0),
        (0, 1, 1, 1),
        (1, 0, 0, 1),
        (1, 0, 1, 0),
    ],
)
def test_mux(a, b, sel, expected):
    assert mux(a, b, sel) == expected


@pytest.mark.parametrize(
    "x,sel,expected",
    [
        (0, 0, (0, 0)),
        (0, 1, (0, 0)),
        (1, 0, (1, 0)),
        (1, 1, (0, 1)),
    ],
)
def test_dmux(x, sel, expected):
    assert dmux(x, sel) == expected
