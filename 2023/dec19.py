from utils import aoc_helper as helper
from pathlib import Path
from math import prod


def parse_point(line: list[str]):
    stripped = [e.split("=") for e in line[1:-1].split(",")]
    x, m, a, s = tuple(int(e[1]) for e in stripped)
    return x, m, a, s


def parse_map(line: list[str]):
    name, stripped = line.split("{")
    stripped = stripped[:-1].split(",")
    end_clause = stripped[-1]
    conditions = [tuple(e.split(":")) for e in stripped[:-1]]
    return name, conditions, end_clause


@helper.profiler
def question_2(mappings) -> tuple[int, list[dict]]:
    approved = []
    queue = [("in", {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)})]
    count = -1
    while queue:
        count += 1
        current_map_id, rating_ranges = queue.pop(0)
        if current_map_id == "R":
            continue
        if current_map_id == "A":
            approved.append(rating_ranges)
            continue
        raw, end_clause = mappings[current_map_id]
        for idx, (raw_element, outcome) in enumerate(raw):
            letter, condition, bound = raw_element[0], raw_element[1], int(raw_element[2:])
            next_range_dict = dict(rating_ranges)
            in_next_queue = (outcome, next_range_dict)
            if condition == "<":
                next_range_dict[letter] = (next_range_dict[letter][0], bound-1)
                rating_ranges[letter] = (bound, rating_ranges[letter][1])
            elif condition == ">":
                next_range_dict[letter] = (bound+1, next_range_dict[letter][1])
                rating_ranges[letter] = (rating_ranges[letter][0], bound)
            queue.append(in_next_queue)
        queue.append((end_clause, dict(rating_ranges)))

    result = sum([prod([b+1-a for a, b in e.values()]) for e in approved])
    return result, approved


@helper.profiler
def question_1(coordinates_maps, points) -> int:
    accepted = []
    for x, m, a, s in points:
        x_query = [map for map in coordinates_maps if map["x"][0] <= x <= map["x"][1]]
        if len(x_query) == 0:
            continue
        m_query = [map for map in x_query if map["m"][0] <= m <= map["m"][1]]
        if len(m_query) == 0:
            continue
        a_query = [map for map in m_query if map["a"][0] <= a <= map["a"][1]]
        if len(a_query) == 0:
            continue
        s_query = [map for map in a_query if map["s"][0] <= s <= map["s"][1]]
        if len(s_query) == 0:
            continue
        accepted.append((x, m, a, s))
    total_rating = sum(sum(e) for e in accepted)
    return total_rating


if __name__ == '__main__':
    maps_raw, points_raw = [e.split("\n") for e in Path("data/day19.txt").read_text(encoding="UTF-8").split("\n\n")]
    points = [parse_point(e) for e in points_raw]
    maps = {key: (conditions, end_clause) for key, conditions, end_clause in [parse_map(e) for e in maps_raw]}
    total, coordinates_maps = question_2(maps)
    print(f"Result 2: {str(total)}")
    q1 = question_1(coordinates_maps, points)
    print(f"Result 1: {str(q1)}")

