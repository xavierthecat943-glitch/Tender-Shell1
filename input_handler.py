# Tender Shell input handler

import readline

from suggestions import SuggestionEngine


class TenderInput:
    def __init__(self, history):
        self.history = history
        self.suggestions = SuggestionEngine(history)

        self._setup_readline()

    def _setup_readline(self):
        """Configure readline for command history."""

        readline.parse_and_bind("set enable-keypad on")

    def get_input(self, prompt):
        """Get input from the user and save it to Tender history."""

        command = input(prompt)

        if command.strip():
            self.history.add(command)

        return command
