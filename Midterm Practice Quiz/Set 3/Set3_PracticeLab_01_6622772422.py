import math as m

circleDiameter = float(input("Input a circle diameter: "))
diameterUnit = input("Input a unit of the diameter: ")
outputAreaUnit = input("Input a unit of the output area: ")

## Check if Valid

if (circleDiameter >= 1) and (diameterUnit in ["cm", "in", "mm"]) and (outputAreaUnit in ["cm", "in", "mm"]):
    ## Change diameterUnit to mm (millimetre)
    if diameterUnit == "cm":
        circleDiameterInmm = circleDiameter * 10
    elif diameterUnit == "in":
        circleDiameterInmm = circleDiameter * 25.4
    else:
        circleDiameterInmm = circleDiameter

    ## Output Area Unit
    if outputAreaUnit == "cm":
        prefix = 0.1
    elif outputAreaUnit == "in":
        prefix = 1/25.4
    else:
        prefix = 1

    ## Calculations
    Area = (m.pi)*(((circleDiameterInmm/2))*prefix)**2

    print("The area of a circle with a %.2f %s diameter is %.2f square %s." % (circleDiameter, diameterUnit, Area, outputAreaUnit))

else:
    print("Invalid input")