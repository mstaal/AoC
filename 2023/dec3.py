from utils import aoc_helper as helper
from pathlib import Path
import re
from collections import defaultdict

special_characters = {"#", "$", "%", "&", "*", "+", "-", "/", "=", "@"}




if __name__ == '__main__':
    content = Path("data/day3.txt").read_text(encoding="UTF-8").split("\n")

    characters_dict = {(idx, idy): y for idx, x in enumerate(content) for idy, y in enumerate(x)}

    number_matches = [[(idx, m.span(), m.group()) for m in re.compile(r"\d+").finditer(e)] for idx, e in enumerate(content)]
    flattened_number_matches = [item for lst in number_matches for item in lst]

    symbol_matches_dict = dict()
    for idx, (y_start, y_end), number_match in flattened_number_matches:
        for idy in range(y_start, y_end):
            neighbours = helper.get_neighbours_dict(content, idx, idy, ignore_none=True)
            symbol_matches = set(neighbours.values()).intersection(special_characters)
            if len(symbol_matches) > 0:
                symbol_matches_dict[(idx, (y_start, y_end))] = number_match

    question1 = sum([int(x) for x in symbol_matches_dict.values()])


    star_matches_dict = dict()
    for idx, (y_start, y_end), number_match in flattened_number_matches:
        for idy in range(y_start, y_end):
            neighbours = helper.get_neighbours_dict(content, idx, idy, ignore_none=True)
            for (n_x, n_y), character in neighbours.items():
                if character == "*":
                    star_matches_dict[(idx, (y_start, y_end), number_match)] = (n_x, n_y)

    groups = defaultdict(list)
    for x, y in star_matches_dict.items():
        groups[y].append(x)

    question2 = sum([int(x[0][2]) * int(x[1][2]) for x in groups.values() if len(x) == 2])

    print(f"Result 1: {str(question1)}")
    print(f"Result 2: {str(question2)}")
