import Utils


def part_one():
    array = Utils.get_file_as_array('Inputs/Day5.txt')
    course_map = [[0] * 1000 for x in range(1000)]
    coords_list = [[[int(i) for i in c.split(',')]for c in line.split(' -> ')] for line in array]
    for coords in coords_list:
        y1, x1 = coords[0]
        y2, x2 = coords[1]
        if x1 == x2:
            for i in range(abs(y1-y2)+1):
                course_map[x1][min(y1, y2) + i] += 1
        elif y1 == y2:
            for i in range(abs(x1-x2)+1):
                course_map[min(x1, x2) + i][y1] += 1
    summed = sum([sum([1 if x > 1 else 0 for x in y]) for y in course_map])
    print(summed)


def part_two():
    array = Utils.get_file_as_array('Inputs/Day5.txt')
    course_map = [[0] * 1000 for x in range(1000)]
    coords_list = [[[int(i) for i in c.split(',')] for c in line.split(' -> ')] for line in array]
    for coords in coords_list:
        y1, x1 = coords[0]
        y2, x2 = coords[1]
        if x1 == x2:
            for i in range(abs(y1 - y2) + 1):
                course_map[x1][min(y1, y2) + i] += 1
        elif y1 == y2:
            for i in range(abs(x1 - x2) + 1):
                course_map[min(x1, x2) + i][y1] += 1
        else:
            for i in range(abs(x1 - x2)+1):
                course_map[(x1-i) if x1>x2 else (x1+i)][(y1-i) if y1>y2 else (y1+i)] += 1

    summed = sum([sum([1 if x > 1 else 0 for x in y]) for y in course_map])
    print(summed)


part_one()
part_two()
