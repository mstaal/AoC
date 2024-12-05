from utils import aoc_helper as helper
from pathlib import Path
from functools import cmp_to_key


def comparison_func_generator(rules: list[tuple[int,int]]):

    def compare(a: int, b: int) -> int:
        if a == b:
            return 0
        for rule in rules:
            rule_a, rule_b = rule
            if a == rule_a and b == rule_b:
                return -1
        return 1
    
    return compare


def question_1(comparison_key, updates: list[list[int]]) -> tuple[int, list[list[int]], list[list[int]]]:
    sorted_updates = [sorted(e, key=comparison_key) for e in updates]
    correct_updates = []
    incorrect_updates = []
    for i, update in enumerate(sorted_updates):
        if update == updates[i]:
            correct_updates.append(update)
        else:
            incorrect_updates.append(update)
    mid_elements = [e[int(len(e)/2)] for e in correct_updates]
    result = sum(mid_elements)
    return result, correct_updates, incorrect_updates


def question_2(comparison_key, incorrect_updates: list[list[int]]) -> int:
    sorted_updates = [sorted(e, key=comparison_key) for e in incorrect_updates]
    mid_elements = [e[int(len(e)/2)] for e in sorted_updates]
    result = sum(mid_elements)
    return result


if __name__ == '__main__':
    content: list[str] = Path("2024/data/day5.txt").read_text(encoding="UTF-8").split("\n\n")
    rules = [tuple(map(int, e.split("|"))) for e in content[0].split("\n")]
    updates = [list(map(int, e.split(","))) for e in content[1].split("\n")]

    comparison_function = comparison_func_generator(rules)
    comparison_key = cmp_to_key(comparison_function)

    question1, correct_updates, incorrect_updates = question_1(comparison_key, updates)
    question2 = question_2(comparison_key, incorrect_updates)

    print(f"Result 1: {str(question1)}")
    print(f"Result 2: {str(question2)}")
