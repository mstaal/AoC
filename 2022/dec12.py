from utils import aoc_helper as helper
from pathlib import Path

from utils.aoc_types import Dijkstra
from utils.global_variables import cardinal_directions


def get_dijkstra_graph(content_list, weight_lambda):
    dijk_graph = {}
    for idx, elm_x in enumerate(content_list):
        for idy, value in enumerate(elm_x):
            adjacent = helper.get_neighbours_dict(content_list, idx, idy, cardinal_directions, True)
            for adj, adj_value in adjacent.items():
                dijk_graph[(idx, idy)] = dijk_graph.get((idx, idy), {})
                dijk_graph[adj] = dijk_graph.get(adj, {})
                if weight_lambda(value, adj_value):
                    dijk_graph[(idx, idy)][adj] = 1
    return Dijkstra(dijk_graph)


@helper.profiler
def part1(content_list, start, end):
    dijk = get_dijkstra_graph(content_list, lambda val, adj_val: adj_val in range(0, val + 2))
    path_length_from_start = dijk.dijkstra(start)
    shortest_length_to_end = path_length_from_start[end]
    return shortest_length_to_end


@helper.profiler
def part2(map_numeric_mapping, map_numeric, end):
    possible_starts = {a for a, val in map_numeric_mapping.items() if val == 0}
    shortest_paths_from_starts = {start: part1(map_numeric, start, end) for start in possible_starts}
    minimal_choice = min(shortest_paths_from_starts.values())
    return minimal_choice


if __name__ == '__main__':
    content = [[d for d in e] for e in Path("data/day12.txt").read_text().split("\n")]
    start_end = {val: (idx, idy) for idx, e in enumerate(content) for idy, val in enumerate(e) if val in ["S", "E"]}
    map_raw = [[d.replace("E", "z").replace("S", "a") for d in e] for e in content]
    to_numeric = [[ord(d)-97 for d in e] for e in map_raw]
    to_numeric_dict = {(idx, idy): val for idx, row in enumerate(to_numeric) for idy, val in enumerate(row)}

    print(f"Result 1: {str(part1(to_numeric, start_end['S'], start_end['E']))}")

    print(f"Result 2: {str(part2(to_numeric_dict, to_numeric, start_end['E']))}")
