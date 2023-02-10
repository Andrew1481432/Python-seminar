import math


def main(x, y):
    a = math.sqrt((y + ((x ** 2) / 9) + x ** 3) ** 5)

    b = (30 * (y ** 2) - (y / 11)) ** 3 + math.exp(x) ** 2
    c = math.floor(64 + 15 * (x ** 3) + y ** 2) ** 7
    d = math.sqrt(b / c)
    return a - d


def call(x, y):
    return format(main(x, y), '.2e')


print(call(0.27, 0.35))
print(call(-0.36, 0.33))
print(call(0.33, 0.45))
print(call(-0.13, 0.01))
print(call(-0.83, 0.78))
