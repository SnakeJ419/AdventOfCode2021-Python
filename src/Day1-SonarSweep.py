
def part_one():
    count = -1
    with open('Inputs/Day1.txt', 'r') as file:
        line = file.readline()
        last_depth = -1
        while line:
            depth = float(line)
            if depth > last_depth:
                count += 1
            last_depth = depth
            line = file.readline()
    print(count)


def part_two():
    count = -1
    with open('Inputs/Day1.txt', 'r') as file:
        line = file.readline()
        last = -1
        window = [0]
        while line:
            depth = float(line)
            window.insert(0, depth)
            if len(window) < 4:
                line = file.readline()
                continue
            window.__delitem__(3)
            window_sum = sum(window)
            if window_sum > last:
                count += 1
            last = window_sum
            line = file.readline()
    print(count)


part_two()
