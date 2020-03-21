#!/usr/bin/env python3

"""
Input: Lines from a GTK-3.0 bookmarks file, typically located at `~/.config/gtk-3.0/bookmarks`

Output: The script filters the directories/files, i.e. the lines that start with `file://` (or those that do not declare a protocol) and then transforms them into a user-friendly format, with terminal colors.
"""

import fileinput
from termcolor import colored

rows = []
max_name_len = 0

# Read line by line, extract only file bookmarks (`file://` protocol) or bookmarks that don't have a protocol (which are assumed to be just paths)
for line in fileinput.input():
    uri, name = line.split(' ', 1)
    name = name.strip()
    uri_parts = uri.split('://', 1)
    if len(uri_parts) == 2:
        protocol = uri_parts[0]
        path = uri_parts[1]
        if protocol == 'file':
            rows.append((path, name))
            max_name_len = max(max_name_len, len(name))
    else:
        rows.append((uri, name))
        max_name_len = max(max_name_len, len(name))

# Output rows
for (path, name) in rows:
    name_formatted = colored(name.rjust(max_name_len), 'white')
    path_formatted = colored(path, 'cyan')
    output = '%s : %s' % (name_formatted, path_formatted)
    print(output)