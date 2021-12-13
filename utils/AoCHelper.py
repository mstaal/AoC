# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math

import pandas as pd
from functools import reduce
import numpy as np
import copy as cc
from itertools import permutations, combinations, chain, product
from utils.GlobalVariables import all_directions


def prod(ints):
    p = 1
    for i in ints:
        p *= int(i)
    return p


def to_2d_dict(array):
    return {(idx, idy): array[idx][idy] for idx in range(0, len(array)) for idy in range(0, len(array[0]))}


def to_3d_dict(array):
    return {(idx, idy, idz): array[idx][idy][idz] for idx in range(0, len(array)) for idy in range(0, len(array[0]))
            for idz in range(0, len(array[0][0]))}


def rot_points_90(points, as_tuple=False):
    result = np.array(points).dot([[0, 1], [-1, 0]])
    if as_tuple:
        return tuple(result)
    return result


def rot_points_90_clockwise(points, as_tuple=False):
    result = np.array(points).dot([[0, -1], [1, 0]])
    if as_tuple:
        return tuple(result)
    return result


def reflect_points_x(points, as_tuple=False):
    result = np.array(points).dot([[1, 0], [0, -1]])
    if as_tuple:
        return tuple(result)
    return result


def reflect_points_y(points, as_tuple=False):
    result = np.array(points).dot([[-1, 0], [0, 1]])
    if as_tuple:
        return tuple(result)
    return result


def get_neighbours(coll, i, j, directions=all_directions, ignore_none=False, characters_to_skip=[], radius=1):
    adjacent_material = {}
    for x, y in [(x * radius, y * radius) for x, y in directions]:
        if 0 <= i + x < len(coll) and 0 <= j + y < len(coll[0]):
            element = coll[i + x][j + y]
            if element not in characters_to_skip:
                adjacent_material[(i + x, j + y)] = coll[i + x][j + y]
        elif not ignore_none:
            adjacent_material[(i + x, j + y)] = None
    return adjacent_material


def adjac_helper(ele, sub=[]):
    if not ele:
        yield sub
    else:
        yield from [idx for j in range(ele[0] - 1, ele[0] + 2)
                    for idx in adjac_helper(ele[1:], sub + [j])]


def adjacent(element):
    adjacent = set([tuple(element) for element in list(adjac_helper(element))])
    adjacent.remove(element)
    return adjacent


def depth(lst):
    depth = lambda L: isinstance(L, list) and max(map(depth, L)) + 1
    return depth(lst)


def csvToStringList(filename, sep):
    return list(map(lambda x: str(x[0]), pd.read_csv(filename, sep, header=None).values))


def csvToIntList(filename, sep):
    return list(map(lambda x: int(x[0]), pd.read_csv(filename, sep, header=None).values))


def csvToList(filename, sep):
    return list(map(lambda x: x[0], pd.read_csv(filename, sep, header=None).values))


def csvCommaToList(filename):
    return list(map(lambda x: x, pd.read_csv(filename, ",", header=None).values[0]))


def csvCommaToIntList(filename):
    return list(map(lambda x: int(x), pd.read_csv(filename, ",", header=None).values[0]))


def stringIndexLoop(text, index):
    return divmod(index, len(text))[1]


def splitFile(file, sep):
    with open(file) as file:
        content = list(file.read().split(sep))
    return content


def binaryParse(word, letter):
    number = 0
    for idx, val in enumerate(str(word)):
        factor = 2 ** (len(word) - 1 - idx)
        number = number + factor if str(val) == str(letter) else number
    return number


def contains_any(element, condition_collection):
    return any(element.__contains__(sub) for sub in condition_collection)


def flatten(lst):
    return [item for sublist in lst for item in sublist]


def reverse_dict(dictionary):
    return {value: key for key, value in dictionary.items()}


def baseToBinary(number, base=16):
    return bin(int(str(number), base))[2:]


def baseToHex(number, base=2):
    return hex(int(number, base))


def baseToBase10(number, base=2):
    return int(str(number), base)


def combi(collection, repeat):
    return [list(x) for x in product(collection, repeat=repeat)]


def gcdExtended(a, b):
    # Base Case
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcdExtended(b % a, a)
    # Update x and y using results of recursive call
    x = y1 - (b // a) * x1
    y = x1
    return int(gcd), int(x), int(y)


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        gcd, x, y = gcdExtended(n_i, p)
        sum += a_i * y * p
    result = sum % prod
    return result
