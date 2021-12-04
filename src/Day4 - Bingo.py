import Utils


def part_one():
    array = Utils.get_file_as_array('Inputs/Day4.txt')
    called = [int(x) for x in array[0].split(',')]
    boards = []
    i = 2
    while i < len(array):
        new_board = []
        while i != len(array) and array[i] != '\n':
            new_board.append([int(s) for s in filter(''.__ne__, array[i].strip('\n').split(' '))])
            i += 1
        boards.append(new_board)
        i += 1
    for call in called:
        for board in range(len(boards)):
            for y in range(len(boards[board])):
                for x in range(len(boards[board][y])):
                    if boards[board][y][x] == call:
                        boards[board][y][x] = '*'
            counts = [y.count('*') for y in boards[board]]
            for x in range(len(boards[board][0])):
                counts.append(sum([1 if y[x] == '*' else 0 for y in boards[board]]))
            if counts.__contains__(5):
                score = sum([sum(filter('*'.__ne__, y)) for y in boards[board]])
                score *= call
                print(score)
                return


def part_two():
    array = Utils.get_file_as_array('Inputs/Day4.txt')
    called = [int(x) for x in array[0].split(',')]
    boards = []
    i = 2
    while i < len(array):
        new_board = []
        while i != len(array) and array[i] != '\n':
            new_board.append([int(s) for s in filter(''.__ne__, array[i].strip('\n').split(' '))])
            i += 1
        boards.append(new_board)
        i += 1

    loosers = [0] * len(boards)
    for call in called:
        for board in range(len(boards)):
            if loosers[board] == 1:
                continue
            for y in range(len(boards[board])):
                for x in range(len(boards[board][y])):
                    if boards[board][y][x] == call:
                        boards[board][y][x] = '*'
            counts = [y.count('*') for y in boards[board]]
            for x in range(len(boards[board][0])):
                counts.append(sum([1 if y[x] == '*' else 0 for y in boards[board]]))
            if counts.__contains__(5):
                if loosers.count(0) == 1:
                    score = sum([sum(filter('*'.__ne__, y)) for y in boards[board]])
                    score *= call
                    print(score)
                    return
                loosers[board] = 1


part_two()
