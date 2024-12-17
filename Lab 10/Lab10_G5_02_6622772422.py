import numpy as np

matrix = np.zeros((3, 4), dtype=int)

for i in range(1, 13):
    matrix[(i - 1) // 4, (i - 1) % 4] = int(input("Input C%s: " % i))

# print("Matrix:")
# print(matrix)

coefficient_matrix = matrix[:, :3]
constants_matrix = matrix[:, 3].reshape(3, 1)

# print("Coefficient Matrix:")
# print(coefficient_matrix)
# print("Constants Matrix:")
# print(constants_matrix)

try:
    invCoefficientMatrix = np.linalg.inv(coefficient_matrix)
    ans = np.matmul(invCoefficientMatrix, constants_matrix)

    print("Solution:")
    print("x = %.2f" % ans[0, 0])
    print("y = %.2f" % ans[1, 0])
    print("z = %.2f" % ans[2, 0])

except np.linalg.LinAlgError: ##ถ้ามันหาไม่ได้
    print("Unable to find a solution.") 