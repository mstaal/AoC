# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from collections import Counter

import pandas as pd
import AoCHelper as helper
import numpy as np
import sympy
import re
from itertools import permutations


def nonValidElements(content, length):
    collections = [content[i:i + length] for i in range(0, len(content), 1)]
    result = []
    for idx, val in enumerate(range(length, len(collections)-length)):
        number = collections[val][0]
        if number not in [element[0] + element[1] for element in list(permutations(collections[idx], 2))]:
            result.append(number)
    return result


def relevantMinMax(content, checkFilter):
    for length in range(2, len(content)):
        intervals = [content[i:i + length] for i in range(0, len(content), 1)]
        sums = [sum(element) for element in intervals]
        if checkFilter in sums:
            interval = intervals[sums.index(checkFilter)]
            return min(interval) + max(interval), True
    return -1, False


def calculate():
    # Use a breakpoint in the code line below to debug your script.
    content = [int(element) for element in helper.splitFile("day9.txt", "\n")]
    firstResult = nonValidElements(content, 25)[0]

    secondResult = relevantMinMax(content, firstResult)[0]
    hej = ""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(calculate())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
