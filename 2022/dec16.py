from utils import aoc_helper as helper
from pathlib import Path
from utils.aoc_types import T
from shapely import Polygon


def parse_input(element):
    first, second = element.split("; ")
    valve_part, flow_rate = first.split(" has flow rate=")
    _, valve_part = valve_part.split(" ")
    flow_rate = int(flow_rate)
    a, *tunnels = second.split(", ")
    tunnels = [a.split(" ")[-1]] + tunnels
    return valve_part, flow_rate, tunnels


def part1(content_input, choice, history):
    current = content_input[choice]
    if current["valve"] in history:
        return {"valve": choice, "rate": current["rate"], "next": None}
    return {"valve": choice, "rate": current["rate"],
            "next": {a: part1(content_input, a, history + [choice]) for a in current["tunnels"]}}


@helper.profiler
def part2(content_input):
    return "first * second"


if __name__ == '__main__':
    content = [parse_input(e) for e in Path("data/day16-sample.txt").read_text().split("\n")]
    content_map = {x: {"valve": x, "rate": y, "tunnels": z} for x, y, z in content}

    hej = part1(content_map, "AA", [])


    print(f"""Result 1: {str(part1(content_map, "AA", []))}""")
    print(f"Result 2: {str(part2(content))}")
