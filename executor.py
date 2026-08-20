# Tender Shell command executor

import os
import subprocess


def change_directory(path):
    """Change Tender's current working directory."""

    try:
        if not path:
            path = os.path.expanduser("~")
        else:
            path = os.path.expanduser(path)

        os.chdir(path)
        return True

    except FileNotFoundError:
        print("Tender: Directory not found.")
    except NotADirectoryError:
        print("Tender: Not a directory.")
    except PermissionError:
        print("Tender: Permission denied.")

    return False


def execute(command):
    """Execute a normal Linux command."""

    try:
        result = subprocess.run(
            command,
            shell=True,
            text=True,
        )

        return result.returncode

    except Exception as error:
        print(f"Tender: Could not execute command: {error}")
        return 1
