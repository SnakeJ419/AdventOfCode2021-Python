import Utils


def part_one():
    array = Utils.get_file_as_array('Inputs/Day2.txt')
    x = 0
    y = 0
    for line in array:
        pieces = line.split(' ')
        identifier = pieces[0]
        amount = int(pieces[1])
        if identifier == 'forward':
            x += amount
        elif identifier == 'up':
            y -= amount
        else:
            y += amount
    print(x * y)


def part_two():
    array = Utils.get_file_as_array('Inputs/Day2.txt')
    aim = 0
    x = 0
    y = 0
    for line in array:
        pieces = line.split(' ')
        identifier = pieces[0]
        amount = int(pieces[1])
        if identifier == 'forward':
            x += amount
            y += aim * amount
        elif identifier == 'up':
            aim -= amount
        else:
            aim += amount
    print(x * y)


part_two()
