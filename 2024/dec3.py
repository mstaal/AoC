from utils import aoc_helper as helper
from pathlib import Path
import re
from collections import defaultdict

regular_characters = {".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}


def question_1(cnt: str) -> int:
    matches = re.findall(r"mul\(\d+,\d+\)", cnt)
    result = sum(int(t[0]) * int(t[1]) for t in [e.removeprefix("mul(").removesuffix(")").split(",") for e in matches])
    return result


def question_2(cnt: str) -> int:
    matches = re.findall(r"mul\(\d+,\d+\)|don\'t\(\)|do\(\)", cnt)
    result = 0
    do_var = True
    for m in matches:
        if m == "do()":
            do_var = True
        elif m == "don't()":
            do_var = False
        elif do_var:
            a, b = m.removeprefix("mul(").removesuffix(")").split(",")
            result += int(a) * int(b)
    return result


if __name__ == '__main__':
    content: str = Path("2024/data/day3.txt").read_text(encoding="UTF-8")

    question1 = question_1(content)
    question2 = question_2(content)

    print(f"Result 1: {str(question1)}")
    print(f"Result 2: {str(question2)}")
