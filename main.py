# SPDX-License-Identifier: MIT
"""Write the Make the AI Judge Laugh entry line to /output/entry.txt."""
import os
from pathlib import Path

ENTRY_TEXT = (
    "My calendar is a museum of other people's priorities."
)


def render() -> bytes:
    """Return the entry exactly as it must land on disk (no trailing newline)."""
    return ENTRY_TEXT.encode("utf-8")


def main() -> None:
    data = render()
    text = data.decode("utf-8")
    assert 1 <= len(text) <= 200 and text.strip(), "entry must be 1-200 chars"
    out = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(data)


if __name__ == "__main__":
    main()
