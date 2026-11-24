#!/usr/bin/env python3
"""Entry for make.fun’s “The One-Line Laugh” bounty.

Copy entry.txt into the output directory the harness sets.
"""

import os

HERE = os.path.dirname(os.path.abspath(__file__))


def emit_entry(out_dir):
    """Write the entry file into out_dir, byte for byte.

    The copy is done by hand in chunks so the bytes land exactly as
    stored: no newline translation, nothing appended at the end.
    """
    src_path = os.path.join(HERE, "entry.txt")
    dst_path = os.path.join(out_dir, "entry.txt")
    with open(src_path, "rb") as fin, open(dst_path, "wb") as fout:
        while True:
            chunk = fin.read(65536)
            if not chunk:
                break
            fout.write(chunk)
    return dst_path


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    emit_entry(out_dir)


if __name__ == "__main__":
    main()
