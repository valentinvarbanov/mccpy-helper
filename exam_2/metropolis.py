#!/usr/bin/env python3
import numpy as np
import random

should_test = False
# should_test = True
num_iterations = 100000

def calcualte_metropolis_hastigs(neighbors, weights, probabilities):

    def inverse_dir(dir):
        # clockwise -> right down left up
        return (dir + 2) % 4

    size = len(neighbors)

    matrix = np.zeros((size, size))
    for cell in range(size):
        for direction in range(4):
            neighboring_cell = neighbors[cell][direction]
            transfer_rate = weights[neighboring_cell] / weights[cell]

            # correction for non-uniform
            transfer_rate *= (probabilities[inverse_dir(direction)] / probabilities[direction])

            if (transfer_rate >= 1):
                # low weight to high
                matrix[cell][neighboring_cell] += probabilities[direction]
            else:
                # we are going from high weight to low one
                success_transfer = probabilities[direction] * transfer_rate
                matrix[cell][neighboring_cell] += success_transfer
                matrix[cell][cell] += probabilities[direction] - success_transfer

    return matrix

def calculate_static(input_list):
    input = np.array(input_list)
    return input / sum(input)

def verify_matrix(neighbors, matrix):
    iterations = sum(weights) * num_iterations
    count = np.zeros(len(matrix[0]))
    pos = 0
    for i in range(iterations):
        new_pos = neighbors[pos][random.randint(0, 3)]
        if random.random() < matrix[pos][new_pos]:
            pos = new_pos
        count[pos] += 1

    return count

# right down left up
neighbors = [
    [0, 0, 0, 1], # 0
    [3, 0, 1, 2], # 1
    [2, 1, 2, 2], # 2
    [4, 3, 1, 3], # 3
    [4, 4, 3, 5], # 4
    [5, 4, 5, 5]  # 5
]
weights = [
    7,  # cell 0
    5,  # cell 1
    4,  # cell 2
    1,  # ...
    5,
    7
]

# right down left up
probabilities = [0.25, 0.25, 0.25, 0.25] # equal directions

# right down left up
probabilities_hastigs = [0.2, 0.2, 0.1, 0.5]

matrix         = calcualte_metropolis_hastigs(neighbors, weights, probabilities)
matrix_hastigs = calcualte_metropolis_hastigs(neighbors, weights, probabilities_hastigs)

static_vec = calculate_static(weights)

print('metropolis:')
print(matrix)
print()

print('metropolis-hastigs:')
print(matrix_hastigs)
print()

print('static:')
print(static_vec)
print()

if should_test:

    results = verify_matrix(neighbors, matrix)
    results_hastigs = verify_matrix(neighbors, matrix_hastigs)

    print('metorpolis-test:')
    print(results)
    print(results / num_iterations)
    print()

    print('metorpolis-hastigs-test:')
    print(results_hastigs)
    print(results_hastigs / num_iterations)
    print()

    print(static_vec)
    print(calculate_static(results))
    print(calculate_static(results_hastigs))
