# Tender Shell command history

class CommandHistory:
    def __init__(self):
        self.commands = []

    def add(self, command):
        """Add a command to history."""
        command = command.strip()

        if command:
            self.commands.append(command)

    def get_all(self):
        """Return all stored commands."""
        return self.commands.copy()

    def get_last(self):
        """Return the most recent command."""
        if not self.commands:
            return None

        return self.commands[-1]

    def search(self, text):
        """Find previous commands that start with the given text."""
        text = text.strip().lower()

        return [
            command
            for command in self.commands
            if command.lower().startswith(text)
        ]
