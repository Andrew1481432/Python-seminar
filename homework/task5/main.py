import math


def main(x, y):
    result = 0

    n = len(x)
    y.insert(0, 0)
    x.insert(0, 0)
    for i in range(1, n+1):
        result += (y[math.ceil(i / 2)]**2 - 1 - x[n + 1 - i]**3) ** 4 / 62

    return result

print(format(main(
    [-0.43, -0.53, 0.84],
    [-0.03, 0.71, 0.37]
), '.2e'))

print(format(main(
    [0.84, -0.72, 0.97],
    [-0.16, 0.54, -0.11]
), '.2e'))

print(format(main(
    [-0.7, -0.46, -0.03],
    [0.18, -0.15, 0.51]
), '.2e'))

print(format(main(
    [0.68, 0.68, -0.79],
    [0.09, -0.77, -0.66],
), '.2e'))

print(format(main(
    [0.97, -0.48, 0.29],
    [0.39, 0.96, -0.95],
), '.2e'))