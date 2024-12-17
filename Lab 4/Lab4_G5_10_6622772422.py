print("Welcome to Income Tax Computation Program")

income = float(input("Please enter your income (THB): "))

if income < 0:
    print("You are in debt!")
else:
    tax = 0
    if income <= 15000:
        tax = 0
    elif income <= 50000:
        tax = (income - 15000) * 0.05
    elif income <= 100000:
        tax = (35000 * 0.05) + (income - 50000) * 0.075
    else:
        tax = (35000 * 0.05) + (50000 * 0.075) + (income - 100000) * 0.1

    totalTaxExpense = tax

    print("Tax expense = %.2f" % totalTaxExpense)
    print("Your net income after tax = %.2f" % (income - totalTaxExpense))
