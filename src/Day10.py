import math

import Utils


def part_one():
    array = Utils.get_file_as_array('Inputs/Day10.txt')
    count = 0
    for line in array:
        line = line.strip('\n')
        count += check_line(line)
    print(count)


def check_line(line: str):
    problems = []
    for c in line:
        if c == '(' or c == '[' or c == '{' or c == '<':
            problems += c
        else:
            cc = get_closing(problems[len(problems) - 1])
            if c == cc:
                problems.__delitem__(len(problems) - 1)
            else:
                print(c)
                return get_value(c)
    return 0


def get_closing(c: str):
    if c == '(':
        return ')'
    elif c == '[':
        return ']'
    elif c == '{':
        return '}'
    elif c == '<':
        return '>'


def get_value(c: str):
    if c == ')':
        return 3
    elif c == ']':
        return 57
    elif c == '}':
        return 1197
    elif c == '>':
        return 25137


def part_two():
    array = Utils.get_file_as_array('Inputs/Day10.txt')
    counts = []
    for line in array:
        line = line.strip('\n')
        if check_line(line) != 0:
            continue
        completion = []
        for c in line:
            if c == '(' or c == '[' or c == '{' or c == '<':
                completion.append(c)
            else:
                completion.pop(len(completion)-1)
        count = 0
        completion.reverse()
        for c in completion:
            count *= 5
            count += simple_value(c)
        counts.append(count)
    counts.sort()
    print(len(counts))
    print(counts)
    print(counts[math.floor(len(counts)/2)])


def simple_value(c: str):
    if c == '(':
        return 1
    elif c == '[':
        return 2
    elif c == '{':
        return 3
    else:
        return 4


def is_incomplete(line: str):
    count = 0
    for c in line:
        if c == '(' or c == '[' or c == '{' or c == '<':
            count += 1
        else:
            count -= 1
    return count != 0

part_two()
