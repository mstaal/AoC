# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time
from collections import Counter

import pandas as pd
from utils import AoCHelper as helper
import numpy as np
import sympy
import itertools
import re
import copy as cc
from functools import reduce
from itertools import permutations, combinations, chain, product

signLambda = lambda letter: 1 if letter == "R" else -1


def firstExercise(content, said):
    for idx, numb in enumerate(content):
        said.append(numb)
    count = len(said)
    while count < 2020:
        spoken = said[len(said)-1]
        indices = [i for i, x in enumerate(said) if x == spoken]
        if len(indices) == 1:
            said.append(0)
        else:
            said.append(indices[len(indices)-1] - indices[len(indices)-2])
        count += 1
    last = said[len(said)-1]
    return last




def secondExercise(content, upper):
    said = {}
    for idx, numb in enumerate(content):
        said[numb] = [idx + 1]
    spoken = content[-1]
    start = time.process_time()
    for count in range(len(said), upper):
        seek = said.get(spoken, [])
        nextSpoken = 0 if len(seek) in [0, 1] else seek[1] - seek[0]
        lst = said.get(nextSpoken, [])
        said[nextSpoken] = [lst[-1], count + 1] if len(lst) > 0 else [count + 1]
        spoken = nextSpoken
    print(time.process_time() - start)
    return spoken


def calculate():
    # Use a breakpoint in the code line below to debug your script.
    content = [int(element) for element in helper.splitFile("day15.txt", ",")]

    # firstExercise(content, [])
    secondExercise(content, 2020)

    hj = ""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calculate()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
