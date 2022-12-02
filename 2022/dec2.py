from utils import AoCHelper as helper
from pathlib import Path


shape_map = {
    "A": 1,
    "B": 2,
    "C": 3
}

exercise_1_translate = {
    "X": "A",
    "Y": "B",
    "Z": "C"
}

match_generator_map = {
    ("A", "X"): "C",
    ("A", "Y"): "A",
    ("A", "Z"): "B",
    ("B", "X"): "A",
    ("B", "Y"): "B",
    ("B", "Z"): "C",
    ("C", "X"): "B",
    ("C", "Y"): "C",
    ("C", "Z"): "A",
}


def game_score(entry):
    opponent, me = entry
    if (opponent == "A" and me == "B") or (opponent == "B" and me == "C") or (opponent == "C" and me == "A"):
        return 6 + shape_map[me]
    elif opponent == me:
        return 3 + shape_map[me]
    else:
        return shape_map[me]


def calculate_total(games):
    return sum(game_score(entry) for entry in games)


@helper.profiler
def part1(content):
    return calculate_total([(opponent, exercise_1_translate[me]) for opponent, me in content])


@helper.profiler
def part2(content):
    return calculate_total([(opponent, match_generator_map[opponent, me]) for opponent, me in content])


if __name__ == '__main__':
    content = [e.split(" ") for e in Path("data/day2.txt").read_text().split("\n")]
    question1 = part1(content)
    question2 = part2(content)

    print(f"Result 1: {str(question1)}")
    print(f"Result 2: {str(question2)}")