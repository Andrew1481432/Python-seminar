import math


def main(y):
    if y < 103:
        return 76 * ((y**3)/70+78*y)**5
    elif 103 <= y < 125:
        a = math.floor(y**2-y-87)
        return (math.exp(y)**2) + a**5
    elif 125 <= y:
        return (y**3*48)**3


def call(y):
    return format(main(y), '.2e')


print(call(141))
print(call(211))
print(call(177))
print(call(56))
print(call(197))
