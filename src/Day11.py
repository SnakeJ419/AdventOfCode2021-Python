import Utils


def part_one():
    grid = [[int(c) for c in line.strip('\n')] for line in Utils.get_file_as_array('Inputs/Day11.txt')]
    count = 0
    synced = False
    i = 0
    while not synced:
        i+=1
        grid = [[e+1 for e in row] for row in grid]
        complete = False
        while not complete:
            complete = True
            for y in range(len(grid)):
                for x in range(len(grid[y])):
                    if grid[y][x] > 9:
                        print(f'{x}, {y}')
                        count += 1
                        complete = False
                        grid[y][x] = 0
                        if x > 0 and y > 0:
                            flash(grid, (y-1, x-1))
                        if y > 0:
                            flash(grid, (y-1, x))
                        if x < len(grid[0])-1 and y > 0:
                            flash(grid, (y-1, x+1))
                        if x < len(grid[0])-1:
                            flash(grid, (y, x+1))
                        if x < len(grid[0])-1 and y < len(grid)-1:
                            flash(grid, (y+1, x+1))
                        if y < len(grid)-1:
                            flash(grid, (y+1, x))
                        if x > 0 and y < len(grid)-1:
                            flash(grid, (y+1, x-1))
                        if x > 0:
                            flash(grid, (y, x-1))
        if sum([sum(row) for row in grid]) == 0:
            synced = True
    print(i)


def flash(grid: list, coord: tuple):
    if grid[coord[0]][coord[1]] != 0:
        grid[coord[0]][coord[1]] += 1


part_one()
