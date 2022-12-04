from utils import AoCHelper as helper
from pathlib import Path


def to_interval(entry: str):
    a, b = entry
    interval = list(range(int(a), int(b)+1))
    return interval


@helper.profiler
def part1(content_list):
    return [(a, b) for a, b in content_list if set(a) <= set(b) or set(a) >= set(b)]


@helper.profiler
def part2(content_list):
    return [(a, b) for a, b in content_list if len(set(a).intersection(b)) > 0]


if __name__ == '__main__':
    content = Path("data/day4.txt").read_text().split("\n")
    content_cleaned = [(to_interval(a.split("-")), to_interval(b.split("-"))) for a, b in [e.split(",") for e in content]]

    fully_contained_filter = part1(content_cleaned)
    overlapping_filter = part2(content_cleaned)

    print(f"Result 1: {str(len(fully_contained_filter))}")
    print(f"Result 2: {str(len(overlapping_filter))}")
