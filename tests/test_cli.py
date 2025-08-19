import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = PROJECT_ROOT / "src"


def run_cli(*args: str) -> str:
    result = subprocess.run(
        [sys.executable, "-m", "verbose_fishstick.cli", *args],
        capture_output=True,
        text=True,
        cwd=SRC_DIR,
        check=True,
    )
    return result.stdout.strip()


def test_cli_add():
    assert float(run_cli("add", "2", "3")) == 5.0


def test_cli_subtract():
    assert float(run_cli("subtract", "5", "3")) == 2.0
