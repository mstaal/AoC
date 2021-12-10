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
from itertools import permutations, combinations, chain, product


def get_adjacent_indices(i, j, m, n):
    adjacent_indices = []
    if i > 0:
        adjacent_indices.append((i - 1, j))
    if i + 1 < m:
        adjacent_indices.append((i + 1, j))
    if j > 0:
        adjacent_indices.append((i, j - 1))
    if j + 1 < n:
        adjacent_indices.append((i, j + 1))
    if i > 0 and j > 0:
        adjacent_indices.append((i-1, j-1))
    if i + 1 < m and j > 0:
        adjacent_indices.append((i+1, j-1))
    if i > 0 and j + 1 < n:
        adjacent_indices.append((i-1, j+1))
    if i + 1 < m and j + 1 < n:
        adjacent_indices.append((i+1, j+1))
    return adjacent_indices


def adjacent(lst, i, j):
    indices = get_adjacent_indices(i, j, len(lst), len(lst[i]))
    elements = [lst[i][j] for i,j in indices]
    return elements

def get_indices_2(i, j, m, n):
    right = [(i, j + idx) for idx in range(1, n - j)]
    left = [(i, j - idx) for idx in range(1, j + 1)]
    down = [(i + idx, j) for idx in range(1, m - i)]
    up = [(i - idx, j) for idx in range(1, i + 1)]
    diagrightup = [(i - idx, j + idx) for idx in range(1, max(n, m)) if i - idx >= 0 and 0 <= j + idx < n]
    diagrightdown = [(i + idx, j + idx) for idx in range(1, max(n, m)) if i + idx < m and 0 <= j + idx < n]
    diagleftup = [(i - idx, j - idx) for idx in range(1, max(n, m)) if i - idx >= 0 and j - idx >= 0]
    diagleftdown = [(i + idx, j - idx) for idx in range(1, max(n, m)) if 0 <= i + idx < m and j - idx >= 0]
    adjacent_indices = [right, left, down, up, diagrightup, diagrightdown, diagleftup, diagleftdown]
    return adjacent_indices


def get_adjacent_2(lst, i, j):
    elements = []
    indices = get_indices_2(i, j, len(lst), len(lst[i]))
    for ll in indices:
        raw = [lst[i][j] for i, j in ll]
        stripped = [value for value in raw if value != "."]
        if(len(stripped) > 0):
            elements.append(stripped[0])
    return elements


def firstExercise(content, countRun = 0):
    copy = cc.deepcopy(content)
    for idx, val in enumerate(content):
        for jdx, vel in enumerate(val):
            element = content[idx][jdx]
            adjacentElements = adjacent(content, idx, jdx)
            count = adjacentElements.count("#")
            if element == "L" and not count > 0:
                copy[idx][jdx] = "#"
            elif element == "#" and count >= 4:
                copy[idx][jdx] = "L"
    one = str(content)
    two = str(copy)
    if one != two:
        return firstExercise(copy, countRun + 1)
    return copy, countRun

def secondExercise(content, amount, countRun = 0):
    copy = cc.deepcopy(content)
    for idx, val in enumerate(content):
        for jdx, vel in enumerate(val):
            element = content[idx][jdx]
            adjacentElements = get_adjacent_2(content, idx, jdx)
            count = adjacentElements.count("#")
            if element == "L" and not count > 0:
                copy[idx][jdx] = "#"
            elif element == "#" and count >= amount:
                copy[idx][jdx] = "L"
    one = str(content)
    two = str(copy)
    if one != two:
        return secondExercise(copy, countRun + 1)
    return copy, countRun

def joltCombinations(content):
    r = ""



def calculate():
    # Use a breakpoint in the code line below to debug your script.
    content = [list(element) for element in helper.splitFile("day11.txt", "\n")]

    firstResult = firstExercise(content)[0]
    flat_list = []
    text = str(firstResult)
    print(text)
    count = text.count("#")

    second = secondExercise(content, 5)
    count2 = str(second).count("#")
    hej = ""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calculate()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
