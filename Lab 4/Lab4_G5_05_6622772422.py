amountWD = int(input("Please specify amount of money you would like to withdraw: "))

bill500 = (amountWD//500)
amountWD2 = amountWD-(bill500*500)

bill100 = (amountWD2//100)
amountWD3 = amountWD2-(bill100*100)

bill50 = (amountWD3//50)
amountWD4 = amountWD3-(bill50*50)

coin2 = (amountWD4//2)
amountWD5 = amountWD4-(coin2*2)

coin1 = (amountWD5//1)

print(f"""We may give you:
{bill500} bill(s) of 500 baht
{bill100} bill(s) of 100 baht
{bill50} bill(s) of 50 baht
{coin2} coin(s) of 2 baht
{coin1} coin(s) of 1 baht
      """)