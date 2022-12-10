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


def generateDicts(data):
    foodDict = {}
    allergensDict = {}
    for element in data:
        for key in element[1]:
            food = foodDict.get(key, [])
            food.append(element[0])
            foodDict[key] = food
        for key in element[0]:
            allergen = allergensDict.get(key, set())
            for food in element[1]:
                allergen.add(food)
            allergensDict[key] = allergen
    return foodDict, allergensDict


def getImpossible(foodDict, allergensDict):
    impossible = set()
    for allergen, foods in allergensDict.items():
        length = len(foods)
        count = 0
        for food in foods:
            allerAlt = foodDict[food]
            if not all((allergen in element) for element in allerAlt):
                count += 1
        if count == length:
            impossible.add(allergen)
    return impossible


def getOccurences(data):
    return [item for sublist in [element[0] for element in data] for item in sublist]


def cleanedDict(foodDict, impossible):
    foodDictCopy = cc.deepcopy(foodDict)
    for element in impossible:
        for key, value in foodDictCopy.items():
            for lst in value:
                if element in lst:
                    lst.remove_inner(element)
    for key, value in foodDictCopy.items():
        inter = set(value[0])
        for lst in value:
            inter = inter.intersection(lst)
        foodDictCopy[key] = list(inter)
    return foodDictCopy


def finalMapping(foodDictCleaned):
    copyDict = cc.deepcopy(foodDictCleaned)
    length = len(copyDict)
    mapping = {}
    while len(mapping) < length:
        search = {key: value for key, value in copyDict.items() if len(value) == 1}
        for key, value in search.items():
            mapping[key] = value[0]
            del copyDict[key]
            for altkey, altvalue in copyDict.items():
                if value[0] in altvalue:
                    altvalue.remove_inner(value[0])
    return mapping

def generateCommaText(mapping):
    lst = list(mapping.keys())
    lst.sort()
    text = ""
    for element in lst:
        text += mapping[element] + ","
    return text


def calculate():
    # Use a breakpoint in the code line below to debug your script.
    content = helper.splitFile("day21.txt", "\n")
    data = [(ingredients.split(" "), allergens.replace("contains ", "").replace(")", "").split(", ")) for
            ingredients, allergens in [element.split(" (") for element in content]]
    foodDict, allergensDict = generateDicts(data)

    # Part 1
    impossible = getImpossible(foodDict, allergensDict)
    occurences = getOccurences(data)
    summing = len([element for element in occurences if element in impossible])

    # Part 2
    foodDictNew = cleanedDict(foodDict, impossible)
    mapping = finalMapping(foodDictNew)
    text = generateCommaText(mapping)
    hfhf = ""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calculate()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
