from utils import AoCHelper as helper
from utils.GlobalVariables import cardinal_directions
from utils.abcTypes import Dijkstra


def exercise1(content):
    dijk_graph = {}
    for idx, elm_x in enumerate(content):
        for idy, elm_y in enumerate(elm_x):
            adjacent = helper.get_neighbours(content, idx, idy, cardinal_directions, True)
            for adj, value in adjacent.items():
                dijk_graph[(idx, idy)] = dijk_graph.get((idx, idy), {})
                dijk_graph[adj] = dijk_graph.get(adj, {})
                dijk_graph[(idx, idy)][adj] = value
                dijk_graph[adj][(idx, idy)] = elm_y
    dijk = Dijkstra(dijk_graph)
    path_length = dijk.dijkstra((0, 0))
    result = path_length[(len(content)-1, len(content)-1)]
    return result


if __name__ == '__main__':
    content = [[int(elm) for elm in element] for element in helper.splitFile("day15.txt", "\n")]

    print(f"Result 1: {str(exercise1(content))}")
    print(f"Result 2: ")
