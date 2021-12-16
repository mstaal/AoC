# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from collections import Counter

import pandas as pd
from utils import AoCHelper as helper
import numpy as np
import sympy
import itertools
import re
import copy
from itertools import permutations, combinations, chain, product

def bingoGame(numbers, elm):
    final = None
    finalNumber = None
    finalIndex = -1
    numberCount = 0
    for num in numbers:
        numberCount += 1
        current = elm[0]
        for idx in range(0, len(current)):
            for idy in range(0, len(current)):
                candidate = current[idx][idy]
                if candidate[0] == num:
                    current[idx][idy] = (current[idx][idy][0], True)
        array = np.array(current)
        iteration = array.tolist() + np.rot90(array).tolist()
        for row in iteration:
            count = len([el for el in row if el[1]])
            if count >= 5:
                final = array.tolist()
                finalNumber = num
                finalIndex = elm[2]
                break
        if final is not None:
            break
    summing = sum([element[0] for element in helper.flatten(final) if not element[1]])
    result = summing * finalNumber
    return (result, finalIndex, numberCount)


def firstExercise(numbers, content):
    results = [bingoGame(numbers, element) for element in content]
    result = [element for element in results if element[2] == min([element[2] for element in results])]
    return result


def secondExercise(numbers, content):
    results = [bingoGame(numbers, element) for element in content]
    result = [element for element in results if element[2] == max([element[2] for element in results])]
    return result


def calculate():
    # Use a breakpoint in the code line below to debug your script.
    content = [element for element in helper.splitFile("day4.txt", "\n\n")]
    numbers = [int(element) for element in content[0].split(",")]
    boardsList = [[inner.split(" ") for inner in element.split("\n")] for element in content[1:]]
    boards = [([[(int(number), False) for number in lsst if number != ''] for lsst in lst], False, idx) for idx, lst in enumerate(boardsList)]

    result1 = firstExercise(numbers, copy.deepcopy(boards))
    result2 = secondExercise(numbers, copy.deepcopy(boards))
    hej = ""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calculate()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
