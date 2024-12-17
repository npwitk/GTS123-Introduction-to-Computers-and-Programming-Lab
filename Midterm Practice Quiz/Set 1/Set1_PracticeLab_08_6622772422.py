englishAlphabet = 'abcdefghijklmnopqrstuvwxyz'

firstChar = input("Give me a character: ")
secondChar = input("Give me another character: ")

if (firstChar in englishAlphabet) and (secondChar in englishAlphabet):
    ## Basic If-else Sorting

    if firstChar > secondChar:
        firstSortedChar = secondChar
        secondSortedChar = firstChar
    else:
        firstSortedChar = firstChar
        secondSortedChar = secondChar
    
    for x in range(ord(firstSortedChar), ord(secondSortedChar) + 1):
        char = chr(x)
        print(char, end='')

    ## Function ORD convert from normal character to ASCII number

else:
    print("You need to input two characters.")