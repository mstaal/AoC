from utils import aoc_helper as helper
from pathlib import Path


def count_rock_load_per_column(c):
    measure = 0
    retro_fit = 0
    for idx, char in enumerate(c):
        if char == "O":
            measure += len(c)-idx+retro_fit
        if char == ".":
            retro_fit += 1
        if char == "#":
            retro_fit = 0
    return measure


@helper.profiler
def question_1(columns) -> int:
    total = sum([count_rock_load_per_column(c) for c in columns])
    return total


@helper.profiler
def question_2(parsed) -> int:
    return 1


if __name__ == '__main__':
    parsed = Path("data/day14.txt").read_text(encoding="UTF-8").split("\n")
    column_based = ["".join([e[idx] for e in parsed]) for idx in range(len(parsed[0]))]
    q1 = question_1(column_based)
    print(f"Result 1: {str(q1)}")
    q2 = question_2(column_based)
    print(f"Result 2: {str(q2)}")
