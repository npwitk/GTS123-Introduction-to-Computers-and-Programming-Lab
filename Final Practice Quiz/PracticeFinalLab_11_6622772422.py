animalDick = {}

while True:
    userInput = input("Input: ")
    if userInput == "done":
        break
    else:
        name, amount = userInput.split()
        amount = int(amount)
        if name in animalDick:
            animalDick[name] += amount
        else:
            animalDick[name] = amount

print("###Summary###")
if animalDick == {}:
    print("Empty List")
else:
    for key, value in animalDick.items():
        print("Total Number of %s : %d" % (key, value))