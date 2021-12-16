# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from collections import Counter

import pandas as pd
from utils import AoCHelper as helper
import numpy as np
import sympy
import re
from itertools import permutations


def generateDict(content):
    dict = {}
    for element in content:
        split = element.split(" ")
        name = split[0] + ' ' + split[1]
        end = ''
        for el in split[2:]:
            end += ' ' + el
        endPieces = end.split(",")
        result = []
        for piece in endPieces:
            result.append(piece.replace("bags contain ", "").replace(" bags", "").replace(".", "").replace(" bag", "").strip())
        dict[name] = result
    return dict

def keyLookup(dict, search):
    result = []
    for key, values in dict.items():
        for value in values:
            if search in value:
                result.append(key)
    return result


def generateRelevant(dict, relevant):
    count = len(relevant)
    for element in relevant:
        newList = keyLookup(dict, element)
        for word in newList:
            relevant.append(word)
        relevant = list(set(relevant))
    if count == len(relevant):
        return relevant
    else:
        return generateRelevant(dict, relevant)


def dictCount(dict, search, count):
    result = dict[search]
    for value in result:
        if value != "no other":
            number = int(value.split(' ')[0])
            newWord = value.replace(str(number) + " ", "")
            count = count + number * dictCount(dict, newWord, 1)
    return count


def calculate():
    # Use a breakpoint in the code line below to debug your script.
    content = helper.splitFile("day7.txt", "\n")

    dict = generateDict(content)
    relevant = generateRelevant(dict, keyLookup(dict, "shiny gold"))

    dictCoun = dictCount(dict, "shiny gold", 0)



    hej = ""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(calculate())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
