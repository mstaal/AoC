from utils import aoc_helper as helper
from pathlib import Path
from copy import deepcopy
from functools import cmp_to_key
import ast


def compare_left_right(left, right):
    return -1 if __compare_left_right(deepcopy(left), deepcopy(right)) else 1


def __compare_left_right(left, right):
    if len(left) == 0 and len(right) > 0:
        return True
    elif len(left) > 0 and len(right) == 0:
        return False
    elif len(left) == 0 and len(right) == 0:
        return None
    a = left.pop(0)
    b = right.pop(0)
    if isinstance(a, int) and isinstance(b, int) and len(left) == 0 and len(right) == 0 and a == b:
        return None
    if isinstance(a, int) and isinstance(b, int) and len(right) == 0:
        return a < b
    elif isinstance(a, int) and isinstance(b, int) and len(left) == 0:
        return a <= b
    elif isinstance(a, int) and isinstance(b, int):
        if a == b:
            return __compare_left_right(left, right)
        return a < b
    elif isinstance(a, list) and isinstance(b, list):
        preliminary = __compare_left_right(a, b)
        if preliminary is not None:
            return preliminary
        return __compare_left_right(left, right)
    elif isinstance(a, int) and isinstance(b, list):
        return __compare_left_right([[a]] + left, [b] + right)
    elif isinstance(a, list) and isinstance(b, int):
        return __compare_left_right([a] + left, [[b]] + right)


@helper.profiler
def part1(content_list):
    return sum(idx+1 for idx, (first, second) in enumerate(content_list) if compare_left_right(first, second) == -1)


@helper.profiler
def part2(content_input):
    sorted_list = sorted(content_input, key=cmp_to_key(compare_left_right))
    first, second = [idx+1 for idx, lst in enumerate(sorted_list) if lst == [[2]] or lst == [[6]]]
    return first * second


if __name__ == '__main__':
    def parse(lst): return [ast.literal_eval(e) for e in lst]
    content = [e.split("\n") for e in Path("data/day13.txt").read_text().split("\n\n")]
    content_parsed = [parse(lst) for lst in content]

    content_parsed_part_2 = [e for lst in deepcopy(content_parsed) for e in lst] + [[[2]]] + [[[6]]]

    print(f"Result 1: {str(part1(content_parsed))}")
    print(f"Result 2: {str(part2(content_parsed_part_2))}")
