# Tender Shell tab completion

import os
import readline


def complete_path(text, state):
    """Complete filesystem paths."""

    expanded = os.path.expanduser(text)

    if os.path.isdir(expanded):
        directory = expanded
        prefix = ""
    else:
        directory = os.path.dirname(expanded) or "."
        prefix = os.path.basename(expanded)

    try:
        entries = os.listdir(directory)
    except (FileNotFoundError, PermissionError):
        return None

    matches = []

    for entry in entries:
        if entry.startswith(prefix):
            full_path = os.path.join(directory, entry)

            if os.path.isdir(full_path):
                matches.append(entry + "/")
            else:
                matches.append(entry)

    matches.sort()

    try:
        return matches[state]
    except IndexError:
        return None


def setup_completion():
    """Enable Tender's tab completion."""

    readline.set_completer(complete_path)
    readline.parse_and_bind("tab: complete")
