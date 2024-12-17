in_str = input("Input: ")

inValid = ""

for c in in_str:
    if len(in_str) != 9 or (c != "X" and c != "O" and c != "."):
        inValid = True

if inValid == True:
    print("Error")

else:
    print("-"*7)

    for row in range(3):
        print("|", end="")

        for col in range(3):
            print(in_str[row*3+col],end="|")

        print()
        print("-"*7)
        