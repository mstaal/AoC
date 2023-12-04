from utils import aoc_helper as helper
from pathlib import Path
from queue import Queue
from functools import lru_cache


def parse_line(line) -> tuple[int, list[int], list[int]]:
    splitted = line.split(":")
    card = int(splitted[0].replace("Card ", "").strip())
    winning_numbers, my_numbers = tuple([e.strip().split(" ") for e in splitted[1].strip().split("|")])
    winning_numbers, my_numbers = [int(e) for e in winning_numbers if e != ""], [int(e) for e in my_numbers if e != ""]
    return card, winning_numbers, my_numbers


def question_1(inp: list[tuple[int, list[int], list[int]]]) -> int:
    points_overview = []
    for card, winning_numbers, my_numbers in inp:
        length = len(set(winning_numbers).intersection(my_numbers))
        points = pow(2, length - 1) if length > 0 else 0
        points_overview.append(points)
    return sum(points_overview)


@helper.profiler
def question_2(inp: list[tuple[int, list[int], list[int]]]) -> int:
    cards = {card: (winning_numbers, my_numbers) for card, winning_numbers, my_numbers in inp}
    copy_count = len(cards)
    q = Queue()
    for c_idx, c in cards.items():
        q.put(c_idx)

    @lru_cache(maxsize=None)
    def compute_length_and_range(crd_no):
        crd = cards[crd_no]
        lngth = len(set(crd[0]).intersection(crd[1]))
        rnge = range(crd_no + 1, crd_no + lngth + 1)
        return lngth, rnge

    while not q.empty():
        card_no = q.get()
        length, next_numbers = compute_length_and_range(card_no)
        for n in next_numbers:
            q.put(n)
        copy_count += length

    return copy_count


if __name__ == '__main__':
    content = Path("data/day4.txt").read_text(encoding="UTF-8").split("\n")
    parsed_content = [parse_line(line) for line in content]

    question1 = question_1(parsed_content)
    print(f"Result 1: {str(question1)}")
    question2 = question_2(parsed_content)
    print(f"Result 2: {str(question2)}")
