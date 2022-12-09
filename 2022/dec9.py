from utils import AoCHelper as helper
from pathlib import Path
from utils.abcTypes import T

EPSILON = 0.0000001

max_allowed_distance = T(1, 1).length() + EPSILON

direction_map = {"U": T(0, 1), "D": T(0, -1), "L": T(-1, 0), "R": T(1, 0)}

diagonal_directions = {T(1, 1), T(1, -1), T(-1, 1), T(-1, -1)}


@helper.profiler
def part1(content_list):
    tail_memory = {T(0, 0)}
    head_position = T(0, 0)
    tail_position = T(0, 0)

    for direction, count in content_list:
        direction_vector = direction_map[direction]
        for _ in range(count):
            head_position += direction_vector
            diff_vector = head_position - tail_position
            distance = diff_vector.length()
            if distance > max_allowed_distance:
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
def calculate_unique_tail_visits(content_list, rope_length):
    tail_memory = {i: {T(0, 0)} for i in range(1, rope_length+1)}
    rope = [T(0, 0) for _ in range(0, rope_length+1)]
    for direction, count in content_list:
        direction_vector = direction_map[direction]
        for _ in range(count):
            rope[0] += direction_vector
            for idx in range(0, rope_length):
                diff_vector = rope[idx] - rope[idx+1]
                distance = diff_vector.length()
                if distance > max_allowed_distance:
                    if diff_vector in [T(2, 0), T(2, 1), T(2, -1)]:
                        rope[idx+1] = T(rope[idx][0]-1, rope[idx][1])
                    elif diff_vector in [T(0, 2), T(1, 2), T(-1, 2)]:
                        rope[idx+1] = T(rope[idx][0], rope[idx][1]-1)
                    elif diff_vector in [T(-2, 0), T(-2, 1), T(-2, -1)]:
                        rope[idx+1] = T(rope[idx][0]+1, rope[idx][1])
                    elif diff_vector in [T(0, -2), T(1, -2), T(-1, -2)]:
                        rope[idx+1] = T(rope[idx][0], rope[idx][1]+1)
                    else:
                        diagonal_direction = next(d for d in diagonal_directions if
                                                  (rope[idx] - (rope[idx+1] + d)).length() < max_allowed_distance)
                        rope[idx+1] = rope[idx+1] + diagonal_direction
                tail_memory[idx+1].add(rope[idx+1])
    return len(tail_memory[rope_length])


if __name__ == '__main__':
    content = [(a, int(b)) for a, b in [e.split(" ") for e in Path("data/day9.txt").read_text().split("\n")]]

    print(f"Result 1: {str(calculate_unique_tail_visits(content, 1))}")
    print(f"Result 2: {str(calculate_unique_tail_visits(content, 9))}")
