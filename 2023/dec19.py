from utils import aoc_helper as helper
from pathlib import Path


def parse_point(line: list[str]):
    stripped = [e.split("=") for e in line[1:-1].split(",")]
    dictionary = {e[0]: int(e[1]) for e in stripped}
    return dictionary


def define_piecewise(start):
    clause, outcome = start
    if "<" in clause:
        letter, right = clause.split("<")
        right = float(right)

        def piecewise(value):
            return outcome if value < right else None

    else:
        letter, right = clause.split(">")
        right = float(right)

        def piecewise(value):
            return outcome if value > right else None

    return letter, piecewise


def parse_map(line: list[str]):
    name, stripped = line.split("{")
    stripped = stripped[:-1].split(",")
    end_clause = stripped[-1]
    starts = [e.split(":") for e in stripped[:-1]]
    functions = [define_piecewise(start) for start in starts]

    def composition(input_values: dict[str, int]):
        for letter, function in functions:
            value = input_values[letter]
            result = function(value)
            if result:
                return result
        return end_clause

    return name, composition


@helper.profiler
def question_1(mappings, points) -> int:
    accepted = []
    for point in points:
        next_map_id = "in"
        while next_map_id not in {"A", "R"}:
            current_map = mappings[next_map_id]
            next_map_id = current_map(point)
        if next_map_id == "A":
            accepted.append(point)
    total_rating = sum(sum(e.values()) for e in accepted)
    return total_rating


@helper.profiler
def question_2(mappings, points) -> int:
    return ""


if __name__ == '__main__':
    maps_raw, points_raw = [e.split("\n") for e in Path("data/day19.txt").read_text(encoding="UTF-8").split("\n\n")]
    points = [parse_point(e) for e in points_raw]
    maps = {key: value for key, value in [parse_map(e) for e in maps_raw]}
    q1 = question_1(maps, points)
    print(f"Result 1: {str(q1)}")
    q2 = question_2(maps, points)
    print(f"Result 2: {str(q2)}")
