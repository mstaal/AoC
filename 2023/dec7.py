from utils import aoc_helper as helper
from pathlib import Path
from itertools import product
from collections import Counter


ORDER = {"A": 13, "K": 12, "Q": 11, "J": 10, "T": 9, "9": 8, "8": 7, "7": 6, "6": 5, "5": 4, "4": 3, "3": 2, "2": 1}
ORDER_J = {k: v if k != "J" else 0 for k, v in ORDER.items()}


def main_value_of_card(cards: str):
    counts = Counter(cards)
    if 5 in counts.values():
        return 7
    elif 4 in counts.values():
        return 6
    elif 3 in counts.values() and 2 in counts.values():
        return 5
    elif 3 in counts.values():
        return 4
    elif len([e for e in counts.values() if e == 2]) == 2:
        return 3
    elif 2 in counts.values():
        return 2
    return 1


def value_of_card(cards: str):
    return tuple([main_value_of_card(cards)] + [ORDER[c] for c in cards])


def value_of_card_j(cards: str):
    hand_without_js = "".join([c for c in cards if c != "J"])
    hands = [f"""{hand_without_js}{"".join(com)}""" for com in product(list(ORDER_J.keys()), repeat=cards.count("J"))]
    return tuple([max([main_value_of_card(h) for h in hands])] + [ORDER_J[c] for c in cards])


def compute_total_winning(lines: list[tuple[str, int]], card_ranking: callable) -> int:
    card_values = [(card_ranking(card), bid) for card, bid in lines]
    order_of_strengths = sum([(idx + 1) * bid for idx, (_, bid) in enumerate(sorted(card_values))])
    return order_of_strengths


def question_1(lines: list[tuple[str, int]]) -> int:
    return compute_total_winning(lines, value_of_card)


@helper.profiler
def question_2(lines: list[tuple[str, int]]) -> int:
    return compute_total_winning(lines, value_of_card_j)


if __name__ == '__main__':
    content = [(c[0], int(c[1])) for c in [[x for x in c.split(" ")] for c in Path("data/day7.txt").read_text(encoding="UTF-8").split("\n")]]

    question1 = question_1(content)
    print(f"Result 1: {str(question1)}")
    question2 = question_2(content)
    print(f"Result 2: {str(question2)}")
