def main(m, z, n):
    a = 0
    b = 0
    for i in range(1, m+1):
        a += (0.01 - (62 * i ** 2 - 90 * z)**3)

    for i in range(1, n+1):
        b += i**5 - i**2 - i**6

    return a + b



def call(m,z,n):
    return format(main(m,z,n), '.2e')


print(call(2, 0.21, 2))
print(call(5, -0.65, 5))
print(call(8, 0.36, 3))
print(call(5, 0.55, 6))
print(call(8, -0.57, 8))