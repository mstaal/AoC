from utils import aoc_helper as helper
from pathlib import Path
from math import lcm


def parse_content(cnt):
    directions = list(cnt[0])
    node_lines = [[d for d in c.split(" = ")] for c in cnt[1].split("\n")]
    node_lines = [(d[0], tuple(d[1][1:-1].split(", "))) for d in node_lines]
    node_map = {k: v for k, v in node_lines}
    return directions, node_map


def question_1(directions: list[str], node_map: dict[str, tuple[str, str]], start: str, endswith: str) -> int:
    count = 0
    current = start
    while not current.endswith(endswith):
        count += 1
        direction = directions[(count - 1) % len(directions)]
        left, right = node_map[current]
        if direction == "L":
            current = left
        elif direction == "R":
            current = right
    return count


@helper.profiler
def question_2(directions: list[str], node_map: dict[str, tuple[str, str]]) -> int:
    relevant = [a for a in node_map.keys() if a.endswith("A")]
    results_from_first = [question_1(directions, node_map, start, "Z") for start in relevant]
    result = lcm(*results_from_first)
    return result


if __name__ == '__main__':
    directions, node_map = parse_content(Path("data/day8.txt").read_text(encoding="UTF-8").split("\n\n"))

    question1 = question_1(directions, node_map, "AAA", "ZZZ")
    print(f"Result 1: {str(question1)}")
    question2 = question_2(directions, node_map)
    print(f"Result 2: {str(question2)}")
