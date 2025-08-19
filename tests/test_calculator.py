"""Tests for the calculator helpers exposed by the package."""

import sys
from pathlib import Path

# Ensure the package under ``src`` takes precedence when importing
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from verbose_fishstick import add, subtract  # noqa: E402


def test_addition() -> None:
    """``add`` should return the sum of two numbers."""
    assert add(2, 3) == 5


def test_subtraction() -> None:
    """``subtract`` should return the difference of two numbers."""
    assert subtract(5, 3) == 2

