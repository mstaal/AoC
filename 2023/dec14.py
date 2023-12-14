from collections import Counter
from utils import aoc_helper as helper
from pathlib import Path


def count_rock_load_per_column(c):
    measure = 0
    for idx, char in enumerate(c):
        if char == "O":
            measure += len(c)-idx
    return measure


def reposition_rocks_in_column(c):
    splitted = c.split("#")
    bookkeeping = []
    for seq in splitted:
        number_of_os = seq.count("O")
        number_of_dots = seq.count(".")
        bookkeeping.append(f"""{"O"*number_of_os}{"."*number_of_dots}#""")
    new_column = "".join(bookkeeping)[:-1]
    return new_column


def rotate_90_degrees(c):
    return ["".join(reversed([e[idx] for e in c])) for idx in range(len(c[0]))]


def reverse_row_columns(p):
    return ["".join([e[idx] for e in p]) for idx in range(len(p[0]))]


cache = {}


def do_cycle(row_based):
    if "".join(row_based) in cache:
        return cache["".join(row_based)]

    column_format = reverse_row_columns(row_based)
    north = reverse_row_columns([reposition_rocks_in_column(col) for col in column_format])

    west_column_format = reverse_row_columns(rotate_90_degrees(north))
    west = reverse_row_columns([reposition_rocks_in_column(col) for col in west_column_format])

    south_column_format = reverse_row_columns(rotate_90_degrees(west))
    south = reverse_row_columns([reposition_rocks_in_column(col) for col in south_column_format])

    east_column_format = reverse_row_columns(rotate_90_degrees(south))
    east = reverse_row_columns([reposition_rocks_in_column(col) for col in east_column_format])

    back_to_north = rotate_90_degrees(east)
    load = sum([count_rock_load_per_column(c) for c in reverse_row_columns(back_to_north)])
    cache["".join(row_based)] = back_to_north, load
    return back_to_north, load


@helper.profiler
def question_1(p) -> int:
    repositioned = [reposition_rocks_in_column(c) for c in reverse_row_columns(p)]
    total = sum([count_rock_load_per_column(c) for c in repositioned])
    return total


def detect_cycle(history: list) -> tuple[int, int]:
    value_count = Counter(history)
    loop_values = [k for k, v in value_count.items() if v > 1]
    beginning, end = loop_values[0], loop_values[-1]
    beginning_indices = [idx for idx, elm in enumerate(history) if elm == beginning]
    beginning_idx, end_idx = -1, -1,
    for current, upcoming in helper.pairwise(beginning_indices):
        if upcoming != current+1:
            beginning_idx = upcoming
            break
    for elm in beginning_indices:
        if elm <= beginning_idx:
            continue
            # Check that they agree on enough elements... :-) (30 is a magic number)
        if history[beginning_idx:beginning_idx+30] == history[elm:elm+30]:
            end_idx = elm-1
            break
    return beginning_idx, end_idx


@helper.profiler
def question_2(p) -> int:
    load_value_history = []
    row_rep = p
    # Compute enough elements to detect the cycle
    for _ in range(200):
        row_rep, val = do_cycle(row_rep)
        load_value_history.append(val)
    beginning_idx, end_idx = detect_cycle(load_value_history)
    period = end_idx+1-beginning_idx
    value_of_interest = load_value_history[beginning_idx+((1000000000-beginning_idx) % period)-1]
    return value_of_interest


if __name__ == '__main__':
    parsed = Path("data/day14.txt").read_text(encoding="UTF-8").split("\n")
    columnss = reverse_row_columns(reverse_row_columns(parsed))
    q1 = question_1(parsed)
    print(f"Result 1: {str(q1)}")
    q2 = question_2(parsed)
    print(f"Result 2: {str(q2)}")
