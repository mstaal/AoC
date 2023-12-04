from utils import aoc_helper as helper
from pathlib import Path
import re
from collections import defaultdict

regular_characters = {".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}


def question_1(cnt: list[str], flttnd_number_matches: list) -> int:
    symbol_matches_dict = dict()
    for idx, (y_start, y_end), number_match in flttnd_number_matches:
        for idy in range(y_start, y_end):
            neighbours = helper.get_neighbours_dict(cnt, idx, idy, ignore_none=True)
            symbol_matches = set(neighbours.values()).difference(regular_characters)
            if len(symbol_matches) > 0:
                symbol_matches_dict[(idx, (y_start, y_end))] = number_match
    return sum(symbol_matches_dict.values())


def question_2(cnt: list[str], flttnd_number_matches: list) -> int:
    star_matches = defaultdict(set)
    for idx, (y_start, y_end), number_match in flttnd_number_matches:
        for idy in range(y_start, y_end):
            neighbours = helper.get_neighbours_dict(cnt, idx, idy, ignore_none=True)
            for (n_x, n_y), character in neighbours.items():
                if character == "*":
                    star_matches[(n_x, n_y)].add((idx, (y_start, y_end), number_match))
    star_numbers = {k: tuple(number_match for (_, _, number_match) in v) for k, v in star_matches.items() if len(v) == 2}
    return sum([x0 * x1 for (x0, x1) in star_numbers.values()])


if __name__ == '__main__':
    content = Path("data/day3.txt").read_text(encoding="UTF-8").split("\n")

    number_matches = [[(idx, m.span(), int(m.group())) for m in re.compile(r"\d+").finditer(e)] for idx, e in enumerate(content)]
    flattened_number_matches = [item for lst in number_matches for item in lst]

    question1 = question_1(content, flattened_number_matches)
    question2 = question_2(content, flattened_number_matches)

    print(f"Result 1: {str(question1)}")
    print(f"Result 2: {str(question2)}")
