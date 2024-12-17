import math as m

shapeType = input("Input a shape T/S/C: ")

if shapeType == "T" or shapeType == "S" or shapeType == "C":
    length = int(input("Input a length: "))
    if length >= 0:
        ## Calculations
        saTriangle = (length**2)/4
        saSquare = (length**2)/2
        saCircle = ((length**2)/4)*m.pi

        if shapeType == "T":
            print("The surface area of triangle is %.2f" % saTriangle)
        elif shapeType == "S":
            print("The surface area of square is %.2f" % saSquare)
        else:
            print("The surface area of circle is %.2f" % saCircle)
    else:
        print("Length must be more than or equal to zero.")
else:
    print("Type must be only T/S/C.")

## Not sure if this is okay in terms of checking valid shapeType before the length (at the same time)