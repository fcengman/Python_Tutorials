
import random as rd
list = []
for account in range(20):
    list.append(rd.randint(1000000, 9999999))

outfile = open("account_numbers.txt", "w")
for account in list:
    outfile.write(str(account) + "\n")

outfile.close()
print("The file has been written.")
