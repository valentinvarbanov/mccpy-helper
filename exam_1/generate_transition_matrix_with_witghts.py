#!/usr/bin/env python3

import numpy

# right down left up
neighbors = [
    [2, 0, 0, 1],
    [1, 0, 1, 1],
    [3, 2, 0, 2],
    [3, 3, 2, 4],
    [4, 3, 4, 5],
    [5, 4, 5, 5]
]
weights = [
    5,   # cell 0
    10,  # cell 1
    5,   # cell 2
    10,  # ...
    25,
    60
]

probabilities = [0.25, 0.25, 0.25, 0.25] # equal directions

size = len(neighbors)

matrix = numpy.zeros((size, size))
for cell in range(size):
    for direction in range(4):
        neighboring_cell = neighbors[cell][direction]
        transfer_rate = weights[neighboring_cell] / weights[cell]
        if (transfer_rate >= 1):
            # low weight to high
            matrix[cell][neighboring_cell] += probabilities[direction]
        else:
            # we are going from high weight to low one
            success_transfer = probabilities[direction] * transfer_rate
            matrix[cell][neighboring_cell] += success_transfer
            matrix[cell][cell] += probabilities[direction] - success_transfer


print(matrix)

print()

import fractions

def float_to_fraction(number):
    fraction_number = fractions.Fraction(number).limit_denominator()
    return str(fraction_number)

float_to_fraction_matrix = numpy.vectorize(float_to_fraction)

matrix_fractions = float_to_fraction_matrix(matrix)

print(matrix_fractions)
