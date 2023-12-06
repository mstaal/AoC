from typing import Callable

from utils import aoc_helper as helper
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, wait
import numpy as np


def parse_content(cnt) -> tuple[list[int], Callable]:
    seed_line, remainder = cnt[0], cnt[1:]
    seeds = [int(e) for e in seed_line.split(": ")[1].split(" ")]
    lines = [[x for x in e.split("\n") if x != ""] for e in remainder]

    mappings_list = [[tuple(int(x) for x in e.split(" ")) for e in part[1:]] for part in lines]
    map_ranges = [sorted([((x, x+length), (y, y+length)) for (y, x, length) in m], key=lambda x: x[0][0]) for m in mappings_list]
    minimum = min(seeds)
    for rg in map_ranges:
        if minimum < rg[0][0][0]:
            rg.insert(0, ((minimum, rg[0][0][0]), (minimum, rg[0][0][0])))

        for idx, ((current, _), _) in enumerate(rg[1:]):
            (_, previous), _ = rg[idx]
            if previous < current:
                rg.append(((previous, current), (previous, current)))

        rg.sort(key=lambda x: x[0][0])

    def create_individual_map(rg):
        def m(x):
            return np.interp(x, [itm for (xe, _) in rg for itm in xe], [itm for (x, ye) in rg for itm in ye])
        return m

    def mapping(x):
        for m in [create_individual_map(rg) for rg in map_ranges]:
            x = m(x)
        return x
    return seeds, mapping


def question_1(sds: list[int], mppg: Callable) -> int:
    result = min(mppg(sds))
    return result


@helper.profiler
def question_2(sds: list[int], mppg: Callable) -> int:
    pairs = [tuple(sds[i:i + 2]) for i in range(0, len(sds), 2)]

    def process_element(start, length):
        return np.min(mppg(np.arange(start, start+length)))

    with ThreadPoolExecutor(max_workers=len(pairs)) as executor:
        futures = [executor.submit(process_element, start, length) for (start, length) in pairs]
        # Wait for all tasks to complete
        wait(futures)
        # Get the results from the completed tasks
        result = np.min([future.result() for future in futures])
    return result


if __name__ == '__main__':
    content = Path("data/day5.txt").read_text(encoding="UTF-8").split("\n\n")
    seeds, mappings = parse_content(content)

    question1 = question_1(seeds, mappings)
    print(f"Result 1: {str(question1)}")
    question2 = question_2(seeds, mappings)
    print(f"Result 2: {str(question2)}")
