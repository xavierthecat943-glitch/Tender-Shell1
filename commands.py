# Tender Shell built-in commands

BUILTIN_COMMANDS = {
    "help": "Show available Tender commands.",
    "about": "Show information about Tender Shell.",
    "hello": "Say hello to Tender.",
    "clear": "Clear the terminal.",
    "exit": "Exit Tender Shell.",
}


def show_help():
    print("\nTender Shell commands:")
    for command, description in BUILTIN_COMMANDS.items():
        print(f"  {command:<10} - {description}")
    print()


def show_about():
    print("\nTender Shell")
    print("A conversational Linux shell built for Tender OS.")
    print()
