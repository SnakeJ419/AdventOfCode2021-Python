import Utils


def part_one():
    array = Utils.get_file_as_array('Inputs/Day3.txt')
    tracker: list = [0] * 12
    total_lines = 0
    for line in array:
        total_lines += 1
        split = [x for x in line]
        print(split)
        tracker[0] += int(split[0])
        tracker[1] += int(split[1])
        tracker[2] += int(split[2])
        tracker[3] += int(split[3])
        tracker[4] += int(split[4])
        tracker[5] += int(split[5])
        tracker[6] += int(split[6])
        tracker[7] += int(split[7])
        tracker[8] += int(split[8])
        tracker[9] += int(split[9])
        tracker[10] += int(split[10])
        tracker[11] += int(split[11])

    gamma: str = ''
    epsilon: str = ''
    for elm in tracker:
        if elm > total_lines/2:
            gamma += str(1)
            epsilon += str(0)
        else:
            gamma += str(0)
            epsilon += str(1)
    gamma_val = int(gamma, 2)
    epsilon_val = int(epsilon, 2)
    print(gamma_val * epsilon_val)


def part_two():
    array = Utils.get_file_as_array('Inputs/Day3.txt')
    tracker: list = [0] * 12
    total_lines = 0
    for line in array:
        total_lines += 1
        split = [x for x in line]
        tracker[0] += int(split[0])
        tracker[1] += int(split[1])
        tracker[2] += int(split[2])
        tracker[3] += int(split[3])
        tracker[4] += int(split[4])
        tracker[5] += int(split[5])
        tracker[6] += int(split[6])
        tracker[7] += int(split[7])
        tracker[8] += int(split[8])
        tracker[9] += int(split[9])
        tracker[10] += int(split[10])
        tracker[11] += int(split[11])

    ox_lines = array.copy()
    counter = 0
    while len(ox_lines) != 1:
        tracker = [0] * 12
        total_lines = 0
        for line in ox_lines:
            total_lines += 1
            split = [x for x in line]
            tracker[0] += int(split[0])
            tracker[1] += int(split[1])
            tracker[2] += int(split[2])
            tracker[3] += int(split[3])
            tracker[4] += int(split[4])
            tracker[5] += int(split[5])
            tracker[6] += int(split[6])
            tracker[7] += int(split[7])
            tracker[8] += int(split[8])
            tracker[9] += int(split[9])
            tracker[10] += int(split[10])
            tracker[11] += int(split[11])

        common = 1 if tracker[counter] >= total_lines/2 else 0
        i = 0
        new_list = []
        for elm in ox_lines:
            split = [x for x in elm]
            if int(split[counter]) == common:
                new_list.append(elm)
            i += 1
        ox_lines = new_list.copy()
        counter += 1

    carb_lines = array.copy()
    counter = 0
    while len(carb_lines) != 1:
        tracker = [0] * 12
        total_lines = 0
        for line in carb_lines:
            total_lines += 1
            split = [x for x in line]
            tracker[0] += int(split[0])
            tracker[1] += int(split[1])
            tracker[2] += int(split[2])
            tracker[3] += int(split[3])
            tracker[4] += int(split[4])
            tracker[5] += int(split[5])
            tracker[6] += int(split[6])
            tracker[7] += int(split[7])
            tracker[8] += int(split[8])
            tracker[9] += int(split[9])
            tracker[10] += int(split[10])
            tracker[11] += int(split[11])

        common = 1 if tracker[counter] >= total_lines / 2 else 0
        i = 0
        new_list = []
        for elm in carb_lines:
            split = [x for x in elm]
            if int(split[counter]) != common:
                new_list.append(elm)
            i += 1
        carb_lines = new_list.copy()
        counter += 1
    print(int(ox_lines[0], 2) * int(carb_lines[0], 2))


part_two()
