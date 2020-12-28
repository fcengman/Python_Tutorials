# This module is used to read and validate input from the terminal.


def rint(text):
    """
    This function is used to validated an integer input from the user.

    Parameters:
        text (string): A string to be printed to the terminal.

    Returns:
        user_input (int): A validated integer value from the user.
    """
    while True:
        try:
            user_input = int(
                input(text + "\n>").replace(" ", "").replace(",", ""))
            break
        except:
            print("That is not a valid integer.")
    return user_input


def rstring(text):
    """
    This function is used to validated an string input from the user.

    Parameters:
        text (string): A string to be printed to the terminal.

    Returns:
        user_input (str): A validated string value from the user.
    """
    user_input = "input"
    while user_input != " " or user_input != "":
        user_input = input(text + "\n>")
    return user_input


def rfloat(text):
    """
    This function is used to validated an string input from the user.

    Parameters:
        text (string): A string to be printed to the terminal.

    Returns:
        user_input (float): A validated float value from the user.
    """
    while True:
        try:
            user_input = float(
                input(text + "\n>").replace(" ", "").replace(",", ""))
            break
        except:
            print("That is not a valid float.")
    return user_input
