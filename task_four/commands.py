def add_contact(args, contacts):
    """ Adds a new contact to the dictionary. Checks for compliance with the command format.
    
    Args:
        args (list): a list of arguments, including name and phone number.
        contacts (dict): a dictionary that stores contacts.

    Returns:
        str: a message about the result of adding a contact.
    """
    if len(args) != 2:
        return "Invalid input. Please use: add [name] [phone]"
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    """ Modifies an existing contact in the dictionary. Checks for the existence of the contact and the format of the command.
    
    Args:
        args (list): a list of arguments, including name and new phone number.
        contacts (dict): a dictionary that stores contacts.

    Returns:
        str: a message about the contact being updated or not.
    """
    if len(args) != 2:
        return "Invalid input. Please use: change [name] [new phone]"
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        return "Contact not found."

def show_phone(args, contacts):
    """ Displays the phone number for the specified name. Checks the format and whether the contact exists.
    
    Args:
        args (list): a list of arguments, including the name.
        contacts (dict): a dictionary of contacts.

    Returns:
        str: phone number for the specified name or a message about its absence.
    """
    if len(args) != 1:
        return "Invalid input. Please use: phone [name]"
    name = args[0]
    if name in contacts:
        return f"{name}: {contacts[name]}"
    else:
        return "Contact not found."

def show_all(contacts):
    """ Prints all contacts in the form of a string representing a dictionary.
    
    Args:
        contacts (dict): a dictionary of contacts.

    Returns:
        str: a formatted representation of all contacts or a message about their absence.
    """
    if not contacts:
        return "No contacts stored."
    return '\n'.join([f"{name}: {phone}" for name, phone in contacts.items()])
