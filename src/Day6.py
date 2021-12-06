import Utils
import time


def part_one():
    array = Utils.get_file_as_array('Inputs/Day6.txt')
    sim_array = [0 for i in range(9)]
    for s in array[0].split(','):
        sim_array[int(s)] += 1
    print(sim_array)

    for i in range(256):
        temp_array = [0] * 9
        for e in range(len(sim_array)):
            if e == 0:
                temp_array[6] += sim_array[0]
                temp_array[8] += sim_array[0]
            else:
                temp_array[e-1] += sim_array[e]
        sim_array = temp_array.copy()
    print(sum(sim_array))


start_time = time.time()
part_one()
print('Ran In %s seconds' % (time.time() - start_time))
