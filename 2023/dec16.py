from utils import aoc_helper as helper
from pathlib import Path
from utils.aoc_types import T


RIGHT = T(1, 0)
LEFT = T(-1, 0)
UP = T(0, -1)
DOWN = T(0, 1)


class CustomQueue:
    def __init__(self, queue=None):
        if queue is not None:
            self.queue = queue
        else:
            self.queue = []
        self.history = set(self.queue)

    def pop(self):
        return self.queue.pop()

    def append(self, item):
        if item not in self.history:
            self.history.add(item)
            self.queue.append(item)

    def __bool__(self):
        return bool(self.queue)


def question_1(input_lst, start, direction) -> int:
    energized = set()
    queue = CustomQueue([(start, direction)])
    while queue:
        current, direction = queue.pop()
        current = current + direction
        x_current, y_current = current
        if y_current < 0 or y_current >= len(input_lst) or x_current < 0 or x_current >= len(input_lst[0]):
            continue
        if current not in energized:
            energized.add(current)
        element = input_lst[current[1]][current[0]]
        if element == ".":
            queue.append((current, direction))
        if element == "/":
            if direction == RIGHT:
                direction = UP
            elif direction == LEFT:
                direction = DOWN
            elif direction == UP:
                direction = RIGHT
            elif direction == DOWN:
                direction = LEFT
            queue.append((current, direction))
        elif element == "\\":
            if direction == RIGHT:
                direction = DOWN
            elif direction == LEFT:
                direction = UP
            elif direction == UP:
                direction = LEFT
            elif direction == DOWN:
                direction = RIGHT
            queue.append((current, direction))
        elif element == "|":
            if direction == RIGHT or direction == LEFT:
                queue.append((current, UP))
                queue.append((current, DOWN))
            else:
                queue.append((current, direction))
        elif element == "-":
            if direction == UP or direction == DOWN:
                queue.append((current, LEFT))
                queue.append((current, RIGHT))
            else:
                queue.append((current, direction))
    result = len(energized)
    return result


@helper.profiler
def question_2(input_lst) -> int:
    top_runs = [question_1(input_lst, T(x, -1), DOWN) for x in range(0, len(input_lst[0]))]
    bottom_runs = [question_1(input_lst, T(x, -1), UP) for x in range(0, len(input_lst[0]))]
    right_runs = [question_1(input_lst, T(len(input_lst[0]), y), LEFT) for y in range(0, len(input_lst))]
    left_runs = [question_1(input_lst, T(-1, y), RIGHT) for y in range(0, len(input_lst))]
    result = max(top_runs + bottom_runs + right_runs + left_runs)
    return result


if __name__ == '__main__':
    parsed = Path("data/day16.txt").read_text(encoding="UTF-8").split("\n")
    q1 = question_1(parsed, LEFT, RIGHT)
    print(f"Result 1: {str(q1)}")
    q2 = question_2(parsed)
    print(f"Result 2: {str(q2)}")
