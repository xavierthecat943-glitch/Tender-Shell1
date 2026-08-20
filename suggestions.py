# Tender Shell autosuggestions

from history import CommandHistory


class SuggestionEngine:
    def __init__(self, history):
        self.history = history

    def suggest(self, text):
        """Return the best matching previous command."""

        if not text.strip():
            return ""

        matches = self.history.search(text)

        if not matches:
            return ""

        return matches[-1]
