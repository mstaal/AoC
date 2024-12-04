from utils import aoc_helper as helper
from pathlib import Path
from collections import Counter


def question_1(cnt: list[list[int]]) -> int:
    column_first = sorted([e[0] for e in cnt])
    column_second = sorted([e[1] for e in cnt])
    distances = [abs(column_first[i] - column_second[i]) for i in range(len(column_first))]
    result = sum(distances)
    return result


def question_2(cnt: list[list[int]]) -> int:
    column_first = [e[0] for e in cnt]
    column_second = [e[1] for e in cnt]
    counter_second = Counter(column_second)
    result = 0
    for i in range(len(column_first)):
        result += column_first[i] * counter_second[column_first[i]]
    return result


if __name__ == '__main__':
    content = [e.split(" ") for e in Path("2024/data/day1.txt").read_text(encoding="UTF-8").split("\n")]
    content_cleaned = [[int(t) for t in e if t != ""] for e in content]
    
    question1 = question_1(content_cleaned)
    question2 = question_2(content_cleaned)

    print(f"Result 1: {str(question1)}")
    print(f"Result 2: {str(question2)}")
