print("Multiplication table: ")
maeArai = int(input("Please enter a number between 1 to 25: "))

if maeArai >= 1 and maeArai <= 25:
    print(f"Multiplication table of {maeArai}:")
    for x in range(1, 13):
        print(str(maeArai) + " x " + str(x) + " = ", end="")
        print(maeArai * x)
else:
    print("You entered in valid number.")