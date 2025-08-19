from src.verbose_fishstick import add, subtract


=======
from verbose_fishstick import add, subtract
=======
from verbose_fishstick.calculator import add, subtract

=======
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from verbose_fishstick import add, subtract  # noqa: E402


def test_addition() -> None:
    assert add(2, 3) == 5


def test_subtraction() -> None:
    assert subtract(5, 3) == 2

