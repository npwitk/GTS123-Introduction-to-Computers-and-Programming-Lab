specialChar = input("Enter a special character: ")
patternSize = int(input("Enter the size of the pattern: "))
patternOption = int(input("Enter option for the pattern: "))

setSpecialCharacters = "#$@*^"

if (specialChar in setSpecialCharacters) and (patternOption == 1 or patternOption == 2) and (patternSize >= 1):
    
    if patternOption == 1:
    
        for column in range(patternSize):
            for row in range(patternSize):
                if column == row:
                    print(specialChar,end="")
                else:
                    print(".",end="")
            print("")
    
    else:

        for column in range(patternSize):
            for row in range(patternSize):
                if row + column == patternSize - 1:
                    print(specialChar,end="")
                else:
                    print(".",end="")
            print("")

else:
    print("Wrong input values.")