import Utils


class Node:

    def __init__(self, key: str):
        self.connections = []
        self.key = key

    def get_connections(self):
        return self.connections

    def add_connection(self, connection_key: str):
        self.connections.append(connection_key)


def get_paths(c_cave: Node, path_list: list, c_path: list, caves: dict):
    c_path.append(c_cave.key)
    if c_cave.key == 'end':
        path_list.append(c_path)
        return
    for cave_key in c_cave.get_connections():
        if cave_key.islower() and c_path.__contains__(cave_key):
            continue
        get_paths(caves[cave_key], path_list, c_path.copy(), caves)


def part_one():
    array = [line.strip('\n') for line in Utils.get_file_as_array('Inputs/Day12.txt')]
    caves: dict = {}
    for line in array:
        key1, key2 = line.split('-')
        if key1 not in caves:
            caves[key1] = Node(key1)
        if key2 not in caves:
            caves[key2] = Node(key2)
        caves[key1].add_connection(key2)
        caves[key2].add_connection(key1)
    path_list = []
    get_paths(caves['start'], path_list, [], caves)
    print(len(path_list))


def get_paths_small(c_cave: Node, path_list: list, c_path: list, caves: dict, two_small: bool):
    c_path.append(c_cave.key)
    if c_cave.key == 'end':
        path_list.append(c_path)
        return
    for cave_key in c_cave.get_connections():
        if cave_key.islower():
            if cave_key == 'start' or (c_path.__contains__(cave_key) and two_small):
                continue
            elif c_path.__contains__(cave_key):
                get_paths_small(caves[cave_key], path_list, c_path.copy(), caves, True)
                continue
        get_paths_small(caves[cave_key], path_list, c_path.copy(), caves, two_small)


def part_two():
    array = [line.strip('\n') for line in Utils.get_file_as_array('Inputs/Day12.txt')]
    caves: dict = {}
    for line in array:
        key1, key2 = line.split('-')
        if key1 not in caves:
            caves[key1] = Node(key1)
        if key2 not in caves:
            caves[key2] = Node(key2)
        caves[key1].add_connection(key2)
        caves[key2].add_connection(key1)
    path_list = []
    get_paths_small(caves['start'], path_list, [], caves, False)
    print(len(path_list))


part_one()
part_two()
