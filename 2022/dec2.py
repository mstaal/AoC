from utils import aoc_helper as helper
from pathlib import Path


shape_map = {
    "A": 1,
    "B": 2,
    "C": 3
}

match_outcome_map = {
    "A": {
        "A": "Y",
        "B": "Z",
        "C": "X"
    },
    "B": {
        "A": "X",
        "B": "Y",
        "C": "Z"
    },
    "C": {
        "A": "Z",
        "B": "X",
        "C": "Y"
    }
}

exercise_1_translate = {val: key for key, val in match_outcome_map["B"].items()}


def game_score(entry):
    opponent, me = entry
    if match_outcome_map[opponent][me] == "Z":
        return 6 + shape_map[me]
    elif match_outcome_map[opponent][me] == "Y":
        return 3 + shape_map[me]
    else:
        return shape_map[me]


def calculate_total(games):
    return sum(game_score(entry) for entry in games)


@helper.profiler
def part1(content_list):
    games = [(opponent, exercise_1_translate[me]) for opponent, me in content_list]
    return calculate_total(games)


@helper.profiler
def part2(content_list):
    games = [(opponent, me) for opponent, victory in content_list for me, v in match_outcome_map[opponent].items() if
             victory == v]
    return calculate_total(games)


if __name__ == '__main__':
    content = [e.split(" ") for e in Path("data/day2.txt").read_text().split("\n")]
    question1 = part1(content)
    question2 = part2(content)

    print(f"Result 1: {str(question1)}")
    print(f"Result 2: {str(question2)}")