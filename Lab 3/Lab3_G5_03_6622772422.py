import math as m

height = input("Enter the pentagon height: ")
height = float(height)

a = (2*height)/(m.sqrt(5+2*(m.sqrt(5))))
A = ((a**2)*(m.sqrt(25+(10)*(m.sqrt(5)))))/(4)
para = 5*a

print("The length for one side of the pentagon is %.4f" % a)
print("The pentagon area and perimeter are %.4f and %.4f" % (A, para))