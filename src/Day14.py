import Utils
import time
from textwrap import wrap
from multiprocessing import Pool
from multiprocessing import freeze_support


def part_one():
    array = [line.strip('\n') for line in Utils.get_file_as_array('Inputs/Day14.txt')]
    sequence = array[0]
    rules = {}
    for line in array[2:]:
        key, insert = line.split(' -> ')
        rules[key] = insert
    for l in range(10):
        new_sequence = ''
        for i in range(len(sequence)-1):
            new_sequence += sequence[i]
            s = sequence[i] + sequence[i+1]
            if s in rules:
                new_sequence += rules[s]
        new_sequence += sequence[len(sequence)-1]
        sequence = new_sequence
    print(set(rules.values()))
    values = [sequence.count(c) for c in set(rules.values())]
    print(max(values) - min(values))


def run_multiprocessing(func, n_processors, args: list):
    with Pool(processes=n_processors) as pool:
        return pool.map(func, args)


def multi_process(args: tuple):
    return process(args[0], args[1], args[2])


def process(sequence: str, rules: dict, loops: int):
    if loops == 0:
        results = {}
        for c in set(rules.values()):
            results[c] = 0
        for c in sequence:
            results[c] += 1
        return results

    if len(sequence) > 100000:
        splits = wrap(sequence, 8000)
        extras = [(splits[i][len(splits[i])-1] + splits[i+1][0]) for i in range(len(splits)-1)]
        splits += extras
        split_results = []  # type: list
        if __name__ == '__main__':
            args = []
            for split in splits:
                args.append((split, rules, loops))
            split_results = run_multiprocessing(multi_process, 24, args)
        else:
            for split in splits:
                split_results.append(process(split, rules, loops))

        results = {}
        for c in set(split_results[0].keys()):
            results[c] = 0
            for result in split_results:
                results[c] += result[c]
        for extra in extras:
            for c in extra:
                results[c] -= 1
        return results

    new_sequence = ''
    for i in range(len(sequence) - 1):
        new_sequence += sequence[i]
        s = sequence[i] + sequence[i + 1]
        if s in rules:
            new_sequence += rules[s]
    new_sequence += sequence[len(sequence) - 1]
    return process(new_sequence, rules, loops-1)


def part_two():
    array = [line.strip('\n') for line in Utils.get_file_as_array('Inputs/Day14.txt')]
    sequence = array[0]
    rules = {}
    def_pairs = {}
    for line in array[2:]:
        key, insert = line.split(' -> ')
        rules[key] = insert
    for pair in set(rules.keys()):
        def_pairs[pair] = 0
    pairs = def_pairs.copy()
    for i in range(len(sequence)-1):
        pairs[sequence[i] + sequence[i+1]] += 1
    results = {}
    for c in set(rules.values()):
        results[c] = 0
    for c in sequence:
        results[c] += 1
    for i in range(40):
        new_pairs = def_pairs.copy()
        for key in pairs.keys():
            replacement = rules[key]
            results[replacement] += pairs[key]
            new_pairs[key[0] + replacement] += pairs[key]
            new_pairs[replacement + key[1]] += pairs[key]
        pairs = new_pairs.copy()
    print(max(results.values()) - min(results.values()))


if __name__ == "__main__":
    freeze_support()
    start_time = time.time()
    part_two()
    print('Ran In %s seconds' % (time.time() - start_time))
