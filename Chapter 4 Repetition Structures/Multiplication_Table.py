# This program prints a multiplcation table from 1x to 12x

SIZE = 12

print("{0}".format("Mutliplication Table from 1x to 12x"))  # Print title.
print("     |", end="")  # Place holder for empty cell.

# Print first row of numbers.
for column in range(SIZE):
    print("{0:4d} |".format(column+1), end="")

print("")

# Iterates over number of total rows.
for row in range(SIZE):
    print("{0:4d} |".format(row+1), end="")  # Prints first column of numbers

    # Iterates over number total columns.
    for column in range(SIZE):
        product = column * (row + 1)
        # Prints product to next cell
        print("{0:4d} |".format(product), end="")
    print("")
