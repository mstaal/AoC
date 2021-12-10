# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from collections import Counter

import pandas as pd
import AoCHelper as helper
import numpy as np
import sympy
import itertools
import re
import copy as cc
from functools import reduce
from itertools import permutations, combinations, chain, product

# Chinese remainder theorem

signLambda = lambda letter: 1 if letter == "R" else -1

def firstExercise(timestamp, secondLine):
    result = []
    resultSecond = []
    lst = [int(number) for number in secondLine.replace("x,", "").split(",")]
    for element in lst:
        sample = [i * element for i in range(0, timestamp)]
        filter = min([i for i in sample if i >= timestamp])
        result.append((filter, element))
        resultSecond.append(filter)
    mini = min(resultSecond)
    res = (mini - timestamp) * 827
    return res


def secondCalc(secondLine):
    timesMap = {}
    timeTuples = []
    times = []
    lst = [number for number in secondLine.split(",")]
    for idx, element in enumerate(lst):
        if element != "x":
            timeTuples.append((int(element), idx))
            timesMap[int(element)] = idx
            times.append(int(element))
    return timesMap, timeTuples, min(times), max(times)


def secondExercise(timeTuples):
    text = ""
    for element in timeTuples:
        text += "(n + " + str(element[1]) + ") mod " + str(element[0]) + " = 0, "
    text = text[:-2]
    return text

def calculate():
    # Use a breakpoint in the code line below to debug your script.
    timestamp, secondLine = helper.splitFile("day13.txt", "\n")
    firstExercise(int(timestamp), secondLine)

    calcs = secondCalc(secondLine)
    chinese = secondExercise(calcs[1])

    n = [i[0] for i in calcs[1]]
    a = [-1*i[1] for i in calcs[1]]
    cr = helper.chinese_remainder(n, a)
    hj = ""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calculate()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
