from utils import aoc_helper as helper
from pathlib import Path


def parse_line(element):
    lines = [e.strip() for e in element.split("\n")]
    return {
        "monkey": int(lines[0].split(" ")[1][:-1]),
        "worry_levels": [int(e) for e in lines[1].split(": ")[1].split(", ")],
        "operation_new": lines[2].split(" = ")[1],
        "divisible_test": int(lines[3].split(" by ")[1]),
        "if_true": int(lines[4].split(" to monkey ")[1]),
        "if_false": int(lines[5].split(" to monkey ")[1]),
        "inspected_count": 0
    }


@helper.profiler
def part1(monkey_mapping, rounds=20, divide=3):
    for r in range(0, rounds):
        for idx in range(0, len(monkey_mapping)):
            current_monkey = monkey_mapping[idx]
            levels = current_monkey["worry_levels"]
            current_monkey["worry_levels"] = []
            for level in levels:
                current_monkey["inspected_count"] += 1
                operation = eval(current_monkey["operation_new"].replace("old", str(level))) // divide
                remainder = operation % current_monkey["divisible_test"]
                divisible_test = remainder == 0
                next_monkey = monkey_mapping[
                    current_monkey["if_true"] if divisible_test else current_monkey["if_false"]]
                next_monkey["worry_levels"].append(operation)
    inspection_counts = [monkey["inspected_count"] for _, monkey in monkey_mapping.items()]
    max_a, max_b = sorted(inspection_counts)[-2:]
    monkey_business = max_a * max_b
    return monkey_business


@helper.profiler
def part2(content_list):
    return "text"


if __name__ == '__main__':
    content = [parse_line(element) for element in Path("data/day11.txt").read_text().split("\n\n")]
    monkey_map = {element["monkey"]: element for element in content}

    print(f"Result 1: {str(part1(monkey_map))}")
    print(f"Result 2: {str(part2(content))}")
