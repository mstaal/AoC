from utils import aoc_helper as helper
from pathlib import Path
from itertools import combinations


def compute_weights(parsed: list[list[str]], replacement: int) -> tuple[list[int], list[int]]:
    by_row = [list(line) for line in parsed]
    weight_row = [1 if len(set(e)) == 2 else replacement for e in by_row]
    by_column = [[line[idx] for line in parsed] for idx in range(len(parsed))]
    weight_column = [1 if len(set(e)) == 2 else replacement for e in by_column]
    return weight_row, weight_column


@helper.profiler
def question_1(parsed, squares, replacement) -> int:
    weight_row, weight_column = compute_weights(parsed, replacement)
    combs = list(combinations(squares, 2))
    total = sum([sum(weight_row[min(x1, x2): max(x1, x2)]) + sum(weight_column[min(y1, y2): max(y1, y2)]) for (x1, y1), (x2, y2) in combs])
    return total


if __name__ == '__main__':
    parsed = Path("data/day11.txt").read_text(encoding="UTF-8").split("\n")
    squares = [(idx, idy) for idx, elm_x in enumerate(parsed) for idy, value in enumerate(elm_x) if value == "#"]
    q1 = question_1(parsed, squares, 2)
    print(f"Result 1: {str(q1)}")
    q2 = question_1(parsed, squares, 1000000)
    print(f"Result 2: {str(q2)}")
