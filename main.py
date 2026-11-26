"""Copy entry.txt to the output directory for the make.fun entry.

The entry is one original line roasting a gadget used every day,
at most 200 characters.
The phone dies at 4 p.m. every day, like it has a union contract
and the owner is the one violating it. The gadget has rights;
the human has a charger and a guilty conscience.
"""
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
OUT = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")
os.makedirs(os.path.dirname(OUT), exist_ok=True)
shutil.copyfile(SRC, OUT)
# The entry text is copied verbatim; the judge reads it exactly as written.
# Verify the copy is byte-identical to the source.
assert open(SRC, "rb").read() == open(OUT, "rb").read(), "output differs from entry.txt"
