# This program gets the actual value of a property and returns the assessed value and property tax.
#import read
import read
''' Import read functions to read float. '''


def main():
    """ This function  executes the program. """
    actual_value = read.rfloat(
        "What is the actual value of the property?")
    print("The assessed value is: ${0:,.2f}".format(
        assessment_value(actual_value)))
    print("The property tax is: ${0:,.2f}".format(
        property_taxes(actual_value)))


def assessment_value(value):
    """This function calculates and returns the assessment value.

    Args:
        value (float): The actual value.

    Returns:
        float: The calcualted assessment value. 
    """
    return value * 0.6


def property_taxes(value):
    """This function calculates the property tax based on the actual value.

    Args:
        value (float): The actual value

    Returns:
        float: The property tax
    """
    return value * 0.072 * 0.6


main()  # Calls the execution of the program.
