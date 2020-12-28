# This program asks the user for integer values equal to the number of bugs they've collected over a series of days.
# It calculates and returns the total number of bugs collected.

# Tries to read and resolve user input.
try:
    bugs_collected = input(
        "Enter the number of bugs collected over five days:\n>").split(",")
    total = 0
    for bugs in bugs_collected:
        total = total + int(bugs)  # Calculates total number of bugs collected.

    print("You collected " + str(total) +
          " bugs over " + str(len(bugs_collected)) + " days.")  # Prints message to terminal.

except:
    print("That is not a valid input")
