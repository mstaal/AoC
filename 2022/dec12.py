from utils import aoc_helper as helper
from pathlib import Path

from utils.aoc_types import DijkstraGraph
from utils.global_variables import cardinal_directions


def get_dijkstra_graph(content_list, add_to_graph_condition):
    graph_structure = {}
    for idx, elm_x in enumerate(content_list):
        for idy, value in enumerate(elm_x):
            adjacent = helper.get_neighbours_dict(content_list, idx, idy, cardinal_directions, True)
            for adj, adj_value in adjacent.items():
                graph_structure[(idx, idy)] = graph_structure.get((idx, idy), {})
                graph_structure[adj] = graph_structure.get(adj, {})
                if add_to_graph_condition(value, adj_value):
                    graph_structure[(idx, idy)][adj] = 1
    return DijkstraGraph(graph_structure)


@helper.profiler
def part1(numeric, start, end):
    graph = get_dijkstra_graph(numeric, lambda val, adj_val: adj_val < val + 2)
    return graph.dijkstra(start)[end]


@helper.profiler
def part2(numeric, end):
    numeric_mapping = {(idx, idy): val for idx, row in enumerate(numeric) for idy, val in enumerate(row)}
    graph = get_dijkstra_graph(numeric, lambda val, adj_val: val < adj_val + 2)
    return min(graph.dijkstra(end)[start] for start in {a for a, val in numeric_mapping.items() if val == 0})


if __name__ == '__main__':
    content = [[d for d in e] for e in Path("data/day12.txt").read_text().split("\n")]
    start_end = {val: (idx, idy) for idx, e in enumerate(content) for idy, val in enumerate(e) if val in ["S", "E"]}
    numeric_repr = [[ord(d)-97 for d in e] for e in [[d.replace("E", "z").replace("S", "a") for d in e] for e in content]]

    print(f"Result 1: {str(part1(numeric_repr, start_end['S'], start_end['E']))}")

    print(f"Result 2: {str(part2(numeric_repr, start_end['E']))}")
