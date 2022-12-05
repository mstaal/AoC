from utils import AoCHelper as helper
from pathlib import Path
from copy import deepcopy


def parse_crate_structure(crate_raw_input):
    crate_map = dict()
    splitting = crate_raw_input.split("\n")
    lines = [e.split(" ") for e in splitting]
    chars = lines[:-1]
    numbers = [int(e) for e in splitting[-1].split(" ") if e.isdigit()]
    for n in numbers:
        column = [c[n-1][1] for c in chars if c[n-1] != "..."]
        column.reverse()
        crate_map[n] = column
    return crate_map


def parse_procedures(procedures_raw_input):
    lines = [e.split(" ") for e in procedures_raw_input.split("\n")]
    return [tuple([int(e) for e in l if e.isdigit()]) for l in lines]


@helper.profiler
def part1(crate_input, procedures_input):
    crate_copy = deepcopy(crate_input)
    for amount, from_, to_ in procedures_input:
        from_list = crate_copy[from_]
        to_list = crate_copy[to_]
        for _ in range(0, amount):
            to_list.append(from_list.pop())
    return crate_copy


@helper.profiler
def part2(crate_input, procedures_input):
    crate_copy = deepcopy(crate_input)
    for amount, from_, to_ in procedures_input:
        from_list = crate_copy[from_]
        to_list = crate_copy[to_]
        from_remaining = from_list[:-amount]
        from_transfer = from_list[-amount:]
        crate_copy[from_] = from_remaining
        crate_copy[to_] = to_list + from_transfer
    return crate_copy


if __name__ == '__main__':
    crates_raw, procedures_raw = Path("data/day5.txt").read_text().split("\n\n")
    crates = parse_crate_structure(crates_raw)
    procedures = parse_procedures(procedures_raw)

    def joining(result: dict): return "".join([val[-1] for val in result.values()])
    question1 = joining(part1(crates, procedures))
    question2 = joining(part2(crates, procedures))

    print(f"Result 1: {str(question1)}")
    print(f"Result 2: {str(question2)}")
