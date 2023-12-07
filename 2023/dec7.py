from utils import aoc_helper as helper
from pathlib import Path
from math import sqrt, ceil, floor
import numpy as np
from collections import Counter


ORDER = {"A": 13, "K": 12, "Q": 11, "J": 10, "T": 9, "9": 8, "8": 7, "7": 6, "6": 5, "5": 4, "4": 3, "3": 2, "2": 1}


def parse_content(cnt):
    parsed = [[x for x in c.split(" ")] for c in cnt]
    parsed = [(c[0], int(c[1])) for c in parsed]
    return parsed


def value_of_card(cards: str):
    counts = Counter(cards)
    if 5 in counts.values():
        main = 7
    elif 4 in counts.values():
        main = 6
    elif 3 in counts.values() and 2 in counts.values():
        main = 5
    elif 3 in counts.values():
        main = 4
    elif len([e for e in counts.values() if e == 2]) == 2:
        main = 3
    elif 2 in counts.values():
        main = 2
    else:
        main = 1
    card_ranking = tuple([main] + [ORDER[c] for c in cards])
    return cards, card_ranking


def question_1(lines: list[tuple[str, int]]) -> int:
    card_values = [(value_of_card(card), bid) for card, bid in lines]
    sorted_cards = sorted(card_values, key=lambda x: x[0][1])
    order_of_strengths = sum([(idx+1)*bid for idx, (_, bid) in enumerate(sorted_cards)])
    return order_of_strengths


@helper.profiler
def question_2(lines: list[tuple[str, int]]) -> int:
    card_values = [(value_of_card(card), bid) for card, bid in lines]
    return result


if __name__ == '__main__':
    content = parse_content(Path("data/day7.txt").read_text(encoding="UTF-8").split("\n"))

    question1 = question_1(content)
    print(f"Result 1: {str(question1)}")
    question2 = question_2(content)
    print(f"Result 2: {str(question2)}")
