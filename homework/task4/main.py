import math


def main(n):
    if n == 0:
        return 0.40
    elif n >= 1:
        return 1 + 80 * (math.log10(1 + 2*main(n-1) + main(n-1)**2)**3)

def call(n):
    return format(main(n), '.2e')


print(call(6))
print(call(2))
print(call(5))
print(call(7))
print(call(3))
