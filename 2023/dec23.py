from utils import aoc_helper as helper
from pathlib import Path
from utils.global_variables import cardinal_directions


def get_start_and_end(parsed: list[list[str]]) -> tuple[tuple[int, int], tuple[int, int]]:
    start, end = None, None
    for idx, idy, value in ((idx, idy, value) for idx, elm_x in enumerate(parsed) for idy, value in enumerate(elm_x)):
        if idx == 0 and value == ".":
            start = (idx, idy)
        if idx == len(parsed) - 1 and value == ".":
            end = (idx, idy)
    return start, end


@helper.profiler
def question_1(input_lst, part_one=True) -> int:
    start, end = get_start_and_end(input_lst)
    queue = [[start]]
    candidates = []
    visited = dict()
    while queue:
        path = queue.pop().copy()
        current_end = path[-1]
        if current_end == end:
            candidates.append(path)
            continue
        current_value = input_lst[current_end[0]][current_end[1]]
        if part_one and current_value in {">", "<", "^", "v"}:
            if current_value == ">":
                next_point = (current_end[0], current_end[1] + 1)
            elif current_value == "<":
                next_point = (current_end[0], current_end[1] - 1)
            elif current_value == "^":
                next_point = (current_end[0] - 1, current_end[1])
            elif current_value == "v":
                next_point = (current_end[0] + 1, current_end[1])
            next_points = [next_point]
        else:
            adjacent = helper.get_neighbours_dict(input_lst, current_end[0], current_end[1], cardinal_directions)
            next_points = [k for k, v in adjacent.items() if v not in {"#", None}]
        next_points = [e for e in next_points if e not in path]

        for adj in next_points:
            if visited.get(adj, 0) >= len(path) + 1:
                continue
            else:
                visited[adj] = len(path) + 1
                next_path = path.copy()
                next_path.append(adj)
                queue.append(next_path)
    result = max(len(e) for e in candidates) - 1
    return result


@helper.profiler
def question_2(input_lst) -> int:
    result = question_1(input_lst, False)
    return ""


if __name__ == '__main__':
    parsed = [list(e) for e in Path("data/day23.txt").read_text(encoding="UTF-8").split("\n")]
    q1 = question_1(parsed)
    print(f"Result 1: {str(q1)}")
    q2 = question_2(parsed)
    print(f"Result 2: {str(q2)}")
