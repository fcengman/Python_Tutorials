
budget = 0
expenses = 0
expenses_catagories = ["housing", "food", "transportation", "entertainment"]


while True:
    try:
        budget = abs(int(input("Enter your budget for the month:\n>")))
        break
    except:
        print("That is not a valid number.")


for catagory in expenses_catagories:
    while True:
        try:
            expenses = expenses + int(input("Enter your " +
                                            catagory + " expense for the month:\n>"))
            break
        except:
            print("That is not a valid number.")


budget_diff = budget - expenses

if budget_diff < 0:
    print("You are over budget by: $", abs(budget_diff))
elif budget_diff > 0:
    print("You are under budget by: $", budget_diff)
else:
    print("Your budgets is equal to your expenses.")
