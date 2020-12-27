'''
    This program getse a number of days from the user and 
    prints out the salery earned over those days in pennies. 
'''

''' Named constants '''
total = 0.0
days = ""
pennies = 0.01

''' Reads input from user as an integer. '''
try:
    days = int(input("Enter the number of days:\n>"))
except:
    print("That is not a valid input.")

''' Prints header to the terminal '''
print("{0:^5s} | {1:^13s}".format("Day", "Pennies"))
print("----------------------")


''' Prints calculated salary over the number of days '''
for day in range(days):
    print("{0:5d} | {1:>13.2f}".format(day+1, pennies), end="")
    total = total + pennies
    pennies = pennies * 2
    print("")

''' Prints final total to terminal '''
print("Total: ${0:>13.2f}".format(total))
