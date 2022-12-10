# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
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


def redefineBasedOnMask(value, mask, conditionList):
    valueBinary = list(helper.baseToBinary(value, 10).zfill(len(mask)))
    for idx, character in enumerate(mask):
        valueBinary[idx] = character if character in conditionList else valueBinary[idx]
    return valueBinary

def firstExercise(splitted):
    dict = {}
    for element in splitted:
        mask = element[0]
        for mapping in element[1:]:
            key, value = [int(element) for element in mapping.split(" = ")]
            dict[key] = helper.baseToBase10("".join(redefineBasedOnMask(value, mask, ["0", "1"])))
    summing = sum(dict.values())
    return summing


def secondExercise(splitted):
    dict = {}
    for element in splitted:
        mask = element[0]
        for mapping in element[1:]:
            key, value = [int(element) for element in mapping.split(" = ")]
            keyBinary = redefineBasedOnMask(key, mask, ["1", "X"])
            for comb in helper.combinations(["0", "1"], keyBinary.count("X")):
                binaryCopy = "".join(keyBinary)
                for number in comb:
                    binaryCopy = binaryCopy.replace("X", number, 1)
                dict[binaryCopy] = value
    summing = sum(dict.values())
    return summing


def calculate():
    # Use a breakpoint in the code line below to debug your script.
    content = helper.splitFile("day14.txt", "\nmask = ")
    content[0] = content[0].replace("mask = ", "")
    content = [text.replace("mem[", "").replace("]", "") for text in content]
    splitted = [element.split("\n") for element in content]
    first = firstExercise(splitted)
    second = secondExercise(splitted)


    hj = ""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calculate()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
