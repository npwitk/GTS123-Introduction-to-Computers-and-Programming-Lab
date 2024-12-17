a=input("Enter amount of melted chocolate to be poured into the cup (ml): ")
b=input("Enter amount of milk to be poured into the cup (ml): ")

a=int(a)
b=int(b)
c=a+b
c=float(c)
d=c*0.0338

print("Now Emmy's cup is filled with %.2f ml (or about %.2f oz) of chocolate milk." % (c,d))