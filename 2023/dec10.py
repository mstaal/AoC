from collections import defaultdict
from copy import deepcopy
from utils import aoc_helper as helper
from pathlib import Path
from utils.aoc_types import DijkstraGraph
from utils.global_variables import cardinal_directions
from shapely.geometry import Polygon


RIGHT = ["-", "7", "J", "S"]
LEFT = ["-", "L", "F", "S"]
DOWN = ["|", "L", "J", "S"]
UP = ["|", "7", "F", "S"]


def get_dijkstra_graph(parsed: list[list[str]]) -> tuple[DijkstraGraph, tuple[int, int]]:
    graph_structure = defaultdict(dict)
    start = None
    for idx, idy, value in ((idx, idy, value) for idx, elm_x in enumerate(parsed) for idy, value in enumerate(elm_x)):
        if value == "S":
            start = (idx, idy)
        adjacent = helper.get_neighbours_dict(parsed, idx, idy, cardinal_directions)
        if value in LEFT and adjacent.get((idx, idy + 1), None) in RIGHT:
            graph_structure[(idx, idy)][(idx, idy + 1)] = 1
        if value in RIGHT and adjacent.get((idx, idy - 1), None) in LEFT:
            graph_structure[(idx, idy)][(idx, idy - 1)] = 1
        if value in UP and adjacent.get((idx + 1, idy), None) in DOWN:
            graph_structure[(idx, idy)][(idx + 1, idy)] = 1
        if value in DOWN and adjacent.get((idx - 1, idy), None) in UP:
            graph_structure[(idx, idy)][(idx - 1, idy)] = 1
    dijk = DijkstraGraph(graph_structure)
    return dijk, start


@helper.profiler
def question_1(parsed: list[list[str]]) -> tuple[int, DijkstraGraph, tuple[int, int], tuple[int, int]]:
    dijk, start = get_dijkstra_graph(parsed)
    starts = dijk.dijkstra(start)
    possible_lengths = {k: v for k, v in starts.items() if v != float("inf")}
    end = next((k for k in possible_lengths.keys() if possible_lengths[k] == max(possible_lengths.values())), None)
    distance = starts[end]
    return distance, dijk, start, end


@helper.profiler
def question_2(distance: int, dijk: DijkstraGraph, start: tuple[int, int], end: tuple[int, int]) -> int:
    _, path = dijk.dijkstra_with_path(start)[end]
    parsed_altered = deepcopy(parsed)
    parsed_altered[path[-2][0]][path[-2][1]] = "."
    dijk_alternative, _ = get_dijkstra_graph(parsed_altered)
    _, path_alt = dijk_alternative.dijkstra_with_path(start)[end]
    cycle = path + list(reversed(path_alt))

    # Pick's theorem: https://en.wikipedia.org/wiki/Pick%27s_theorem
    interior_count = int(Polygon(cycle).area - distance + 1)
    return interior_count


if __name__ == '__main__':
    parsed = [list(c) for c in Path("data/day10.txt").read_text(encoding="UTF-8").split("\n")]

    distance, dijk, start, end = question_1(parsed)
    print(f"Result 1: {str(distance)}")
    question2 = question_2(distance, dijk, start, end)
    print(f"Result 2: {str(question2)}")
