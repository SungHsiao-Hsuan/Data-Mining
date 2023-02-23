from pathlib import Path
from typing import Final

from args import *

dir = title

IN_DIR: Final[Path] = Path(__file__).parent.parent / "inputs"
OUT_DIR: Final[Path] = Path(__file__).parent.parent / "results" / dir

assert IN_DIR.exists(), f"inputs directory does not exist: {IN_DIR}"
OUT_DIR.mkdir(exist_ok=True)


