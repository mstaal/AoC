# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from utils import aoc_helper as helper, global_variables as glob
import numpy as np


def part1(content):
    low_point_dict = {}
    for idx in range(0, len(content)):
        for idy in range(0, len(content)):
            near_by = helper.get_neighbours_dict(content, idx, idy, directions=glob.cardinal_directions, ignore_none=True)
            if len(near_by) == len([k for k, v in near_by.items() if content[idx][idy] < v]):
                low_point_dict[(idx, idy)] = content[idx][idy]
    return low_point_dict


def part2(content, point, memory={}):
    adjacent_dict = helper.get_neighbours_dict(content, point[0], point[1], glob.cardinal_directions, True)
    basin = {k: v for k, v in adjacent_dict.items() if k not in memory.keys() and v < 9}
    memory.update(basin)
    temp = {}
    for key, value in basin.items():
        temp.update(part2(content, key, memory))
    basin.update(temp)
    return basin


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    content = [[int(number) for number in list(element)] for element in helper.splitFile("day9.txt", "\n")]
    content_dict = helper.to_2d_dict(content)
    low_point_dict = part1(content)
    risks = sum([element + 1 for element in low_point_dict.values()])

    res2 = [part2(content, element) for element in low_point_dict.keys()]
    result = np.prod(sorted([len(elm) for elm in res2])[-3:])
    hej = ""

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
