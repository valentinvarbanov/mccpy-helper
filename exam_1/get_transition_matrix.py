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


print(matrix)

print()

import fractions

def float_to_fraction(number):
    fraction_number = fractions.Fraction(number).limit_denominator()
    return str(fraction_number)

float_to_fraction_matrix = numpy.vectorize(float_to_fraction)

matrix_fractions = float_to_fraction_matrix(matrix)

print(matrix_fractions)
