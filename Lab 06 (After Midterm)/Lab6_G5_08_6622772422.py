stringOG = input("Enter a string: ")
newString = []

for x in stringOG:
    if x.islower():
        r = x.upper()
    else:
        r = x.lower()
    newString.append(r)

print("Reverse string output: ", end="")

for i in range(len(stringOG)):
    print(newString[i], end="")