import math as m

x = input("Input a positive number: ")

if float(x) > 0:
    x = float(x)
else:
    print("Wrong Input")
    exit()

def CirArea(r):
    circleArea = m.pi*(r**2)
    print("The area of the circle is %.2f" % circleArea)

def SqArea(b):
    squareArea = b**2
    print("The area of the sqaure is %.2f" % squareArea)

CirArea(x)
SqArea(x)