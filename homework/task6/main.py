def zero(items, left, right):
    if items[0] == 2007:
        return left
    if items[0] == 1966:
        return right


def four(items, left, right):
    if items[4] == 'RAGEL':
        return left
    elif items[4] == 'JOKE':
        return right


def three(items, left, middle, right):
    if items[3] == 1957:
        return left
    elif items[3] == 1971:
        return middle
    elif items[3] == 2003:
        return right


def two(items, left, right):
    if items[2] == 'SMT':
        return left
    if items[2] == 'ASP':
        return right


def one(items, left, middle, right):
    if items[1] == 'WISP':
        return left
    elif items[1] == 'SQL':
        return middle
    elif items[1] == 'KICAD':
        return right


def main(items):
    return one(
        items,
        three(
            items,
            two(items, zero(items, 0, 1), four(items, 2, 3)),
            4,
            zero(items, two(items, 5, 6), two(items, 7, 8))
        ),
        zero(items, 9, 10),
        11)


print(main([2007, 'KICAD', 'SMT', 1971, 'IOKE']))
print(main([2007, 'WISP', 'SMT', 1957, 'RAGEL']))
print(main([2007, 'WISP', 'SMT', 2003, 'RAGEL']))
print(main([2007, 'SQL', 'SMT', 1957, 'IOKE']))
print(main([1966, 'SQL', 'ASP', 2003, 'IOKE']))