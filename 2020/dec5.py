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


def rowNumber(word):
    return helper.baseToBase10(helper.baseToBase10(word[:7].replace("B", "1").replace("F", "0")), 10)


def seatNumber(word):
    return helper.binaryParse(word[7:], "R")


def gap(list):
    result = []
    for idx, val in enumerate(range(1, len(list)-1)):
        el1 = list[idx]
        el2 = list[val]
        if el2 - el1 > 1:
            result.append(idx)
    return result

def calculate():
    # Use a breakpoint in the code line below to debug your script.
    content = helper.splitFile("day5.txt", "\n")
    results = []

    for word in content:
        row = rowNumber(word)
        column = seatNumber(word)
        number = row * 8 + column
        results.append(number)
        results.sort()

    hejj = gap(results)
    jjfjf = max(results)
    hej = ""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(calculate())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
