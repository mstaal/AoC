from utils import aoc_helper as helper
from pathlib import Path
from utils.aoc_types import T
from shapely import Polygon


@helper.profiler
def part1(content_input: list[tuple[T, T]], y_val):
    parts = set()
    for i, (x, y) in enumerate(content_input):
        print(f"index: {i}")
        length = int((x-y).manhattan_length())
        gen = (T(a, b) for a in set(range(x[0] - length, x[0] + length)) for b in [y_val])
        area = {e for e in gen if (e - x).manhattan_length() <= length and e != y}
        parts.update(area)
    return len(parts)


@helper.profiler
def part2(content_input):
    return "first * second"


if __name__ == '__main__':
    content = [(x.split(" at ")[1], y.split(" at ")[1]) for x, y in [e.split(": ") for e in Path("data/day15-sample.txt").read_text().split("\n")]]
    content = [(x.split(", "), y.split(", ")) for x, y in content]
    content_cleaned = [(T(int(x[0][2:]), int(x[1][2:])), T(int(y[0][2:]), int(y[1][2:]))) for x, y in content]


    print(f"Result 1: {str(part1(content_cleaned, 10))}")
    print(f"Result 2: {str(part2(content))}")
