import numpy as np

def distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2)**2))

def find_longest_distance(p1, p2, p3):
    distances = [distance(p1, p2), distance(p2, p3), distance(p3, p1)]
    longest_distance = max(distances)
    return longest_distance

x1, y1, z1 = [float(coord) for coord in input("Input coordinate of P1 (x y z): ").split()]
x2, y2, z2 = [float(coord) for coord in input("Input coordinate of P2 (x y z): ").split()]
x3, y3, z3 = [float(coord) for coord in input("Input coordinate of P3 (x y z): ").split()]

p1 = np.array([x1, y1, z1])
p2 = np.array([x2, y2, z2])
p3 = np.array([x3, y3, z3])

longest_distance = find_longest_distance(p1, p2, p3)

print("The longest distance = %.2f" % longest_distance)