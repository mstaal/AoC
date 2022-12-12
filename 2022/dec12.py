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
def part1(numeric, start, end):
    graph = get_dijkstra_graph(numeric, lambda val, adj_val: adj_val in range(0, val + 2))
    shortest_lengths_from_start = graph.dijkstra(start)
    return shortest_lengths_from_start[end]


@helper.profiler
def part2(numeric, end):
    numeric_mapping = {(idx, idy): val for idx, row in enumerate(numeric) for idy, val in enumerate(row)}
    possible_starts = {a for a, val in numeric_mapping.items() if val == 0}
    graph = get_dijkstra_graph(numeric, lambda val, adj_val: val in range(0, adj_val + 2))
    minimal_choice = min(graph.dijkstra(end)[start] for start in possible_starts)
    return minimal_choice


if __name__ == '__main__':
    content = [[d for d in e] for e in Path("data/day12.txt").read_text().split("\n")]
    start_end = {val: (idx, idy) for idx, e in enumerate(content) for idy, val in enumerate(e) if val in ["S", "E"]}
    numeric_repr = [[ord(d)-97 for d in e] for e in [[d.replace("E", "z").replace("S", "a") for d in e] for e in content]]

    print(f"Result 1: {str(part1(numeric_repr, start_end['S'], start_end['E']))}")

    print(f"Result 2: {str(part2(numeric_repr, start_end['E']))}")
