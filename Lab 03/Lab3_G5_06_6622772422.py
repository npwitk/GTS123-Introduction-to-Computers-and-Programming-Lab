import math as m

d=int(input("Enter the distance to the building: "))
a=int(input("Enter the elevation angle in degree: "))

h=d*m.tan(m.radians(a))

print("The building height is %.4f" % h)
