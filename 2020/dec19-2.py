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


def getRule42(rules):
    return generateRegex(rules, 42)


def getRule31(rules):
    return generateRegex(rules, 31)


def getCustomRule8(rules):
    return "(" + getRule42(rules) + ")+"


def getCustomRule11(rules, repeat):
    lst = [f"(({getRule42(rules)}){{{str(number)}}}({getRule31(rules)}){{{str(number)}}})|" for number in range(1, repeat)]
    text = "(" + "".join(lst)[:-1] + ")"
    return text


def generateRegex(rules, index):
    regex = ""
    rule = rules[index]
    if len(rule) == 1:
        child = rule[0]
        for element in child:
            if element.isalpha():
                regex = regex + element
            else:
                regex = regex + "(" + generateRegex(rules, int(element)) + ")"
    elif len(rule) == 2:
        for idx, val in enumerate(rule):
            for element in val:
                regex = regex + "(" + generateRegex(rules, int(element)) + ")"
            regex = regex + ("|" if idx == 0 else "")
    return regex


def generateCustomRegex(rules, repeat):
    return getCustomRule8(rules) + getCustomRule11(rules, repeat)


def calculate():
    content = helper.splitFile("day19.txt", "\n\n")
    rules = {int(element[0]): element[1].replace("\"", "") for element in
             [element.split(": ") for element in content[0].split("\n")]}
    rules = {key: [element.split(" ") for element in value.split(" | ")] for key, value in rules.items()}
    messages = [element for element in content[1].split("\n")]

    # Part 1
    regex = f"^{generateRegex(rules, 0)}$"
    matches = [(element, re.search(regex, element)) for element in messages if re.search(regex, element) is not None]

    # Part 2: 330-388 (332)
    regex2 = f"^{generateCustomRegex(rules, 10)}$"
    matches2 = [(element, re.search(regex2, element)) for element in messages if re.search(regex2, element) is not None]
    hj = ""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calculate()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
