import math as m

def myCylinder():
    radius = float(input("Enter the radius r of the cylinder: "))
    height = float(input("Enter the height h of the cylinder: "))

    Volume = (m.pi * (radius**2) * height)
    SurfaceArea = (2 * m.pi * radius * height) + (2 * m.pi * (radius**2))

    return Volume, SurfaceArea

v,a = myCylinder()
print("The volume is %.2f and the surface area is %.2f" % (v, a))