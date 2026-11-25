import os
import sys
from pathlib import Path

LIMIT = 200
NAME = "entry.txt"


def step_validate(data: bytes) -> str:
    text = data.decode("utf-8").strip()
    if len(text) < 1 or len(text) > LIMIT:
        sys.exit(f"gate violation: {len(text)} characters")
    return text


def step_publish(text: str) -> Path:
    outdir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "out")
    outdir.mkdir(parents=True, exist_ok=True)
    path = outdir / NAME
    path.write_bytes(text.encode("utf-8"))
    return path


def main() -> int:
    src = Path(__file__).resolve().parent / NAME
    text = step_validate(src.read_bytes())
    dest = step_publish(text)
    print(f"ok {len(text)}/{LIMIT} chars -> {dest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
