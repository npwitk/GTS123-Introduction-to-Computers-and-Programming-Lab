## VERY CHALLENGING

import random as r

recWidth = int(input("Rectangle width: "))
recHeight = int(input("Rectangle height: "))
borderThickness = int(input("Border thickness: "))

randomArray = ["#", "*", "$"]

for row in range(recHeight):
    for column in range(recWidth):
        if (row < borderThickness or row >= recHeight - borderThickness) or (column < borderThickness or column >= recWidth - borderThickness):
            print(r.choice(randomArray), end="")
        else:
            print(" ", end="")
    print("")