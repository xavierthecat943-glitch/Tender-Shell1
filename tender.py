from config import TENDER_NAME, PROMPT_USER, PROMPT_SYMBOL
from parser import parse_input
from conversation import respond
from executor import execute
from commands import show_help, show_about


def clear_screen():
    print("\033[2J\033[H", end="")


def main():
    print(f"Welcome to {TENDER_NAME} Shell!")
    print("Type 'help' for help or 'exit' to leave.\n")

    while True:
        try:
            user_input = input(
                f"{PROMPT_USER}@home ~ {PROMPT_SYMBOL} "
            )

            parsed = parse_input(user_input)

            if parsed["type"] == "empty":
                continue

            if parsed["type"] == "conversation":
                print(f"{TENDER_NAME}: {respond(parsed['command'])}")

            elif parsed["type"] == "tender":
                command = parsed["command"]

                if command == "exit":
                    print("Goodbye! 👋")
                    break

                elif command == "help":
                    show_help()

                elif command == "about":
                    show_about()

                elif command == "clear":
                    clear_screen()

                else:
                    print(f"{TENDER_NAME}: I don't know that command yet.")

            elif parsed["type"] == "linux":
                execute(parsed["command"])

        except KeyboardInterrupt:
            print("\nTender: Use 'exit' to leave.")

        except EOFError:
            print("\nGoodbye! 👋")
            break


if __name__ == "__main__":
    main()
