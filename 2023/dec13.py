from utils import aoc_helper as helper
from pathlib import Path
import re
from functools import cache, lru_cache



def parse_input(parsed):
    parts = [line.split(" ") for line in parsed]
    parts = [(part[0], [int(e) for e in part[1].split(",")]) for part in parts]
    return parts


def calculate(lst):
    for idx in range(len(lst)-1):
        current_row = lst[idx]
        next_row = lst[idx+1]
        if current_row == next_row:
            if all(lst[idx-i] == lst[idx+1+i] for i in range(1, min(idx+1, len(lst)-idx-1))):
                return ("row", idx)
    for idx in range(len(lst[0])-1):
        current_column = "".join([e[idx] for e in lst])
        next_column = "".join([e[idx+1] for idy, e in enumerate(lst)])
        if current_column == next_column:
            if all([e[idx-i] for e in lst] == [e[idx+1+i] for e in lst] for i in range(1, min(idx+1, len(lst[0])-idx-1))):
                return ("column", idx)


@helper.profiler
def question_1(parsed) -> int:
    calcs = [calculate(el) for el in parsed]
    hej = ""
    total = sum(e+1 if t == "column" else 100*(e+1) for t, e in calcs)
    return total


@helper.profiler
def question_2(parsed) -> int:
    return 2


if __name__ == '__main__':
    parsed = [e.split("\n") for e in Path("data/day13.txt").read_text(encoding="UTF-8").split("\n\n")]
    q1 = question_1(parsed)
    print(f"Result 1: {str(q1)}")
    q2 = question_2(digested)
    print(f"Result 2: {str(q2)}")
