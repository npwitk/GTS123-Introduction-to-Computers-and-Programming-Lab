inputText = input("Input: ")

for x in inputText:
    if x.isnumeric():
        x = int(x)
        column = 1
        for y in range(0,x):
            if column % 3 == 0:
                print("#", end="")
            else:
                print("*", end="")
            column += 1
        print("\n")