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
from itertools import permutations, combinations, chain, product


def joltDifferences(content, dict, index):
    possibleChoices = [index + i for i in range(0, 4)]
    choice = -1
    for element in possibleChoices:
        if element in content and element not in dict.keys():
            choice = element
            break
    if choice == -1:
        dict[index+3] = 3
        return dict
    dict[choice] = choice - index
    return joltDifferences(content, dict, choice)

def joltCombinations(content):
    copied = content.copy()
    copied.sort()
    dictCount = {0: 1}
    for element in copied:
        interval = [element - i for i in range(1, 4)]
        dictCount[element] = max(1, sum(dictCount.get(entity, 0) for entity in interval))
    return dictCount[max(dictCount.keys())]



def calculate():
    # Use a breakpoint in the code line below to debug your script.
    content = [int(element) for element in helper.splitFile("day10.txt", "\n")]
    content.sort()

    resultOne = joltDifferences(content, {}, 0)
    sumOne = len([element for element in resultOne.values() if element == 1])
    sumThree = len([element for element in resultOne.values() if element == 3])


    resultTwo = joltCombinations(content)
    hej = ""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calculate()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
