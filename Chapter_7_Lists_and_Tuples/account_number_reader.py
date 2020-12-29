import read_user_input as read


def read_account_numbers():
    infile = open("account_numbers.txt", "r")
    list = []
    while True:
        infile_line = infile.readline()
        if infile_line != "":
            list.append(infile_line.rstrip("\n"))
        else:
            return list


def get_account_number():
    while True:
        user_input = read.rint("Enter a 7 didgit account number:")
        if user_input < 1000000 or user_input > 9999999:
            print("That is not a valid account number.\n")
        else:
            return user_input


def check_account_number(list, user_input):
    for account in list:
        if int(account) == user_input:
            return True

    return False


def main():
    list = read_account_numbers()
    user_input = get_account_number()
    if check_account_number(list, user_input):
        print("The number is valid.")
    else:
        print("The number is not valid.")


main()
