from math import pi

# squares = list(map(lambda x: x**2, range(10)))
squares = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]

vec = [-10, -4, 0, 4, 16]

print(squares)

print([(x, x*2) for x in vec])

# print([round(pi, i) for i in range(1, 6)])

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]
print([[row[i] for row in matrix] for i in range(4)])

print(list(zip(*matrix)))
