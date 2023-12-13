from utils import aoc_helper as helper
from pathlib import Path


def parse_input(parsed):
    parts = [line.split(" ") for line in parsed]
    parts = [(part[0], [int(e) for e in part[1].split(",")]) for part in parts]
    return parts


def search(lst):
    results = set()
    for idx in range(len(lst)-1):
        if all(lst[idx-i] == lst[idx+1+i] for i in range(0, min(idx+1, len(lst)-idx-1))):
            results.add(("row", idx))
    for idy in range(len(lst[0])-1):
        if all([e[idy-i] for e in lst] == [e[idy+1+i] for e in lst] for i in range(0, min(idy+1, len(lst[0])-idy-1))):
            results.add(("column", idy))
    return results


@helper.profiler
def question_1(parsed) -> tuple[int, list[tuple[str, int]]]:
    splitted = [e.split("\n") for e in parsed]
    calcs = [itm for lst in splitted for itm in search(lst)]
    total = sum(e+1 if t == "column" else 100*(e+1) for t, e in calcs)
    return total, calcs


@helper.profiler
def question_2(parsed) -> int:
    _, old_calcs = question_1(parsed)
    calcs = []
    for idx, text in enumerate(parsed):
        for idc, char in enumerate(text):
            new_char = "." if char == "#" else ("#" if char == "." else char)
            new_search = search(f"{text[:idc]}{new_char}{text[idc+1:]}".split("\n")).difference({old_calcs[idx]})
            if new_search:
                calcs.append(next(iter(new_search)))
                break
    total = sum(e + 1 if t == "column" else 100 * (e + 1) for t, e in calcs)
    return total


if __name__ == '__main__':
    parsed = Path("data/day13.txt").read_text(encoding="UTF-8").split("\n\n")
    q1, _ = question_1(parsed)
    print(f"Result 1: {str(q1)}")
    q2 = question_2(parsed)
    print(f"Result 2: {str(q2)}")
