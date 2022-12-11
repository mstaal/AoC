# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from collections import Counter

import pandas as pd
from utils import aoc_helper as helper
import numpy as np
import sympy
import re
from itertools import permutations


def calculateFirst(content, sum=0, index=0, executed=[]):
    terminated = False
    for idx in range(index, len(content)):
        ins, number = content[idx].split()
        if idx in executed:
            terminated = True
            break
        if ins == "acc":
            sum += int(number)
            executed.append(idx)
        if ins == "jmp":
            return calculateFirst(content, sum, int(idx) + int(number), executed)
    return (sum, terminated)


def calculateSecond2nd(content, sum, index, changeIdx):
    element = content[changeIdx]
    if "nop" in element:
        content[changeIdx] = element.replace("nop", "jmp")
    elif "jmp" in element:
        content[changeIdx] = element.replace("jmp", "nop")
    return calculateFirst(content, sum, index, [])


def calculate():
    # Use a breakpoint in the code line below to debug your script.
    content = helper.split_file("day8.txt", "\n")
    resOne = calculateFirst(content)
    resultsTwo = [calculateSecond2nd(content.copy(), 0, 0, element) for element in list(range(0, 643))]
    resultsTwoFilter = [element for element in resultsTwo if not element[1]][0][0]
    hej = ""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(calculate())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
