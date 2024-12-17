import math as m

d = input("Enter the sphere diameter: ")
d = float(d)

r = d/2

print("The length of the sphere radius is %.4f" % r)

volume = (4/3)*m.pi*(r**3)
surfaceArea = 4*m.pi*(r**2)

print("The sphere volume and the surface area are %.4f and %.4f1" % (volume, surfaceArea))
