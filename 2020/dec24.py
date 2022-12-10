import re
import hexutil as hex
import numpy as np
from utils import aoc_helper as helper

directions = {
    'e': (2, 0),
    'se': (1, -1),
    'sw': (-1, -1),
    'w': (-2, 0),
    'nw': (-1, 1),
    'ne': (1, 1)
}


def neighbors(tile):
    yield from ((tile[0] + x, tile[1] + y) for (x, y) in directions.values())


def regexSplitter(text, regex):
    result = []
    while len(text) > 0:
        match = re.match(regex, text)
        piece = text[match.start():match.end()]
        result.append(piece)
        text = text[match.end():]
    return result


def walk(matches):
    coordinates = []
    for match in matches:
        vector = np.array([0, 0])
        for dir in match:
            if dir == "e":
                vector += np.array([2, 0])
            if dir == "w":
                vector += np.array([-2, 0])
            if dir == "ne":
                vector += np.array([1, 1])
            if dir == "nw":
                vector += np.array([-1, 1])
            if dir == "se":
                vector += np.array([1, -1])
            if dir == "sw":
                vector += np.array([-1, -1])
        coordinates.append(tuple(vector))
    return coordinates


def walk2(matches):
    coordinates = []
    for match in matches:
        vector = 0
        for dir in match:
            if dir == "e":
                vector += 1
            if dir == "w":
                vector += -1
            if dir == "ne":
                vector += 1j
            if dir == "nw":
                vector += -1 + 1j
            if dir == "se":
                vector += 1 - 1j
            if dir == "sw":
                vector += -1j
        coordinates.append(vector)
    return coordinates


def nextDay(current):
    next = {}
    affected = current.copy()
    for key, value in current.items():
        nb = neighbors(key)
        for el in nb:
            affected[el] = True

    for key, value in affected.items():
        black = current.get(key, False)
        numNeighbors = len([n for n in current.keys() if n in neighbors(key)])
        if black and numNeighbors in (1, 2):
            next[key] = True
        elif not black and numNeighbors == 2:
            next[key] = True
    return next


def maxAbsolute(day):
    first = max(abs(element[0]) for element in day.keys()) + 1
    second = max(abs(element[1]) for element in day.keys()) + 1
    return int((2*max(first, second))/2 + 2)


def generateGrid(maxi):
    lst = []
    second = list(range(-maxi, maxi + 1))
    for right in second:
        left = -(maxi + (0 if (maxi + right) % 2 == 0 else 1))
        while left < maxi+1:
            lst.append(hex.Hex(left, right))
            left += 2
    return lst


def calculate():
    # Use a breakpoint in the code line below to debug your script.
    # Part 1
    content = helper.splitFile("day24.txt", "\n")
    regex = "(e|se|sw|w|nw|ne)"
    matches = [regexSplitter(element, regex) for element in content]
    coordinates = walk(matches)
    counts = {element: coordinates.count(element) for element in coordinates}
    blackCount = {element: count for element, count in counts.items() if count % 2 == 1}

    # Part 2
    day1 = {element: True for element, count in counts.items()}
    maxi = maxAbsolute(day1)
    day2 = nextDay(day1)
    maxi2 = maxAbsolute(day2)
    nextDay(day2)
    hfhhf = ""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calculate()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
