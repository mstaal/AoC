import itertools
import re
import urllib.parse
from pathlib import Path
from typing import Callable
from shapely.geometry import Polygon
import numpy as np
import pandas as pd
from functools import reduce
from concurrent.futures import ThreadPoolExecutor, wait
from utils.global_variables import all_directions, all_directions_3d, cardinal_directions
from time import time


def profiler(method):
    def wrapper_method(*arg, **kw):
        t = time()
        result = method(*arg, **kw)
        print(f"Method '{method.__name__}' took: {round(time() - t, 6)} secs")
        return result

    return wrapper_method


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


def embed_matrix(matrix, val=0, np_type=np.int64, repeat=1):
    vec = lambda mat: [val for _ in mat]
    extend = lambda mat, k: np.rot90(mat) if k == 0 else extend(np.c_[mat, vec(mat)].astype(np_type), k - 1)
    new_matrix = extend(extend(extend(extend(matrix, repeat), repeat), repeat), repeat)
    return new_matrix


def linear_2d_operation(points, matrix, as_tuple):
    if isinstance(points, tuple) or (
            isinstance(points, list) and len(points) == 2 and all(isinstance(s, int) for s in points)):
        result = np.array(points).dot(matrix)
        if as_tuple:
            return tuple(result)
        return result
    return [linear_2d_operation(element, matrix, as_tuple) for element in points]


def rot_points_90(points, as_tuple=False):
    return linear_2d_operation(points, [[0, 1], [-1, 0]], as_tuple)


def rot_points_90_clockwise(points, as_tuple=False):
    return linear_2d_operation(points, [[0, -1], [1, 0]], as_tuple)


def reflect_points_x(points, as_tuple=False):
    return linear_2d_operation(points, [[1, 0], [0, -1]], as_tuple)


def reflect_points_y(points, as_tuple=False):
    return linear_2d_operation(points, [[-1, 0], [0, 1]], as_tuple)


def get_neighbor_rays(r, c, content: list[list], max_radius=None) -> tuple[list, list, list, list]:
    def _condition(i: int): return max_radius is None or i < max_radius

    top = [row[c] for i, row in enumerate(content[:r]) if _condition(i)]
    bottom = [row[c] for i, row in enumerate(content[r + 1:]) if _condition(i)]
    left = [col for i, col in enumerate(content[r][:c]) if _condition(i)]
    right = [col for i, col in enumerate(content[r][c + 1:]) if _condition(i)]
    return top, bottom, left, right


def get_neighbours_dict(coll, i, j, directions=all_directions, ignore_none=False, characters_to_skip=[], radius=1):
    adjacent_material = {}
    for x, y in [(x * radius, y * radius) for x, y in directions]:
        if 0 <= i + x < len(coll) and 0 <= j + y < len(coll[0]):
            element = coll[i + x][j + y]
            if element not in characters_to_skip:
                adjacent_material[(i + x, j + y)] = coll[i + x][j + y]
        elif not ignore_none:
            adjacent_material[(i + x, j + y)] = None
    return adjacent_material


def get_neighbours_dict_3d(coll, i, j, k, directions=all_directions_3d, ignore_none=False, characters_to_skip=[],
                           radius=1):
    adjacent_material = {}
    for x, y, z in [(x * radius, y * radius, z * radius) for x, y, z in directions]:
        if 0 <= i + x < len(coll) and 0 <= j + y < len(coll[0]) and 0 <= k + z < len(coll[0][0]):
            element = coll[i + x][j + y][k + z]
            if element not in characters_to_skip:
                adjacent_material[(i + x, j + y, k + z)] = coll[i + x][j + y][k + z]
        elif not ignore_none:
            adjacent_material[(i + x, j + y, k + z)] = None
    return adjacent_material


def adjac_helper(ele, sub=[]):
    if not ele:
        yield sub
    else:
        yield from [idx for j in range(ele[0] - 1, ele[0] + 2) for idx in adjac_helper(ele[1:], sub + [j])]


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


def split_file(file, sep):
    return Path(file).read_text(encoding="UTF-8").split(sep)


def binary_parse(word, letter):
    number = 0
    for idx, val in enumerate(str(word)):
        factor = 2 ** (len(word) - 1 - idx)
        number = number + factor if str(val) == str(letter) else number
    return number


def contains_any(element, condition_collection):
    return any(element.__contains__(sub) for sub in condition_collection)


def flatten(lst: list):
    return [item for sublist in lst for item in sublist]


def reverse_dict(dictionary: dict):
    return {value: key for key, value in dictionary.items()}


def permutations(element, length=None):
    return itertools.permutations(element, length if length is not None else len(element))


def combinations(element, repeat=None):
    return [x for x in itertools.product(element, repeat=repeat if repeat is not None else len(element))]


def base_to_binary(number, base=16):
    return bin(int(str(number), base))[2:]


def base_to_hex(number, base=2):
    return hex(int(number, base))


def base_to_base10(number, base=2):
    return int(str(number), base)


def replace_nth(text, sub, wanted, n):
    where = [m for m in re.finditer(sub, text)][n]
    before = text[:where.regs[0][0]]
    after = text[where.regs[0][1]:]
    new_string = before + wanted + after
    return new_string


def gcd_extended(a, b):
    # Base Case
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcd_extended(b % a, a)
    # Update x and y using results of recursive call
    x = y1 - (b // a) * x1
    y = x1
    return int(gcd), int(x), int(y)


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        gcd, x, y = gcd_extended(n_i, p)
        sum += a_i * y * p
    result = sum % prod
    return result


def wolfram_alpha_query(equation):
    return f"https://www.wolframalpha.com/input?i={urllib.parse.quote(f'{equation}')}"


def parallel(max_workers: int, process_element: Callable, args: list[tuple]):
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(process_element, *arg) for arg in args]
        # Wait for all tasks to complete
        wait(futures)
        # Get the results from the completed tasks
        results = [future.result() for future in futures]
    return results


def pairwise(iterable: iter):
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


def get_polygon_and_properties(exterior_points: list[tuple[int, int]]) -> tuple[Polygon, float, int, int]:
    polygon = Polygon(exterior_points)
    number_of_integer_points_on_boundary = polygon.length
    area = polygon.area
    # Pick's theorem: https://en.wikipedia.org/wiki/Pick%27s_theorem
    number_of_integer_points_in_interior = int(area + 1 - number_of_integer_points_on_boundary / 2)
    # Alternatively: (See: https://www.reddit.com/r/adventofcode/comments/18l0qtr/comment/kdvjfse/?utm_source=share&utm_medium=web2x&context=3)
    # polygon.buffer(0.5, join_style="mitre").area
    return polygon, area, number_of_integer_points_on_boundary, number_of_integer_points_in_interior
