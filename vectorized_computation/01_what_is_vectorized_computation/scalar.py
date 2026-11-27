""" 
Scalar Computation: sequentially performed in sequence
"""

values = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

result = []

for value in values:
    result.append(value * 2)

print(result)


