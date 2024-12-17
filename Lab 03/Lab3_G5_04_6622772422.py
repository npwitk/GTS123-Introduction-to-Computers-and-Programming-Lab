import math as m

xp1 = input("Enter coordinate X for P1: ")
xp1 = float(xp1)
yp1 = input("Enter coordinate Y for P1: ")
yp1 = float(yp1)
xp2 = input("Enter coordinate X for P2: ")
xp2 = float(xp2)
yp2 = input("Enter coordinate Y for P2: ")
yp2 = float(yp2)

diameter = m.sqrt((xp1 - xp2)**2+(yp1 - yp2)**2)
area = m.pi*((diameter/2)**2)
circumference = m.pi*diameter

print("The length of the circle diameter is %.4f" % diameter)
print("The circle area and circumference are %.4f and %.4f" % (area, circumference))
