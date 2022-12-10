from utils import aoc_helper as helper
from pathlib import Path


@helper.profiler
def solve(content_list, seq_length):
    for idx, _ in enumerate(content_list):
        if len(set(content_list[idx: idx + seq_length])) == seq_length:
            return idx + seq_length


if __name__ == '__main__':
    content = list(Path("data/day6.txt").read_text())

    print(f"Result 1: {str(solve(content, 4))}")
    print(f"Result 2: {str(solve(content, 14))}")
