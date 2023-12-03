from typing import List, Tuple

from utils import aoc_helper as helper
from pathlib import Path
import numpy as np
import re

special_characters = {"#", "$", "%", "&", "*", "+", "-", "/", "=", "@"}




if __name__ == '__main__':
    content = Path("data/day3.txt").read_text(encoding="UTF-8").split("\n")

    characters_dict = {(idx, idy): y for idx, x in enumerate(content) for idy, y in enumerate(x)}

    number_matches = [[(idx, m.span(), m.group()) for m in re.compile(r"\d+").finditer(e)] for idx, e in enumerate(content)]
    flattened_matches = [item for lst in number_matches for item in lst]

    symbol_matches_dict = dict()
    for idx, (y_start, y_end), match in flattened_matches:
        for idy in range(y_start, y_end):
            neighbours = helper.get_neighbours_dict(content, idx, idy, ignore_none=True)
            symbol_matches = set(neighbours.values()).intersection(special_characters)
            if len(symbol_matches) > 0:
                symbol_matches_dict[(idx, (y_start, y_end))] = match

    question1 = sum([int(x) for x in symbol_matches_dict.values()])

    question2 = question_2(games_parsed)
    print(f"Result 1: {str(question1)}")
    print(f"Result 2: {str(question2)}")
