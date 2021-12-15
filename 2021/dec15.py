from utils import AoCHelper as helper
from utils.GlobalVariables import cardinal_directions
from utils.abcTypes import Graph


def exercise1(content):
    graph = Graph(len(content)*len(content))
    map = {}
    count = 0
    for idx, elm_x in enumerate(content):
        for idy, elm_y in enumerate(elm_x):
            map[(idx, idy)] = count
            count += 1
    for idx, elm_x in enumerate(content):
        for idy, elm_y in enumerate(elm_x):
            adjacent = helper.get_neighbours(content, idx, idy, cardinal_directions, True)
            for adj, value in adjacent.items():
                graph.add_edge(map[(idx, idy)], map[adj], value, elm_y)
    path_length = graph.dijkstra(0)
    result = path_length[len(content)*len(content)-1]
    return result


if __name__ == '__main__':
    content = [[int(elm) for elm in element] for element in helper.splitFile("day15.txt", "\n")]

    print(f"Result 1: {str(exercise1(content))}")
    print(f"Result 2: ")
