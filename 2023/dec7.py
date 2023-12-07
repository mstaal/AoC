from utils import aoc_helper as helper
from pathlib import Path
from itertools import product
from collections import Counter


ORDER = {"A": 13, "K": 12, "Q": 11, "J": 10, "T": 9, "9": 8, "8": 7, "7": 6, "6": 5, "5": 4, "4": 3, "3": 2, "2": 1}
ORDER_J = {k: v for k, v in ORDER.items() if k != "J"}


def parse_content(cnt):
    parsed = [[x for x in c.split(" ")] for c in cnt]
    parsed = [(c[0], int(c[1])) for c in parsed]
    return parsed


def main_value_of_card(cards: str):
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
    return main


def value_of_card(cards: str):
    return tuple([main_value_of_card(cards)] + [ORDER[c] for c in cards])


def question_1(lines: list[tuple[str, int]]) -> int:
    card_values = [(card, value_of_card(card), bid) for card, bid in lines]
    sorted_cards = sorted(card_values, key=lambda x: x[1])
    order_of_strengths = sum([(idx+1)*bid for idx, (_, _, bid) in enumerate(sorted_cards)])
    return order_of_strengths


def value_of_card_j(cards: str):
    hand_without_js = "".join([c for c in cards if c != "J"])
    hands = [f"""{hand_without_js}{"".join(com)}""" for com in product(list(ORDER_J.keys()), repeat=cards.count("J"))]
    main = max([main_value_of_card(h) for h in hands])
    card_ranking = tuple([main] + [ORDER_J.get(c, 0) for c in cards])
    return card_ranking


@helper.profiler
def question_2(lines: list[tuple[str, int]]) -> int:
    card_values = [(card, value_of_card_j(card), bid) for card, bid in lines]
    sorted_cards = sorted(card_values, key=lambda x: x[1])
    order_of_strengths = sum([(idx + 1) * bid for idx, (_, _, bid) in enumerate(sorted_cards)])
    return order_of_strengths


if __name__ == '__main__':
    content = parse_content(Path("data/day7.txt").read_text(encoding="UTF-8").split("\n"))

    question1 = question_1(content)
    print(f"Result 1: {str(question1)}")
    question2 = question_2(content)
    print(f"Result 2: {str(question2)}")
