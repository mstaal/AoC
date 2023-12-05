from typing import Callable

from utils import aoc_helper as helper
from pathlib import Path
import numpy as np


def parse_content(cnt) -> tuple[list[int], Callable]:
    seed_line, remainder = cnt[0], cnt[1:]
    seeds = [int(e) for e in seed_line.split(": ")[1].split(" ")]
    lines = [[x for x in e.split("\n") if x != ""] for e in remainder]

    def parse_part(part, minimum):
        mappings_list = [tuple(int(x) for x in e.split(" ")) for e in part[1:]]
        ranges = sorted([((x, x+length), (y, y+length)) for (y, x, length) in mappings_list], key=lambda x: x[0][0])
        if minimum < ranges[0][0][1]:
            ranges = [((minimum, ranges[0][0][1]), (minimum, ranges[0][0][1]))] + ranges

        for idx, ((current, _), _) in enumerate(ranges[1:]):
            (_, previous), _ = ranges[idx]
            if previous < current:
                ranges.append(((previous, current), (previous, current)))
        ranges = sorted([(x, y) for (x, y) in ranges], key=lambda x: x[0][0])

        def m(x):
            return np.interp(x, [itm for (x, y) in ranges for itm in x], [itm for (x, y) in ranges for itm in y])

        return m
    mappings = [parse_part(line, min(seeds)) for line in lines]

    def mapping(x):
        for m in mappings:
            x = m(x)
        return x
    return seeds, mapping


def question_1(sds: list[int], mppg: Callable) -> int:
    result = min(mppg(sds))
    return result


@helper.profiler
def question_2(sds: list[int], mppg: Callable) -> int:
    pairs = [tuple(sds[i:i + 2]) for i in range(0, len(sds), 2)]
    candidates = set()
    for p_start, p_length in pairs:
        calc = np.min(mppg(np.arange(p_start, p_start+p_length)))
        candidates.add(calc)
    result = min(candidates)
    return result


if __name__ == '__main__':
    content = Path("data/day5.txt").read_text(encoding="UTF-8").split("\n\n")
    seeds, mappings = parse_content(content)

    question1 = question_1(seeds, mappings)
    print(f"Result 1: {str(question1)}")
    question2 = question_2(seeds, mappings)
    print(f"Result 2: {str(question2)}")
