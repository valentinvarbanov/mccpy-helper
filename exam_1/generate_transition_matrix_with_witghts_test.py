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


import random

iterations = sum(weights) * 10000
count = numpy.zeros(size)
pos = 0
for i in range(iterations):
    new_pos = neighbors[pos][random.randint(0, 3)]
    if random.random() < matrix[pos][new_pos]:
        pos = new_pos
    count[pos] += 1

print(count)
print()
print(numpy.multiply(count,(1/10000)))
