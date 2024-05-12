def parse_input(user_input):
    """ Parses a user input string into a command and arguments.
    
    Args:
        user_input (str): user input.

    Returns:
        tuple: the first element is a command, the second is a list of arguments.
    """
    parts = user_input.strip().split()
    command = parts[0].lower() if parts else ''
    args = parts[1:]
    return command, args
