#!/usr/bin/env python3

import numpy

# right down left up
neighbor = [
    [2, 0, 0, 1],
    [1, 0, 1, 1],
    [3, 2, 0, 2],
    [3, 3, 2, 4],
    [4, 3, 4, 5],
    [5, 4, 5, 5]
]
# right down left up -> must match the order above
probabilities = [0.2, 0.2, 0.1, 0.5]

size = len(neighbor)

matrix = numpy.zeros((size, size))
for row in range(size):
    for direction in range(4):
        neighboring_cell = neighbor[row][direction]
        matrix[row][neighboring_cell] += probabilities[direction]

print("matrix:")
print(matrix)

print()
print()


eigenvalues, eigenvectors = numpy.linalg.eig(matrix)

print("values:")
print(eigenvalues)
print("vectors:")
print(eigenvectors)

#TBD: do we need to transpose ???


print()
print()

print("transposed:")
matrix_t = matrix.transpose() # not sure if needed
eigenvalues, eigenvectors = numpy.linalg.eig(matrix_t)

print("values:")
print(eigenvalues)
print("vectors:")
print(eigenvectors)
