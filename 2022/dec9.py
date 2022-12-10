from utils import AoCHelper as helper
from pathlib import Path
from utils.abcTypes import T

max_allowed_distance = T(1, 1).length()

direction_map = {"U": T(0, 1), "D": T(0, -1), "L": T(-1, 0), "R": T(1, 0)}

diagonal_directions = {T(1, 1), T(1, -1), T(-1, 1), T(-1, -1)}


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
                    x, y = rope[idx]
                    if diff_vector in [T(2, 0), T(2, 1), T(2, -1)]:
                        rope[idx+1] = T(x-1, y)
                    elif diff_vector in [T(0, 2), T(1, 2), T(-1, 2)]:
                        rope[idx+1] = T(x, y-1)
                    elif diff_vector in [T(-2, 0), T(-2, 1), T(-2, -1)]:
                        rope[idx+1] = T(x+1, y)
                    elif diff_vector in [T(0, -2), T(1, -2), T(-1, -2)]:
                        rope[idx+1] = T(x, y+1)
                    else:
                        def on_to_diagonal(d): return (rope[idx] - (rope[idx+1] + d)).length() <= max_allowed_distance
                        diagonal_direction = next(d for d in diagonal_directions if on_to_diagonal(d))
                        rope[idx+1] = rope[idx+1] + diagonal_direction
                tail_memory[idx+1].add(rope[idx+1])
    return len(tail_memory[rope_length])


if __name__ == '__main__':
    content = [(a, int(b)) for a, b in [e.split(" ") for e in Path("data/day9.txt").read_text().split("\n")]]

    print(f"Result 1: {str(calculate_unique_tail_visits(content, 1))}")
    print(f"Result 2: {str(calculate_unique_tail_visits(content, 9))}")
