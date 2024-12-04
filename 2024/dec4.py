from utils import aoc_helper as helper
from pathlib import Path
import numpy as np


def question_1(cnt: list[str]) -> int:
    words_to_check = cnt.copy()
    matrix = np.array([list(c) for c in cnt])
    words_to_check.extend(["".join(e) for e in np.rot90(matrix, -1)])
    words_to_check.extend(["".join(matrix.diagonal(i)) for i in range(-len(cnt)+1, len(cnt))])
    words_to_check.extend(["".join(np.flipud(matrix).diagonal(i)) for i in range(-len(cnt)+1, len(cnt))])
    count = 0
    for word in words_to_check:
        count += word.count("XMAS") + word[::-1].count("XMAS")
    return count


def question_2(cnt: list[str]) -> int:
    

    result = 0
    return result


if __name__ == '__main__':
    content: list[str] = Path("2024/data/day4.txt").read_text(encoding="UTF-8").split("\n")

    question1 = question_1(content)
    question2 = question_2(content)

    print(f"Result 1: {str(question1)}")
    print(f"Result 2: {str(question2)}")
