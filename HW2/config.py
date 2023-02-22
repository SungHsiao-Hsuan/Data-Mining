from pathlib import Path
from typing import Final

IN_DIR: Final[Path] = Path(__file__).parent / "inputs"

assert IN_DIR.exists(), f"inputs directory does not exist: {IN_DIR}"
