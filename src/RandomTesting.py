
def avg_squares(array: list):
    return sum([x * x for x in array]) / len(array)


def string_to_ints(string: str):
    return [int(x) for x in string.split(',')]


def optionals(*a: int, b: int = 0, c: int = 0):
    print(f'{a}, {b}, {c}')


optionals()
# (), 0, 0
optionals(1, 2, 3)
# (1, 2, 3), 0, 0
optionals(1, b=2, c=3)
# (1), 2, 3
