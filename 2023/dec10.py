from collections import defaultdict

from utils import aoc_helper as helper
from pathlib import Path
from utils.aoc_types import DijkstraGraph
from utils.global_variables import cardinal_directions


RIGHT = ["-", "7", "J", "S"]
LEFT = ["-", "L", "F", "S"]
DOWN = ["|", "L", "J", "S"]
UP = ["|", "7", "F", "S"]


def question_1(parsed: list[list[str]]) -> int:
    graph_structure = defaultdict(dict)
    start = None
    for idx, elm_x in enumerate(parsed):
        for idy, value in enumerate(elm_x):
            if value == ".":
                continue
            if value == "S":
                start = (idx, idy)
            adjacent = helper.get_neighbours_dict(parsed, idx, idy, cardinal_directions, characters_to_skip=[None, "."])
            if value == "F" or value == "S":
                if adjacent.get((idx, idy+1), None) in RIGHT:
                    graph_structure[(idx, idy)][(idx, idy+1)] = 1
                if adjacent.get((idx+1, idy), None) in DOWN:
                    graph_structure[(idx, idy)][(idx+1, idy)] = 1
            if value == "L" or value == "S":
                if adjacent.get((idx, idy+1), None) in RIGHT:
                    graph_structure[(idx, idy)][(idx, idy+1)] = 1
                if adjacent.get((idx-1, idy), None) in UP:
                    graph_structure[(idx, idy)][(idx-1, idy)] = 1
            if value == "J" or value == "S":
                if adjacent.get((idx, idy-1), None) in LEFT:
                    graph_structure[(idx, idy)][(idx, idy-1)] = 1
                if adjacent.get((idx-1, idy), None) in UP:
                    graph_structure[(idx, idy)][(idx-1, idy)] = 1
            if value == "7" or value == "S":
                if adjacent.get((idx, idy-1), None) in LEFT:
                    graph_structure[(idx, idy)][(idx, idy-1)] = 1
                if adjacent.get((idx+1, idy), None) in DOWN:
                    graph_structure[(idx, idy)][(idx+1, idy)] = 1
            if value == "-" or value == "S":
                if adjacent.get((idx, idy-1), None) in LEFT:
                    graph_structure[(idx, idy)][(idx, idy-1)] = 1
                if adjacent.get((idx, idy+1), None) in RIGHT:
                    graph_structure[(idx, idy)][(idx, idy+1)] = 1
            if value == "|" or value == "S":
                if adjacent.get((idx-1, idy), None) in UP:
                    graph_structure[(idx, idy)][(idx-1, idy)] = 1
                if adjacent.get((idx+1, idy), None) in DOWN:
                    graph_structure[(idx, idy)][(idx+1, idy)] = 1
    dijk = DijkstraGraph(graph_structure)
    possible_lengths = {k: v for k, v in dijk.dijkstra(start).items() if v != float("inf")}
    result = max(possible_lengths.values())
    return result


@helper.profiler
def question_2(parsed: list[list[str]]) -> int:
    return sum(x for x, _ in extra)


if __name__ == '__main__':
    parsed = [list(c) for c in Path("data/day10.txt").read_text(encoding="UTF-8").split("\n")]

    question1 = question_1(parsed)
    print(f"Result 1: {str(question1)}")
    question2 = question_2(parsed)
    print(f"Result 2: {str(question2)}")
