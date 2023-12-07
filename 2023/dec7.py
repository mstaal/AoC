from utils import aoc_helper as helper
from pathlib import Path
from math import sqrt, ceil, floor
import numpy as np
from collections import Counter


ORDER = {"A": 1, "K": 2, "Q": 3, "J": 4, "T": 5, "9": 6, "8": 7, "7": 8, "6": 9, "5": 10, "4": 11, "3": 12, "2": 13}
ORDER_J = {"A": 1, "K": 2, "Q": 3, "J": 14, "T": 5, "9": 6, "8": 7, "7": 8, "6": 9, "5": 10, "4": 11, "3": 12, "2": 13}


def parse_content(cnt):
    parsed = [[x for x in c.split(" ")] for c in cnt]
    parsed = [(c[0], int(c[1])) for c in parsed]
    return parsed


def value_of_card(cards: str):
    counts = Counter(cards)
    if 5 in counts.values():
        main = 1
    elif 4 in counts.values():
        main = 2
    elif 3 in counts.values() and 2 in counts.values():
        main = 3
    elif 3 in counts.values():
        main = 4
    elif len([e for e in counts.values() if e == 2]) == 2:
        main = 5
    elif 2 in counts.values():
        main = 6
    else:
        main = 7
    card_ranking = tuple([main] + [ORDER[c] for c in cards])
    return cards, card_ranking


def question_1(lines: list[tuple[str, int]]) -> int:
    card_values = [(value_of_card(card), bid) for card, bid in lines]
    sorted_cards = sorted(card_values, key=lambda x: x[0][1], reverse=True)
    order_of_strengths = sum([(idx+1)*bid for idx, (_, bid) in enumerate(sorted_cards)])
    return order_of_strengths


@helper.profiler
def question_2(lines: list[tuple[str, int]]) -> int:
    return result


if __name__ == '__main__':
    content = parse_content(Path("data/day7.txt").read_text(encoding="UTF-8").split("\n"))

    question1 = question_1(content)
    print(f"Result 1: {str(question1)}")
    question2 = question_2(content)
    print(f"Result 2: {str(question2)}")
