from utils import aoc_helper as helper
import urllib.parse

# Chinese remainder theorem


def first_exercise(min_required_timestamp, second_line):
    departure_bus_pairs = []
    lst = [int(number) for number in second_line.replace("x,", "").split(",")]
    for element in lst:
        sample = [i * element for i in range(0, min_required_timestamp)]
        filter_res = min([i for i in sample if i >= min_required_timestamp])
        departure_bus_pairs.append((filter_res, element))
    minimal_possible_time, bus_id = min(departure_bus_pairs, key=lambda x: x[0])
    res = (minimal_possible_time - min_required_timestamp) * bus_id
    return res


def second_calc(second_line):
    time_to_indices = []
    lst = [number for number in second_line.split(",")]
    for idx, element in enumerate(lst):
        if element != "x":
            time_to_indices.append((int(element), idx))
    return time_to_indices


def second_exercise(time_to_indices):
    crt_equation = ""
    for time, bus_index in time_to_indices:
        crt_equation += f"(a + {str(bus_index)}) mod {str(time)} = 0, "
    chinese_remainder_equation = crt_equation[:-2]
    return chinese_remainder_equation


def second_exercise_alt(time_to_indices):
    n_bus_index_list = [n for n, _ in time_to_indices]
    a_time_list = [-1 * a for _, a in time_to_indices]
    return helper.chinese_remainder(n_bus_index_list, a_time_list)


def calculate():
    # Use a breakpoint in the code line below to debug your script.
    timestamp, secondLine = helper.split_file("day13.txt", "\n")
    print(f"Result 1: {first_exercise(int(timestamp), secondLine)}")

    time_to_indices = second_calc(secondLine)
    wolfram_equation = second_exercise(time_to_indices)
    print(f"Result 2 (Wolfram): {wolfram_equation}")
    print(f"Result 2 (Wolfram-query): {helper.wolfram_alpha_query(wolfram_equation)}")

    print(f"Result 2 (Alternative): {second_exercise_alt(time_to_indices)}")


if __name__ == '__main__':
    calculate()
