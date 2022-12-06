from utils import AoCHelper as helper
from pathlib import Path


@helper.profiler
def part1(content_list, seq_length):
    for idx, _ in enumerate(content_list):
        if len(set(content_list[idx: idx + seq_length])) == seq_length:
            return idx + seq_length


if __name__ == '__main__':
    content = list(Path("data/day6.txt").read_text())

    question1 = part1(content, 4)
    question2 = part1(content, 14)

    print(f"Result 1: {str(question1)}")
    print(f"Result 2: {str(question2)}")
