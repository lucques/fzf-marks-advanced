#!/usr/bin/env python3

"""
Input: The bookmark file, the name, the path.

Update the bookmark in the bookmark file if already present or insert it if not.
"""

import os
from urllib.parse import quote
import argparse

parser = argparse.ArgumentParser(description='Save bookmark.')
parser.add_argument('bookmark_file', type=str, nargs=1)
parser.add_argument('name', type=str, nargs=1)
parser.add_argument('path', type=str, nargs=1)

args = parser.parse_args()

name = args.name[0]
path = quote(args.path[0])
bookmark_file = args.bookmark_file[0]
new_line = path + ' ' + name + '\n'

with open(bookmark_file, 'r+') as f:
    lines = f.readlines()
    f.seek(0)

    overridden = False

    for line in lines:
        if line.startswith(path):
            f.write(new_line)
            overridden = True
        else:
            f.write(line)

    if not overridden:
        f.write(new_line)

    f.truncate()