from utils import aoc_helper as helper
from pathlib import Path
from copy import deepcopy


def parse(content_input):
    result = []
    for idx in range(0, len(content_input)-1):
        a, b = content_input[idx].split(",")
        c, d = content_input[idx+1].split(",")
        result += [(x, y) for x in range(int(a), int(c)+1) for y in range(int(b), int(d)+1)]
    return result

@helper.profiler
def part1(content_input):
    return ""


@helper.profiler
def part2(content_input):
    return "first * second"


if __name__ == '__main__':
    content = [e.split(" -> ") for e in Path("data/day14-sample.txt").read_text().split("\n")]

    content_parsed = [parse(e) for e in content]

    content_parsed_part_2 = [e for lst in deepcopy(content) for e in lst] + [[[2]]] + [[[6]]]

    print(f"Result 1: {str(part1(content_parsed))}")
    print(f"Result 2: {str(part2(content_parsed_part_2))}")
