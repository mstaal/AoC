from utils import aoc_helper as helper
from pathlib import Path
import ast


def parse(lst):
    return [ast.literal_eval(e) for e in lst]


def compare_left_right(left, right):
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
            return compare_left_right(left, right)
        return a < b
    elif isinstance(a, list) and isinstance(b, list):
        preliminary = compare_left_right(a, b)
        if preliminary is not None:
            return preliminary
        return compare_left_right(left, right)
    elif isinstance(a, int) and isinstance(b, list):
        return compare_left_right([[a]] + left, [b] + right)
    elif isinstance(a, list) and isinstance(b, int):
        return compare_left_right([a] + left, [[b]] + right)


@helper.profiler
def part1(content_list):
    right_order_map = {}
    for idx, (first, second) in enumerate(content_list):
        result = compare_left_right(first, second)
        right_order_map[idx] = result
    indices_sum = sum(idx+1 for idx, val in right_order_map.items() if val)
    return indices_sum


@helper.profiler
def part2(content_list):
    return ""


if __name__ == '__main__':
    content = [e.split("\n") for e in Path("data/day13.txt").read_text().split("\n\n")]
    content_parsed = [parse(lst) for lst in content]


    print(f"Result 1: {str(part1(content_parsed))}")

    print(f"Result 2: {str(part2(content_parsed))}")
