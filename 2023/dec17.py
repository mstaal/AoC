from utils import aoc_helper as helper
from pathlib import Path
from utils.aoc_types import T
from heapq import heappush, heappop


START = T(0, 0)
RIGHT = T(1, 0)
LEFT = T(-1, 0)
UP = T(0, -1)
DOWN = T(0, 1)

MOVES = {
    START: (RIGHT, DOWN),
    RIGHT: (UP, DOWN),
    LEFT: (UP, DOWN),
    UP: (LEFT, RIGHT),
    DOWN: (LEFT, RIGHT),
}


def question_1(input_lst, min_cap, max_cap) -> int:
    start_x, start_y = (0, 0)
    end_x, end_y = (len(input_lst[0])-1, len(input_lst)-1)
    queue = []
    visit_bookkeeper = set()
    heats = {T(0, 0): 0}
    heappush(queue, (0, (T(start_x, start_y), START)))

    result = None
    while queue:
        loss, (current_position, direction) = heappop(queue)
        if current_position == T(end_x, end_y):
            result = loss
            break
        new_directions = MOVES[direction]
        if (current_position, direction) in visit_bookkeeper:
            continue
        visit_bookkeeper.add((current_position, direction))
        for new_direction in new_directions:
            # Remember to increment total at each step.
            total_loss = loss
            for i in range(1, max_cap+1):
                new_pos_x, new_pos_y = current_position + new_direction * i
                new_position = T(new_pos_x, new_pos_y)
                new_node = (new_position, new_direction)
                if 0 <= new_pos_x <= end_x and 0 <= new_pos_y <= end_y:
                    total_loss = total_loss + input_lst[new_pos_y][new_pos_x]
                    # Even if we are not pushing the start nodes, we still have to increment the total.
                    if i >= min_cap:
                        # If we have arrived here before in the same direction, we only preserve the optimum.
                        if total_loss < heats.get(new_node, float("inf")):
                            heats[new_node] = total_loss
                            heappush(queue, (total_loss, new_node))
    return result


@helper.profiler
def question_2(input_lst) -> int:
    return question_1(input_lst, 4, 10)


if __name__ == '__main__':
    parsed = [[int(i) for i in e] for e in Path("data/day17.txt").read_text(encoding="UTF-8").split("\n")]
    q1 = question_1(parsed, 1, 3)
    print(f"Result 1: {str(q1)}")
    q2 = question_2(parsed)
    print(f"Result 2: {str(q2)}")
