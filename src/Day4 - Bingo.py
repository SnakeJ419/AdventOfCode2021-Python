import Utils
import numpy as np


def part_one():
    array = Utils.get_file_as_array('Inputs/Day4.txt')
    called = [int(x) for x in array.pop(0).split(',')]
    boards = [[[int(x) for x in filter(''.__ne__, y.strip('\n').split(' '))] for y in b] for b in [[list(filter('\n'.__ne__, array))[l*5 + n] for n in range(5)] for l in range(int(len(list(filter('\n'.__ne__, array)))/5))]]
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
    called = [int(x) for x in array.pop(0).split(',')]
    boards = [[[int(x) for x in filter(''.__ne__, y.strip('\n').split(' '))] for y in b] for b in [[list(filter('\n'.__ne__, array))[l * 5 + n] for n in range(5)] for l in range(int(len(list(filter('\n'.__ne__, array))) / 5))]]

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
