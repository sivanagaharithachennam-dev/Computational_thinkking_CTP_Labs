from Calculator import add, multiply
from hypothesis import given, strategies as st


def test_add():
    assert add(2, 3) == 5


def test_multiply():
    assert multiply(2, 3) == 6


@given(st.integers(), st.integers())
def test_add_property(a, b):
    assert add(a, b) == a + b