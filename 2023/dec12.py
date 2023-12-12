from utils import aoc_helper as helper
from pathlib import Path
import re
from functools import cache, lru_cache


class TList:
    def __init__(self, lst):
        self.lst = lst

    def __hash__(self):
        return hash(tuple(self.lst))


def parse_input(parsed):
    parts = [line.split(" ") for line in parsed]
    parts = [(part[0], [int(e) for e in part[1].split(",")]) for part in parts]
    return parts


def determine_combinations(text, numbers):
    groups = [m.span()[0] for m in re.compile(r"\?").finditer(text)]
    replacements = [text]
    for group in groups:
        replacements = [itm for t in replacements for itm in (t[:group] + "#" + t[group+1:], t[:group] + "." + t[group+1:])]
    replacements = [t for t in replacements if t.count("#") == sum(numbers)]
    replacements_split = [(idx, [len(e) for e in t.split(".") if e != ""]) for idx, t in enumerate(replacements)]
    replacements_split = [idx for idx, t in replacements_split if t == numbers]
    replacements = [replacements[idx] for idx in replacements_split]
    return replacements


@helper.profiler
def question_1(digested) -> int:
    combs = [determine_combinations(text, numbers) for text, numbers in digested]
    total = sum([len(comb) for comb in combs])
    return total


@helper.profiler
def question_2(parsed) -> int:
    return 2


if __name__ == '__main__':
    parsed = Path("data/day12.txt").read_text(encoding="UTF-8").split("\n")
    digested = parse_input(parsed)
    q1 = question_1(digested)
    print(f"Result 1: {str(q1)}")
    q2 = question_2(parsed)
    print(f"Result 2: {str(q2)}")
