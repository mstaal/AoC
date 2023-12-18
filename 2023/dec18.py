from utils import aoc_helper as helper
from pathlib import Path
from shapely.geometry import Polygon


def parse_line(line: list[str]):
    direction, count, colour = line
    count = int(count)
    colour = colour[1:-1]
    return direction, count, colour


def compute_lava_from_exterior_points(exterior_points: list[tuple[int, int]]) -> int:
    polygon = Polygon(exterior_points)
    boundary_points = polygon.length
    area = polygon.area
    # Pick's theorem: https://en.wikipedia.org/wiki/Pick%27s_theorem
    interior_points = area + 1 - boundary_points/2
    cubic_meters_of_lava = boundary_points + interior_points
    # Alternatively: (See: https://www.reddit.com/r/adventofcode/comments/18l0qtr/comment/kdvjfse/?utm_source=share&utm_medium=web2x&context=3)
    # polygon.buffer(0.5, join_style="mitre").area
    return int(cubic_meters_of_lava)


def compute_current_point(current: tuple[int, int], direction: str, count: int) -> tuple[int, int]:
    if direction == "R":
        return current[0] + count, current[1]
    if direction == "L":
        return current[0] - count, current[1]
    if direction == "D":
        return current[0], current[1] + count
    if direction == "U":
        return current[0], current[1] - count


@helper.profiler
def question_1(input_lst) -> int:
    current = (0, 0)
    entries = [current]
    for direction, count, colour in input_lst:
        current = compute_current_point(current, direction, count)
        entries.append(current)
    return compute_lava_from_exterior_points(entries)


@helper.profiler
def question_2(input_lst) -> int:
    current = (0, 0)
    entries = [current]
    direction_map = {0: "R", 1: "D", 2: "L", 3: "U"}
    for _, _, colour in input_lst:
        stripped = colour[1:]
        hexa, direction_proxy = stripped[:5], int(stripped[5:])
        count = int(hexa, 16)
        direction = direction_map[direction_proxy]
        current = compute_current_point(current, direction, count)
        entries.append(current)
    return compute_lava_from_exterior_points(entries)


if __name__ == '__main__':
    parsed = [parse_line(e.split(" ")) for e in Path("data/day18.txt").read_text(encoding="UTF-8").split("\n")]
    q1 = question_1(parsed)
    print(f"Result 1: {str(q1)}")
    q2 = question_2(parsed)
    print(f"Result 2: {str(q2)}")
