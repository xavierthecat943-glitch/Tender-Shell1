# Tender Shell input handler

import readline

from history import CommandHistory
from suggestions import SuggestionEngine


class TenderInput:
    def __init__(self, history):
        self.history = history
        self.suggestions = SuggestionEngine(history)

    def get_input(self, prompt):
        """Get input from the user."""

        return input(prompt)
