## WOW THIS IDEA IS BONKERS!!

x = int(input("Input: "))
value = 1

if x >= 1 and x <= 15:
    if x == 1:
        print("1")
    else:
        for row in range(x):
            for column in range(x):
                if row < column: ## columm number less than row number then print "0"
                    print("0", end="\t")
                else:
                    print(value, end="\t")
                    value += 1
            print()
else:
    print("Invalid input")