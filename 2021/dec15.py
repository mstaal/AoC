import numpy as np

from utils import aoc_helper as helper
from utils.global_variables import cardinal_directions
from utils.aoc_types import DijkstraGraph


def exercise(content):
    dijk_graph = {}
    for idx, elm_x in enumerate(content):
        for idy, dist_back in enumerate(elm_x):
            adjacent = helper.get_neighbours_dict(content, idx, idy, cardinal_directions, True)
            for adj, dist_to_adj in adjacent.items():
                dijk_graph[(idx, idy)] = dijk_graph.get((idx, idy), {})
                dijk_graph[adj] = dijk_graph.get(adj, {})
                dijk_graph[(idx, idy)][adj] = dist_to_adj
                dijk_graph[adj][(idx, idy)] = dist_back
    dijk = DijkstraGraph(dijk_graph)
    path_length = dijk.dijkstra((0, 0))
    result = path_length[(len(content)-1, len(content)-1)]
    return result


def add(content):
    return [[elm + 1 if elm < 9 else 1 for elm in element] for element in content]


if __name__ == '__main__':
    content = [[int(elm) for elm in element] for element in helper.split_file("day15.txt", "\n")]
    print(f"Result 1: {str(exercise(content))}")

    rotated = np.rot90(np.array(content), k=3).tolist()
    with_sides = np.rot90(rotated + add(rotated) + add(add(rotated)) + add(add(add(rotated))) + add(add(add(add(rotated))))).tolist()
    with_all = np.array(with_sides + add(with_sides) + add(add(with_sides)) + add(add(add(with_sides))) + add(add(add(add(with_sides)))))
    print(f"Result 2: {str(exercise(with_all))}")
