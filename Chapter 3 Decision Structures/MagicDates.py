# This program gets an integer value for a year, month, and day.
# If the month times the day equals the year, it displays a message telling the user that
# the date is magic.

# Begins inifinte loop until program can be completed.
while True:
    try:
        # Get day from the user
        day = int(input("Enter a numeric value for day:\n>"))
        # Checks for valid day input.
        if day < 0 or day > 31:
            print("That is not a valid day.\n")
            continue  # restart loop if day invalid.

        # Get month from the user
        month = int(input("Enter a numeric value for month:\n>"))
        # Checks for valid month input.
        if month < 0 or month > 12:
            print("That is not a valid month.\n")
            continue  # restart loop if month invalid.

        # Get year from the user
        year = int(input("Enter a two digit numeric value for year:\n>"))
        # Checks for valid year input.
        if year < 0 or year > 99:
            print("That is not a valid year.\n")
            continue  # restart loop if year invalid.

        day_times_month = day * month  # Store the product of day times month

        # Returns statement to terminal.
        if day_times_month == year:
            print("This is a magic date.")
            break
        else:
            print("This is not a magic date.")
            break

    except:
        print("That is not a valid number.")
