# This program gets the length and width of two rectangles from the user.
# Then it tells the user which rectangle has the greater area or if the rectangles are the same.

def calculate_area(rectangle1, rectangle2):
    rectangle1_area = int(rectangle1[0]) * int(rectangle1[1])
    rectangle2_area = int(rectangle2[0]) * int(rectangle2[1])
    if rectangle1_area > rectangle2_area:
        return 1
    elif rectangle1_area == rectangle2_area:
        return 0
    else:
        return -1


rectangle1 = input("Enter the width and length of rectangle 1:\n>").split(" ")
rectangle2 = input("Enter the width and length of rectangle 2:\n>").split(" ")

calculated_area = calculate_area(rectangle1, rectangle2)


if calculated_area == 1:
    print("The area of rectangle 1 is greater than area if rectangle 2.\n")
elif calculated_area == 0:
    print("The rea of the rectangles is the same.\n")
else:
    print("The area of rectangle 2 is greater than the are of rectangle 1")
