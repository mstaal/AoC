from utils import aoc_helper as helper
from pathlib import Path
from utils.global_variables import cardinal_directions


def get_start(parsed: list[list[str]]) -> tuple[int, int]:
    for idx, idy, value in ((idx, idy, value) for idx, elm_x in enumerate(parsed) for idy, value in enumerate(elm_x)):
        if value == "S":
            return idx, idy


@helper.profiler
def question_1(input_lst, steps_to_go=64) -> int:
    start = get_start(input_lst)
    where_to_be = set()
    queue = [(start, 0)]
    visited = set()
    while queue:
        (current_x, current_y), steps = queue.pop()
        if steps == steps_to_go:
            where_to_be.add(((current_x, current_y), steps))
            continue
        adjacent = helper.get_neighbours_dict(input_lst, current_x, current_y, cardinal_directions, True)
        for adj, value in adjacent.items():
            next_step_point = (adj, steps + 1)
            if value != "#" and not (next_step_point in visited):
                queue.append(next_step_point)
                visited.add(next_step_point)
    return len(where_to_be)


@helper.profiler
def question_2(input_lst) -> int:
    return ""


if __name__ == '__main__':
    parsed = [list(e) for e in Path("data/day21.txt").read_text(encoding="UTF-8").split("\n")]
    q1 = question_1(parsed)
    print(f"Result 1: {str(q1)}")
    q2 = question_2(parsed)
    print(f"Result 2: {str(q2)}")
