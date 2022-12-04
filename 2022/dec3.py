from utils import AoCHelper as helper
from pathlib import Path


def letter_to_priority(letter: str):
    if letter.islower():
        return ord(letter) - 96
    return (ord(letter) - 64) + 26


@helper.profiler
def part1(content_list):
    duplicates = [duplicate for a, b in content_list for duplicate in set(a).intersection(b)]
    priorities = [letter_to_priority(e) for e in duplicates]
    return sum(priorities)


@helper.profiler
def part2(content_list):
    # https://stackoverflow.com/questions/1624883/alternative-way-to-split-a-list-into-groups-of-n
    groups = zip(*(iter(content_list),) * 3)
    duplicates_within_group = [duplicate for a, b, c in groups for duplicate in set(a).intersection(b).intersection(c)]
    priorities = [letter_to_priority(e) for e in duplicates_within_group]
    return sum(priorities)


if __name__ == '__main__':
    content = Path("data/day3.txt").read_text().split("\n")
    content_split = [(e[:divmod(len(e), 2)[0]], e[divmod(len(e), 2)[0]:]) for e in content]

    print(f"Result 1: {str(part1(content_split))}")
    print(f"Result 2: {str(part2(content))}")