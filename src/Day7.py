import Utils
import statistics
from collections import Counter


def part_one():
    array = [int(s) for s in Utils.get_file_as_array('Inputs/Day7.txt')[0].split(',')]
    avg = statistics.median(array)
    fuel = 0
    for e in array:
        fuel += abs(avg - e)
    print(fuel)


def part_two():
    array = [int(s) for s in Utils.get_file_as_array('Inputs/Day7.txt')[0].split(',')]

    fuel = 0
    counts = [0] * (max(array)+1)
    print(f'max: {max(array)}')
    for i in range(max(array)+1):
        print(i)
        for e in array:
            counts[i] += sum([x+1 for x in range(abs(i-e))])
    print(min(counts))

part_one()
part_two()
