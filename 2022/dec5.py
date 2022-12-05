from utils import AoCHelper as helper
from pathlib import Path
from copy import deepcopy


def parse_crate_structure(crate_raw_input):
    splitting = crate_raw_input.split("\n")
    lines = [e.split(" ") for e in splitting]
    numbers = [int(e) for e in splitting[-1].split(" ") if e.isdigit()]
    crate_map = {n: list(reversed([c[n-1][1] for c in lines[:-1] if c[n-1] != "..."])) for n in numbers}
    return crate_map


def parse_procedures(procedures_raw_input):
    lines = [e.split(" ") for e in procedures_raw_input.split("\n")]
    return [tuple([int(e) for e in l if e.isdigit()]) for l in lines]


@helper.profiler
def calculate_crate_distribution(crate_input, procedures_input, reverse_tail):
    crate_map = deepcopy(crate_input)
    for amount, from_, to_ in procedures_input:
        from_list = crate_map[from_]
        to_list = crate_map[to_]
        from_remaining = from_list[:-amount]
        from_transfer = (list(reversed(from_list[-amount:])) if reverse_tail else from_list[-amount:])
        crate_map[from_] = from_remaining
        crate_map[to_] = to_list + from_transfer
    return crate_map


if __name__ == '__main__':
    crates_raw, procedures_raw = Path("data/day5.txt").read_text().split("\n\n")
    crates = parse_crate_structure(crates_raw)
    procedures = parse_procedures(procedures_raw)

    def joining(result: dict): return "".join(val[-1] for val in result.values())
    question1 = joining(calculate_crate_distribution(crates, procedures, True))
    question2 = joining(calculate_crate_distribution(crates, procedures, False))

    print(f"Result 1: {str(question1)}")
    print(f"Result 2: {str(question2)}")
