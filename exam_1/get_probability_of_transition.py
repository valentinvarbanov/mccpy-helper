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


def probability(matrix, from_cell, to_cell, steps):

    multiplied = numpy.zeros((len(matrix), len(matrix)))
    numpy.fill_diagonal(multiplied, 1)

    for step in range(steps):
        multiplied = multiplied @ matrix

    return multiplied[from_cell][to_cell]

print(probability(matrix, 2, 4, 2))
print(probability(matrix, 2, 4, 3))
