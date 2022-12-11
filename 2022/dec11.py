import copy
from utils import aoc_helper as helper
from pathlib import Path
from operator import mul
from functools import reduce


def parse_line(element):
    lines = [e.strip() for e in element.split("\n")]
    return {
        "monkey": int(lines[0].split(" ")[1][:-1]),
        "worry_levels": [int(e) for e in lines[1].split(": ")[1].split(", ")],
        "operation": lines[2].split(" = ")[1],
        "divisor": int(lines[3].split(" by ")[1]),
        "if_true": int(lines[4].split(" to monkey ")[1]),
        "if_false": int(lines[5].split(" to monkey ")[1]),
        "inspected_count": 0
    }


@helper.profiler
def calculate_monkey_business(monkey_mapping_input, rounds, divide=1):
    monkey_mapping = copy.deepcopy(monkey_mapping_input)
    lcm = reduce(mul, [monkey["divisor"] for monkey in monkey_mapping.values()], 1)
    for r in range(0, rounds):
        for idx in range(0, len(monkey_mapping)):
            current_monkey = monkey_mapping[idx]
            levels = current_monkey["worry_levels"]
            current_monkey["worry_levels"] = []
            for level in levels:
                current_monkey["inspected_count"] += 1
                # (a mod k*n) mod n == a mod n where k*n == 'lcm'. Relevant for part 2.
                operation = eval(f'{current_monkey["operation"].replace("old", str(level))} % {lcm}') // divide
                remainder_test = operation % current_monkey["divisor"] == 0
                next_monkey = monkey_mapping[current_monkey["if_true"] if remainder_test else current_monkey["if_false"]]
                next_monkey["worry_levels"].append(operation)
    monkey_business = reduce(mul, sorted([monkey["inspected_count"] for monkey in monkey_mapping.values()])[-2:], 1)
    return monkey_business


if __name__ == '__main__':
    content = [parse_line(element) for element in Path("data/day11.txt").read_text().split("\n\n")]
    monkey_map = {element["monkey"]: element for element in content}

    print(f"Result 1: {str(calculate_monkey_business(monkey_map, 20, 3))}")
    print(f"Result 2: {str(calculate_monkey_business(monkey_map, 10000))}")
