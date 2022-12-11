# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from utils import aoc_helper as helper


def question1Count(content):
    forward = sum([int(element.split(" ")[1]) for element in content if "forward" in element])
    down = sum([int(element.split(" ")[1]) for element in content if "down" in element])
    up = sum([int(element.split(" ")[1]) for element in content if "up" in element])
    result = forward * (down - up)
    return result

def question2Count(content):
    aim = 0
    horizontal = 0
    depth = 0
    for element in content:
        if "down" in element:
            aim += int(element.split(" ")[1])
        if "up" in element:
            aim -= int(element.split(" ")[1])
        if "forward" in element:
            x = int(element.split(" ")[1])
            horizontal += x
            depth += aim * x
    result = horizontal * depth
    return result


def calculate():
    # Use a breakpoint in the code line below to debug your script.
    content = [element for element in helper.split_file("day2.txt", "\n")]
    result1 = question1Count(content)
    result2 = question2Count(content)

    hej = ""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calculate()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
