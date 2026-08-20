# Tender Shell command executor

import subprocess


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
