from commands import add_contact, change_contact, show_phone, show_all
from utils import parse_input

def main():
    """ The main function that starts an interactive loop to process user commands.
    """
    contacts = {}  # Dictionary for storing contacts
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")  # Reading a command from the user
        command, args = parse_input(user_input)  # Parsing the command

        # Response to commands
        if command in ["close", "exit"]:
            print("Good bye!")
            break  # Ending the program
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
