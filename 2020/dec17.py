# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time
from collections import Counter

import pandas as pd
from utils import aoc_helper as helper
import numpy as np
import sympy
import itertools
import re
import copy as cc
from functools import reduce
from itertools import permutations, combinations, chain, product

signLambda = lambda letter: 1 if letter == "R" else -1


def adjac(ele, sub = []):
  if not ele:
     yield sub
  else:
     yield from [idx for j in range(ele[0] - 1, ele[0] + 2)
                for idx in adjac(ele[1:], sub + [j])]



def iterateOne(dict, coordinates):
    trueNext = {}
    for coor in coordinates:
        adjacent = set([tuple(element) for element in list(adjac(coor))])
        adjacent.remove(coor)
        adjacentTrue = adjacent.intersection(dict)
        if (dict.get(coor, False) and len(adjacentTrue) in [2, 3]) or (not dict.get(coor, False) and len(adjacentTrue) == 3):
            trueNext[coor] = True
    return trueNext


def firstExercise(dict, coordinates, count):
    for i in range(0, count):
        dict = iterateOne(dict, coordinates)
    hj = ""

def calculate():
    # Use a breakpoint in the code line below to debug your script.
    content = helper.splitFile("day17.txt", "\n")
    origin = (0, 0, 0, 0)
    interval = (-11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
    coordinates = set(itertools.product(interval, repeat=len(origin)))
    initial_dict = {(i-1, 1-j, 0, 0): True for i, j in itertools.product(range(len(content[0])), range(len(content))) if content[j][i] == '#'}
    firstExercise(initial_dict, coordinates, 6)

    hej = list(adjac((1, 0, 0)))

    hj = ""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calculate()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
