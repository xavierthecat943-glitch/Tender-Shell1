# Tender Shell conversation system

from responses import RESPONSES, DEFAULT_RESPONSE


def respond(message):
    """Generate a basic Tender response."""

    message = message.strip().lower()

    if message in RESPONSES:
        return RESPONSES[message]

    return DEFAULT_RESPONSE
