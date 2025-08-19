from verbose_fishstick.calculator import add, subtract


def test_addition() -> None:
    assert add(2, 3) == 5


def test_subtraction() -> None:
    assert subtract(5, 3) == 2
