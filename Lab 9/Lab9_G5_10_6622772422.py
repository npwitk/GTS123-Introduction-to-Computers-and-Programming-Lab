import math as m

def SquareArea():
    length = float(input("Enter the length: "))
    area = length**2
    return area


def CircleArea():
    radius = float(input("Enter the radius: "))
    area = m.pi * (radius**2)
    return area

userChoice = input("Do you want to find the area of a square (s) or a circle (c)?: ")

if userChoice == "s":
    sqaureArea = SquareArea()
    print("The area of the square is %.2f" % sqaureArea)

elif userChoice == "c":
    circleArea = CircleArea()
    print("The area of the circle is %.2f" % circleArea)
else:
    print("Wrong Input")