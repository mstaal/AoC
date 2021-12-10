# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from collections import Counter

import pandas as pd
import AoCHelper as helper
import numpy as np
import sympy
from itertools import permutations


def calculate(right, down):
    # Use a breakpoint in the code line below to debug your script.
    input = helper.csvToList("day3.txt", "\n")
    rangeList = list(range(1, len(input)+1))
    xs = [element * down for element in rangeList][:len(input)-1]

    treeCount = 0
    yCount = 0
    for i in xs:
        line = input[i]
        yCount = helper.stringIndexLoop(line, yCount + right)
        character = line[yCount]
        answer = character == "#"
        if (answer):
            treeCount += 1
    return "(" + str(right) + "," + str(down) + "): " + str(treeCount)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(calculate(3, 1))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
