print("""welcome to pizza online ordering.
please input "y" if you want to order, otherwise input \"n\"""")
      
totalPrice = 0

pizza = input("pizza? (price_359): ")
if pizza == 'y':
    totalPrice = totalPrice + 359

chicken = input("chicken? (price_3 pieces for 199): ")
if chicken == 'y':
    totalPrice = totalPrice + 199

pasta = input("pizza? (price_99): ")
if pasta == 'y':
    totalPrice = totalPrice + 99

salad = input("salad? (price_99): ")
if salad == 'y':
    totalPrice = totalPrice + 99

coke = input("coke? (price_550 ml for 25): ")
if coke == 'y':
    totalPrice = totalPrice + 25

print(f"""total price is {totalPrice}
thanks""")