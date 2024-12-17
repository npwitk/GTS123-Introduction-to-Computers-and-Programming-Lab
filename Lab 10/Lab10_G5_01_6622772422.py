import numpy as np

matrixSize = int(input("Input size of matrix: "))
matrix = np.zeros((matrixSize, matrixSize))

for i in range(matrixSize):
    for j in range(matrixSize):
        matrix[i, j] = float(input("Input element at row %s column %s: "%(i+1,j+1)))

print("Matrix =")
print(matrix)

det = np.linalg.det(matrix)
inverseMatrix = np.linalg.inv(matrix)

print("Determinant =", det)
print("Inverse matrix =")
print(inverseMatrix)
