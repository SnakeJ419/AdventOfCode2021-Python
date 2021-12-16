import Utils


def part_one():
    array = [line.strip('\n') for line in Utils.get_file_as_array('Inputs/Day13.txt')]
    i = 0
    points = set()
    instructions = []
    while array[i] != '':
        x, y = [int(s) for s in array[i].split(',')]
        points.add((x, y))
        i += 1
    i += 1
    for line in array[i:]:
        direction, value = line.split(' ')[2].split('=')
        instructions.append((direction, int(value)))
    points = fold(points, instructions[0])
    print(len(points))


def fold(points: set, instruction: tuple):
    direction, value = instruction
    new_points = []
    for point in points:
        if direction == 'x':
            new_points.append(((point[0] - 2*(point[0] - value)) if point[0] > value else point[0], point[1]))
        elif direction == 'y':
            new_points.append((point[0], (point[1] - 2*(point[1] - value)) if point[1] > value else point[1]))
    return set(new_points)


def part_two():
    array = [line.strip('\n') for line in Utils.get_file_as_array('Inputs/Day13.txt')]
    i = 0
    points = set()
    instructions = []
    while array[i] != '':
        x, y = [int(s) for s in array[i].split(',')]
        points.add((x, y))
        i += 1
    i += 1
    for line in array[i:]:
        direction, value = line.split(' ')[2].split('=')
        instructions.append((direction, int(value)))
    for intr in instructions:
        points = fold(points, intr)
    # points = fold(points, instructions[0])
    grid = []
    for i in range(max([point[1] for point in points])+3):
        grid.append(list([' '] * (max([point[0] for point in points]) + 3)))
    for point in points:
        grid[point[1]][point[0]] = '#'
    # grid.reverse()
    for line in grid:
        string = ''
        for c in line:
            string += c
        print(string)


# part_one()
part_two()
