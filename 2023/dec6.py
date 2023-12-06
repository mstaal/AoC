from utils import aoc_helper as helper
from pathlib import Path
from math import sqrt, ceil, floor
import numpy as np

EPSILON = 1e-12


def parse_content(cnt):
    time_line, distance_line = cnt
    times = [int(e) for e in time_line.replace("Time: ", "").strip().split(" ") if e != ""]
    distances = [int(e) for e in distance_line.replace("Distance: ", "").strip().split(" ") if e != ""]
    return times, distances


def question_1(times: list[int], distances: list[int]) -> int:
    combined = list(zip(times, distances))
    solutions = [((t-sqrt(t**2-4*d))/2+EPSILON, (t+sqrt(t**2-4*d))/2-EPSILON) for (t, d) in combined]
    solutions_rounded = [(ceil(a), floor(b)) for (a, b) in solutions]
    number_of_solutions = [b-a+1 for (a, b) in solutions_rounded]
    result = np.prod(number_of_solutions)
    return result


@helper.profiler
def question_2(times: list[int], distances: list[int]) -> int:
    times_single = int("".join([str(e) for e in times]))
    distances_single = int("".join([str(e) for e in distances]))
    solution_a, solution_b = ((times_single-sqrt(times_single**2-4*distances_single))/2+EPSILON,
                 (times_single+sqrt(times_single**2-4*distances_single))/2-EPSILON)
    solution_a_rounded, solution_b_rounded = (ceil(solution_a), floor(solution_b))
    result = solution_b_rounded - solution_a_rounded + 1
    return result


if __name__ == '__main__':
    times, distances = parse_content(Path("data/day6.txt").read_text(encoding="UTF-8").split("\n"))

    question1 = question_1(times, distances)
    print(f"Result 1: {str(question1)}")
    question2 = question_2(times, distances)
    print(f"Result 2: {str(question2)}")
