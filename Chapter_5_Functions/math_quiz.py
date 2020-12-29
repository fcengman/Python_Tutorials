# This program gives the user two integers and an operator and asks for the answer.
# It checks the answer and returns a message to the user.
# The game continues until the user enters a 0.


import random
import read_user_input as read


def generate_random_operator():
    """This function generates a random operator.

    Returns:
        str: An operator represeneted as a string.
    """
    num = random.randint(
        1, 4)  # Get a random number between 1 and 4. Each number represents an operator.
    if num == 1:
        return "+"
    elif num == 2:
        return "-"
    elif num == 3:
        return "*"
    else:
        return "/"


def get_question():
    """This function generates and returns two random numbers between 1 and 100.

    Returns:
        float: Two random numbers
    """
    num1 = float(random.randint(1, 100))
    num2 = float(random.randint(1, 100))
    return num1, num2


def print_question(num1, num2, operator):
    """This function prints the question to the terminal.

    Args:
        num1 (float): A random number.
        num2 (float): A random number.
        operator (str): A operator represented as a string.
    """
    print("{0:>4.0f}".format(num1))
    print("{0} {1:>2.0f}".format(operator, num2))


def calculate_answer(num1, num2, operator):
    """This function calculates the correct answer based on the operator.

    Args:
        num1 (float): A random number.
        num2 (float): A random number.
        operator (str): A operator represented as a string.

    Returns:
        float: The calculated answer.
    """
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    else:
        # Round the division to two decimal places.
        return round(num1 / num2, 2)


def check_answer(calc_answer, user_answer):
    """This function checks the calculated answer against the user's answer.

    Args:
        calc_answer (float): The calculated answer.
        user_answer (float): The user's answer.

    Returns:
        bool: A bool based on if the answers match.
    """
    if calc_answer == user_answer:
        return True
    else:
        return False


def main():
    """This function executes the program."""
    continue_game = True

    """Begins game loop"""
    while continue_game:

        """Gets question variables."""
        num1, num2 = get_question()
        operator = generate_random_operator()

        print_question(num1, num2, operator)
        user_answer = read.rfloat("Answer:")
        calc_answer = calculate_answer(num1, num2, operator)
        if check_answer(calc_answer, user_answer):
            print("That is correct!")
        elif user_answer == 0:
            print("Goodbye")
            continue_game = False
        else:
            print("Not quite right. The answer was: {0:4.2}".format(
                calc_answer))


main()
