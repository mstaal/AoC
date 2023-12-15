from collections import defaultdict
from utils import aoc_helper as helper
from pathlib import Path


def hasher(element):
    current_value = 0
    ascii_values = [ord(e) for e in element]
    for idx, val in enumerate(ascii_values):
        current_value = ((current_value + val) * 17) % 256
    return current_value


@helper.profiler
def question_1(p) -> int:
    return sum(hasher(e) for e in p)


@helper.profiler
def question_2(p) -> int:
    cache = defaultdict(dict)
    for idx, elm_x in enumerate(p):
        if "=" in elm_x:
            label, focal_length = elm_x.split("=")
            cache[hasher(label)][label] = int(focal_length)
        if "-" in elm_x:
            label = elm_x[:-1]
            if hasher(label) in cache and label in cache[hasher(label)]:
                del cache[hasher(label)][label]
    return sum((box+1)*(slot+1)*length for box in cache.keys() for slot, length in enumerate(cache[box].values()))


if __name__ == '__main__':
    parsed = Path("data/day15.txt").read_text(encoding="UTF-8").split(",")
    q1 = question_1(parsed)
    print(f"Result 1: {str(q1)}")
    q2 = question_2(parsed)
    print(f"Result 2: {str(q2)}")
