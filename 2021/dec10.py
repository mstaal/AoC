# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import statistics

from utils import AoCHelper as helper


def is_corrupt_after_removal(element):
    return element.__contains__(">") or element.__contains__(")") or element.__contains__("]") or element.__contains__("}")


def remove_inner(element):
    length = len(element)
    text = element.replace("<>", "").replace("()", "").replace("{}", "").replace("[]", "")
    if length != len(text):
        text = remove_inner(text)
    return text


def illegal_points(text):
    calc = 0
    points = {"[)": 3, "<)": 3, "{)": 3, "(]": 57, "{]": 57, "<]": 57, "[}": 1197, "<}": 1197, "(}": 1197, "(>": 25137, "[>": 25137, "{>": 25137}
    for error, point in points.items():
        calc += text.count(error) * point
    return calc


def autocomplete_points(elm):
    calc = 0
    points = {"(": 1, "[": 2, "{": 3, "<": 4}
    for char in list(elm).__reversed__():
        calc = 5 * calc + points[char]
    return calc


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    content = [element for element in helper.splitFile("day10.txt", "\n")]
    removed = [remove_inner(element) for element in content]
    corrupted = [el for el in removed if is_corrupt_after_removal(el)]
    exercise1 = sum([illegal_points(text) for text in corrupted])
    print(f"Result 1: {str(exercise1)}")

    incomplete = [el for el in removed if not is_corrupt_after_removal(el)]
    exercise2 = statistics.median([autocomplete_points(elm) for elm in incomplete])
    print(f"Result 2: {str(exercise2)}")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
