# This program asks the user for a numer in the range of 1 through 7.
# The program should display the corresponding day of the week.
# day_of_the_week = int(input("Enter a number in the range of 1 through 7\n>"))

message = "The day of the week is"

while True:
    try:
        day_of_the_week = int(
            input("Enter a number in the range of 1 through 7:\n>"))
        if day_of_the_week == 0:
            break
        elif day_of_the_week == 1:
            print(message, "Monday\n")
        elif day_of_the_week == 2:
            print(message, "Tuesday\n")
        elif day_of_the_week == 3:
            print(message, "Wednesday\n")
        elif day_of_the_week == 4:
            print(message, "Thursday\n")
        elif day_of_the_week == 5:
            print(message, "Friday\n")
        elif day_of_the_week == 6:
            print(message, "Saturday\n")
        elif day_of_the_week == 4:
            print(message, "Sunday\n")
        else:
            print("That is not a valid number.\n")

    except:
        print("That is not a valid input.\n")
