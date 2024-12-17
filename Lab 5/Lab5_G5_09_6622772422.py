height = int(input("Height: "))
dotCount = 1
if height >= 1:
    for hashCount in range(height-1, -1, -1):
        print("#" * hashCount, end="")
        print("." * dotCount, end="")
        print("#" * hashCount)
        dotCount += 2
else:
    print("Error")
