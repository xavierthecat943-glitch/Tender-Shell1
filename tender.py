import subprocess


def main():
    print("Welcome to Tender Shell!")
    print("Type 'exit' to leave.\n")

    while True:
        try:
            command = input("tender@home ~ $ ")

            if command == "exit":
                print("Goodbye! 👋")
                break

            if not command.strip():
                continue

            if command.lower() in ["hello", "hi", "hey"]:
                print("Tender: Hey! 👋")
                continue

            subprocess.run(command, shell=True)

        except KeyboardInterrupt:
            print("\nTender: Use 'exit' to leave.")
        except EOFError:
            print("\nGoodbye! 👋")
            break


if __name__ == "__main__":
    main()
