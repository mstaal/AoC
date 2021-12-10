# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time
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

def generateRulesMap(rules, rule):
    lambdaMap = lambda x: {int(element): rules[int(element)] for element in x if any(char.isdigit() for char in element)}
    zeroSplit = [element.split(" ") for element in rule.split(" | ")]
    mappings = list(map(lambdaMap, zeroSplit))[0]
    while any(any(char.isdigit() for char in element) for element in mappings.values()):
        maps = {key: value for key, value in mappings.items() if any(char.isdigit() for char in str(value))}
        for key, value in maps.items():
            extra = list(map(lambdaMap, list(set(re.findall("\d+", value)))))[0]
            replacement = value
            for extrakey, extravalue in extra.items():
                replacement = replacement.replace(str(extrakey), "".join(["(",extravalue, ")"]))
                mappings[key] = replacement
    return mappings


def generateRulesList(rules, rule):
    zeroSplit = [element.split(" ") for element in rule.split(" | ")]
    mappings = list(map(lambda x: [rules[int(element)] for element in x], zeroSplit))
    for idx, choice in enumerate(mappings):
        for idy, element in enumerate(choice):
            if not element.isalpha():
                mapping = generateRulesList(rules, element)
                mappings[idx][idy] = mapping
    return mappings


def firstExercise(rulesList, messages):
    correct = []
    for message in messages:
        for idx, value in enumerate(message):
            dfdf = ""


def generateRegex(rulesList):
    text = ""
    for idx, rule in enumerate(rulesList):
        check = isinstance(rule, list)
        if check:
            rulepiece = generateRegex(rule)
            text = text + "(" + rulepiece + ")" + ("|" if idx == 0 else "")
        if isinstance(rule, str):
            text = text + "".join(rule)
    return text


def calculate():
    # Use a breakpoint in the code line below to debug your script.
    content = helper.splitFile("day19.txt", "\n\n")
    rules = {int(element[0]): element[1].replace("\"", "") for element in [element.split(": ") for element in content[0].split("\n")]}
    messages = content[1].split("\n")

    rulesList = generateRulesList(rules, rules[0])
    hfhf = generateRegex(rulesList)
    #rulesMap = generateRulesMap(rules, rules[0])
    firstExercise(rulesList, messages)

    hj = ""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calculate()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
