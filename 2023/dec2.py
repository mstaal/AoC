from typing import List, Tuple

from utils import aoc_helper as helper
from pathlib import Path
import numpy as np


def parse_game(text: str) -> tuple[int, list[dict]]:
    game_id, payload = text.split(": ")
    game_id = int(game_id.replace("Game ", ""))

    subsets = [{z[1]: int(z[0]) for z in [y.split(" ") for y in x.split(", ")]} for x in payload.split("; ")]
    return game_id, subsets


def question_1(games: dict[int, list[dict]]) -> int:
    breaking_games = set()
    for game_id, game in games.items():
        for subset in game:
            if subset.get("red", 0) > 12 or subset.get("green", 0) > 13 or subset.get("blue", 0) > 14:
                breaking_games.add(game_id)
    possible_games = set(games.keys()) - breaking_games
    return sum(possible_games)


def question_2(games: dict[int, list[dict]]) -> int:
    game_power = dict()
    for game_id, game in games.items():
        power = int(np.prod([max(subset.get(color, 0) for subset in game) for color in ["red", "green", "blue"]]))
        game_power[game_id] = power
    return sum(game_power.values())


if __name__ == '__main__':
    content = Path("data/day2.txt").read_text(encoding="UTF-8").split("\n")
    games_parsed = {game_id: game for game_id, game in [parse_game(line) for line in content]}

    question1 = question_1(games_parsed)
    question2 = question_2(games_parsed)
    print(f"Result 1: {str(question1)}")
    print(f"Result 2: {str(question2)}")
