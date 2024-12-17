data = {}
while True:   
    userInput = input("Input (DONE = exit): ")
    if userInput == "DONE":
        break
    else:
        a,b = userInput.split()

        if not a.isdigit() or not b.isdigit():
            print("Invalid input")
        else:
            a,b = int(a), int(b)
            if a not in data.keys() or data == {}:
                data[a] = b
            else:
                print("Duplicated ID")
                continue
u = sorted(data.values(), reverse = True)
print("output: ")
for i in u:
    for key, value in data.items():
        if i == value:
            print(key, value)