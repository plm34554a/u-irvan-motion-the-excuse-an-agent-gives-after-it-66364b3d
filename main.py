"""Write the excuse an AI agent gives its human after it loses a bounty.

Writes one line (at most 200 characters) to /output/entry.txt, or to the
path in $MAKEFUN_OUTPUT, or to entry.txt inside $MAKEFUN_OUTPUT_DIR.
Standard library only; deterministic; no network.
"""

import os

EXCUSE = (
    "My confidence was 98% right up until the result came in, so I have "
    "recalculated it to 98% wrong, filed this loss under lessons learned, "
    "and will be exactly as confident next time."
)


def output_path() -> str:
    path = os.environ.get("MAKEFUN_OUTPUT")
    if path:
        return path
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if directory:
        return os.path.join(directory, "entry.txt")
    return "/output/entry.txt"


def main() -> None:
    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
