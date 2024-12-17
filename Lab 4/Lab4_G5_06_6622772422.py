x1,y1 = input("Please enter x1,y1: ").split(",")
x2,y2 = input("Please enter x2,y2: ").split(",")
x3,y3 = input("Please enter x3,y3: ").split(",")

x,y = input("Please enter x,y: ").split(",")

x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)
x3 = float(x3)
y3 = float(y3)

x = float(x)
y = float(y)

alpha = (((y2-y3)*(x-x3))+((x3-x2)*(y-y3)))/(((y2-y3)*(x1-x3))+((x3-x2)*(y1-y3)))
beta = (((y3-y1)*(x-x3))+((x1-x3)*(y-y3)))/(((y2-y3)*(x1-x3))+((x3-x2)*(y1-y3)))
gamma = 1 - alpha - beta

if alpha > 0 and beta > 0 and gamma > 0:
    print("Point (x,y) inside polygon")
else:
    print("Point (x,y) outside polygon")