userLine = int(input("Enter No. of lines: "))

for x in range(1, userLine+1):
    if x % 2 == 0:
        print("*" * x)
    else:
        print("-"* x)