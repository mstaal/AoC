import statistics

from utils import aoc_helper as helper


def remove_inner(element):
    length = len(element)
    text = element.replace("<>", "").replace("()", "").replace("{}", "").replace("[]", "")
    if length != len(text):
        text = remove_inner(text)
    return text


def illegal_points(text):
    calc = 0
    points = {")": 3, "]": 57, "}": 1197, ">": 25137}
    for error, point in points.items():
        calc += text.count(error) * point
    return calc


def autocomplete_points(elm):
    calc = 0
    points = {"(": 1, "[": 2, "{": 3, "<": 4}
    for char in list(elm).__reversed__():
        calc = 5 * calc + points[char]
    return calc


if __name__ == '__main__':
    content = [element for element in helper.split_file("day10.txt", "\n")]
    removed = [remove_inner(element) for element in content]
    is_corrupt_after_removal = lambda el: helper.contains_any(el, [">", ")", "]", "}"])
    corrupted = [el for el in removed if is_corrupt_after_removal(el)]
    exercise1 = sum([illegal_points(text) for text in corrupted])
    print(f"Result 1: {str(exercise1)}")

    incomplete = [el for el in removed if not is_corrupt_after_removal(el)]
    exercise2 = statistics.median([autocomplete_points(elm) for elm in incomplete])
    print(f"Result 2: {str(exercise2)}")
