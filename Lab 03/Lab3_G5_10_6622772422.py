import math as m

area = float(input("Input the covered area for one paint bottle (cm square): "))
noSphere = int(input("Input the number of the spheres: "))
radius = float(input("Input the radius of each sphere (cm): "))
                       
surfaceArea = 4*m.pi*(radius**2)

bottleAns = m.ceil((surfaceArea*noSphere)/area)

print("The paint bottles are needed to paint the surface of spheres is %.0f." % bottleAns)
# print(f"The paint bottles are needed to paint the surface of spheres is {bottleAns}")