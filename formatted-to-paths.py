#!/usr/bin/env python3

"""
Input: Multiple lines as formatted by `raw-to-formatted.py`.

Output: Single line with " "-separated paths that were extracted from input. Special characters like `%20` are decoded.
"""

import fileinput
from urllib.parse import unquote

for i, line in enumerate(fileinput.input()):
    # Separate by whitespace
    if i != 0:
        print(" ", end='')

    _, path = line.rsplit(' ', 1)
    path = path.strip()
    path_unquoted = unquote(path)
    if path != path_unquoted:
        print("\"%s\"" % path_unquoted, end='')
    else:
        print("%s" % path_unquoted, end='')