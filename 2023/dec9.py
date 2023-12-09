from utils import aoc_helper as helper
from pathlib import Path


def parse_content(cnt):
    return [[int(itm) for itm in e.split(" ")] for e in cnt]


def extrapolate(parsed: list[list[int]]) -> list[tuple[int, int]]:
    extrapolated = []
    for i, lst in enumerate(parsed):
        line = [lst.copy()]
        current = lst.copy()
        while any(a != 0 for a in current):
            current = [b-a for a, b in helper.pairwise(current)]
            line.append(current)
        line = list(reversed(line))
        for idx, val in enumerate(line[:-1]):
            line[idx+1].append(line[idx+1][-1]+val[-1])
            line[idx+1].insert(0, line[idx+1][0]-val[0])
        extrapolated.append((line[-1][0], line[-1][-1]))
    return extrapolated


def question_1(extra: list[tuple[int, int]]) -> int:
    return sum(y for _, y in extra)


@helper.profiler
def question_2(extra: list[tuple[int, int]]) -> int:
    return sum(x for x, _ in extra)


if __name__ == '__main__':
    parsed = parse_content(Path("data/day9.txt").read_text(encoding="UTF-8").split("\n"))
    extrapolated = extrapolate(parsed)

    question1 = question_1(extrapolated)
    print(f"Result 1: {str(question1)}")
    question2 = question_2(extrapolated)
    print(f"Result 2: {str(question2)}")
