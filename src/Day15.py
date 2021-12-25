import Utils
import time


class Cell:
    def __init__(self, pose: tuple, travel_cost: int):
        self.cost: int = None
        self.parent: Cell = None
        self.pose: tuple = pose
        self.x, self.y = pose
        self.edge = True
        self.travel_cost = travel_cost

    def get_travel_cost(self):
        return self.travel_cost

    def set_edge(self, edge: bool):
        self.edge = edge

    def get_edge(self):
        return self.edge

    def set_cost(self, cost: int):
        self.cost = cost

    def get_cost(self):
        return self.cost

    def set_parent(self, parent):
        self.parent = parent

    def get_parent(self):
        return self.parent

    def calc_path(self):
        if self.parent is not None:
            return self.parent.calc_path().append(self)
        return [self]


def get_tup(pos: tuple, array: list):
    return array[pos[1]][pos[0]]


def find_min_edge(path_grid: list):
    min_cell: Cell = None
    for row in path_grid:
        for cell in row:
            if (cell.get_cost() is None) or (not cell.get_edge()):
                continue

            if min_cell is None:
                min_cell = cell
            elif cell.get_cost() < min_cell.get_cost():
                min_cell = cell
    return min_cell


def is_cheaper(new_cell: Cell, direc: tuple, path_grid: list):
    max_x = len(path_grid[0])-1
    max_y = len(path_grid)-1
    new_pos = add(new_cell.pose, direc)
    if new_pos[0] < 0 or new_pos[1] < 0 or new_pos[0] > max_x or new_pos[1] > max_y:
        # if cell does not exist return false
        return False

    old_cell: Cell = get_tup(new_pos, path_grid)

    # if the cell does not have a value then the new one is the cheapest path to it
    if old_cell.get_cost() is None:
        return True

    # if the old path to reach the cell is cheaper or equal return false, else return true
    return (new_cell.get_cost() + old_cell.get_travel_cost()) < old_cell.get_cost()


def add(one: tuple, two: tuple):
    return (one[0] + two[0]), (one[1] + two[1])


# dictionary of the directions that neighbors are in to make looping easier
directions = {'u': (0, -1), 'r': (1, 0), 'd': (0, 1), 'l': (-1, 0)}


def recalc_neighbors(parent: Cell, path_grid: list):
    for direc in directions.keys():
        if is_cheaper(parent, directions[direc], path_grid):
            cell: Cell = get_tup(add(parent.pose, directions[direc]), path_grid)
            if cell.get_cost() is None:
                continue
            # if cost is not currently uncalculated apply new cheaper cost and recursively check its neighbors as well
            cell.set_parent(parent)
            cell.set_cost(parent.get_cost() + cell.get_travel_cost())
            recalc_neighbors(cell, path_grid)


def part_one():
    array = Utils.get_file_as_array('Inputs/Day15.txt')
    grid = [[int(c) for c in line.strip('\n')] for line in array]
    # maze will continue to be solved until the end is reached
    # maintain a grid of the cheapest discovered path to reach any position
    # from whatever the current cheapest 'edge' (has not been pathed from yet) position is calculate the cost to reach
    # its neighbors
    # if this path leads to a position that does not yet have a value, assign it a value and tell it who its parent is
    # tell the cell before this one in the path that this is its child
    # if calculating the cost to a cell that already has a cost assigned to it, compare the new cost with the current
    # cost, if the new cost is greater than or equal to the old cost do nothing. Else give the cell a new cost to reach
    # and reassign its parent to the cell along the new path. For every child of this cell recalculate its cost to reach
    # recursively do this for the children of the children
    #
    # Scratch that, when a cells value gets updated it should check all the cells around it, if the path to get to one
    # of them is now cheaper that cell should have its cost and parent updated then have the same process recursively
    # applied, this process should not be applied to unexplored cells
    max_x = len(grid[0])-1
    max_y = len(grid)-1

    path_grid = []
    for y in range(max_y+1):
        row = []
        for x in range(max_x+1):
            row.append(Cell((x, y), grid[y][x]))
        path_grid.append(row.copy())
    path_grid[0][0].set_cost(0)

    while path_grid[max_y][max_x].get_cost() is None:
        # get the current cheapest edge cell
        min_edge = find_min_edge(path_grid)
        # print(f'Pos: {min_edge.pose} Cost: {min_edge.get_cost()}')
        min_edge.set_edge(False)

        # calculate new potential neighbor costs
        for direc in directions.keys():
            # only change anything about the cell being compared to if this is a cheaper route
            if is_cheaper(min_edge, directions[direc], path_grid):
                # get the cell that a new path is being given to
                cell: Cell = get_tup(add(min_edge.pose, directions[direc]), path_grid)
                cell.set_parent(min_edge)
                # if the neighbor did not previously have a value there is no need to check neighbors
                if cell.get_cost() is None:
                    cell.set_cost(min_edge.get_cost() + cell.get_travel_cost())
                else:
                    cell.set_cost(min_edge.get_cost() + cell.get_travel_cost())
                    recalc_neighbors(cell, path_grid)
    print(path_grid[max_y][max_x].get_cost())


def convert(i: int):
    if i > 9:
        return convert(i-9)
    return i


def part_two():
    array = Utils.get_file_as_array('Inputs/Day15.txt')
    grid = [[int(c) for c in line.strip('\n')] for line in array]
    big_grid = []
    for i in range(5):
        for row in grid:
            big_row = []
            for j in range(5):
                for e in row:
                    big_row.append(convert(e+i+j))
            big_grid.append(big_row.copy())
    grid = big_grid

    max_x = len(grid[0])-1
    max_y = len(grid)-1

    path_grid = []
    for y in range(max_y+1):
        row = []
        for x in range(max_x+1):
            row.append(Cell((x, y), grid[y][x]))
        path_grid.append(row.copy())
    path_grid[0][0].set_cost(0)

    while path_grid[max_y][max_x].get_cost() is None:
        # get the current cheapest edge cell
        min_edge = find_min_edge(path_grid)
        # print(f'Pos: {min_edge.pose} Cost: {min_edge.get_cost()}')
        min_edge.set_edge(False)

        # calculate new potential neighbor costs
        for direc in directions.keys():
            # only change anything about the cell being compared to if this is a cheaper route
            if is_cheaper(min_edge, directions[direc], path_grid):
                # get the cell that a new path is being given to
                cell: Cell = get_tup(add(min_edge.pose, directions[direc]), path_grid)
                cell.set_parent(min_edge)
                # if the neighbor did not previously have a value there is no need to check neighbors
                if cell.get_cost() is None:
                    cell.set_cost(min_edge.get_cost() + cell.get_travel_cost())
                else:
                    cell.set_cost(min_edge.get_cost() + cell.get_travel_cost())
                    recalc_neighbors(cell, path_grid)
    print(path_grid[max_y][max_x].get_cost())


start_time = time.time()
part_two()
print('Ran In %s seconds' % (time.time() - start_time))