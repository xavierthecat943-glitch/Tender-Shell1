# Tender Shell command parser


def parse_input(user_input):
    """
    Determine what kind of input the user entered.
    """

    command = user_input.strip()

    if not command:
        return {
            "type": "empty",
            "command": "",
        }

    if command.lower() in ["hello", "hi", "hey", "thanks", "thank you", "bye"]:
        return {
            "type": "conversation",
            "command": command.lower(),
        }

    if command.lower() in ["help", "about", "clear", "exit"]:
        return {
            "type": "tender",
            "command": command.lower(),
        }

    return {
        "type": "linux",
        "command": command,
    }
