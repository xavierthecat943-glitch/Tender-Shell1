# Tender Shell tab completion

import os
import readline


def get_matches(text):
    """Find filesystem matches for the current input."""

    expanded = os.path.expanduser(text)

    directory = os.path.dirname(expanded)
    prefix = os.path.basename(expanded)

    if not directory:
        directory = "."

    try:
        entries = os.listdir(directory)
    except (FileNotFoundError, PermissionError):
        return []

    matches = []

    for entry in entries:
        if not entry.startswith(prefix):
            continue

        full_path = os.path.join(directory, entry)

        if os.path.isdir(full_path):
            matches.append(entry + "/")
        else:
            matches.append(entry)

    return sorted(matches)


def complete(text, state):
    """Provide filesystem completion."""

    line = readline.get_line_buffer()
    before_cursor = line[:readline.get_endidx()]

    # Complete paths after commands such as cd
    if before_cursor.startswith("cd "):
        path = before_cursor[3:].strip()
        matches = get_matches(path)

        if state < len(matches):
            match = matches[state]

            if path.startswith("~/"):
                return "~/"+match

            if path.startswith("/"):
                directory = os.path.dirname(path)
                if directory == "/":
                    return "/" + match
                return directory + "/" + match

            return match

        return None

    # Basic filesystem completion
    matches = get_matches(text)

    if state < len(matches):
        return matches[state]

    return None


def setup_completion():
    """Enable Tender tab completion."""

    readline.set_completer(complete)
    readline.parse_and_bind("tab: complete")# Tender Shell tab completion

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
