from utils import AoCHelper as helper
from pathlib import Path
import numpy as np
from utils.abcTypes import T


direction_map = {"U": T(0, 1), "D": T(0, -1), "L": T(-1, 0), "R": T(1, 0)}

@helper.profiler
def part1(content_list):
    tail_memory = {T(0, 0)}
    head_position = T(0, 0)
    tail_position = T(0, 0)

    for direction, count in content_list:
        max_allowed_distance = T(1, 1).length() + 0.0000001
        for idx, _ in enumerate(range(count)):
            direction_vector = direction_map[direction]
            head_position += direction_vector
            diff_vector = head_position - tail_position
            distance = diff_vector.length()
            if distance > max_allowed_distance:
                diff_vector = head_position - tail_position
                if diff_vector in [T(2, 0), T(2, 1), T(2, -1)]:
                    tail_position = T(head_position[0]-1, head_position[1])
                elif diff_vector in [T(0, 2), T(1, 2), T(-1, 2)]:
                    tail_position = T(head_position[0], head_position[1]-1)
                elif diff_vector in [T(-2, 0), T(-2, 1), T(-2, -1)]:
                    tail_position = T(head_position[0]+1, head_position[1])
                elif diff_vector in [T(0, -2), T(1, -2), T(-1, -2)]:
                    tail_position = T(head_position[0], head_position[1]+1)
                tail_memory.add(tail_position)
    return len(tail_memory)


@helper.profiler
def part2(content_list):
    return "max_score"


if __name__ == '__main__':
    content = [(a, int(b)) for a, b in [e.split(" ") for e in Path("data/day9.txt").read_text().split("\n")]]

    print(f"Result 1: {str(part1(content))}")
    print(f"Result 2: {str(part2(content))}")
