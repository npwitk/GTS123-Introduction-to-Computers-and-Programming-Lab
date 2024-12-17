iceWidth = float(input("Enter the width of the cube: "))
containerWidth = float(input("Enter the width of the cube: "))
containerHeight = float(input("Enter the height of the cube: "))
containerDepth = float(input("Enter the depth of the cube: "))
                       
a = containerWidth//iceWidth
b = containerHeight//iceWidth
c = containerDepth//iceWidth

answer = a*b*c

print("The number of cubes that can fit into the container is %.0f." % answer)