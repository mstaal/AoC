import math
from itertools import permutations
from utils import aoc_helper as helper
import json
import re
import copy as cp


def insert_after_or_before(new, inner):
    start, end = str(new).replace(" ", "").split("None")

    matches_start = list(re.finditer("\d{1,}", start))
    matches_end = list(re.finditer("\d{1,}", end))
    if len(matches_start) == 0 and len(matches_end) == 0:
        return json.loads(str(new).replace(" ", "").replace("None", "0"))
    if len(matches_start) > 0:
        match_start = matches_start[-1]
        value_start = int(start[match_start.start():match_start.end()]) + inner[0]
        start = start[0:match_start.start()] + str(value_start) + start[match_start.end():]
    if len(matches_end) > 0:
        match_end = matches_end[0]
        value_end = int(end[match_end.start():match_end.end()]) + inner[1]
        end = end[0:match_end.start()] + str(value_end) + end[match_end.end():]
    result = json.loads(start + "0" + end)
    return result


def explode(input):
    if helper.depth(input) <= 4:
        return input, False
    copy = cp.deepcopy(input)
    for idx, elm_x in enumerate(input):
        if helper.depth(elm_x) >= 4:
            for idy, elm_y in enumerate(elm_x):
                if helper.depth(elm_y) >= 3:
                    for idz, elm_z in enumerate(elm_y):
                        if helper.depth(elm_z) >= 2:
                            for idw, elm_w in enumerate(elm_z):
                                if helper.depth(elm_w) >= 1:
                                    copy[idx][idy][idz][idw] = None
                                    complete = insert_after_or_before(copy, elm_w)
                                    return complete, True
    return input, False


def get_first_large_element(input):
    for idx, elm_x in enumerate(input):
        if isinstance(elm_x, int) and elm_x > 9:
            return (idx, None, None, None), elm_x
        elif isinstance(elm_x, list):
            for idy, elm_y in enumerate(elm_x):
                if isinstance(elm_y, int) and elm_y > 9:
                    return (idx, idy, None, None), elm_y
                elif isinstance(elm_y, list):
                    for idz, elm_z in enumerate(elm_y):
                        if isinstance(elm_z, int) and elm_z > 9:
                            return (idx, idy, idz, None), elm_z
                        elif isinstance(elm_z, list):
                            for idw, elm_w in enumerate(elm_z):
                                if isinstance(elm_w, int) and elm_w > 9:
                                    return (idx, idy, idz, idw), elm_w
    return None, None

def split(input):
    copy = cp.deepcopy(input)
    tup, value = get_first_large_element(copy)
    if value is None:
        return copy, False
    loop = [element for element in tup if element is not None]
    lst = copy
    for index in loop[0:len(loop)-1]:
        lst = lst[index]
    lst[loop[-1]] = [math.floor(value / 2), math.ceil(value / 2)]
    return copy, True


def one_calculation(added):
    spl_result = True
    while helper.depth(added) > 4 or spl_result:
        added, explode_res = explode(added)
        if explode_res:
            continue
        added, spl_result = split(added)
    return added


def add_all(content):
    result = content[0] if len(content) > 0 else None
    for idx, element in enumerate(content[1:]):
        added = [result, element]
        result = one_calculation(added)
    return result


def magnitude(result):
    if isinstance(result, int):
        return result
    return 3 * magnitude(result[0]) + 2 * magnitude(result[1])


if __name__ == '__main__':
    content = [json.loads(element) for element in helper.splitFile("day18.txt", "\n")]
    added = add_all(content)
    result1 = magnitude(added)
    print(f"Result 1: {str(result1)}")

    result2 = max(magnitude(one_calculation([x, y])) for x, y in list(permutations(content, 2)))
    print(f"Result 2: {str(result2)}")
