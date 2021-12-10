# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from collections import Counter

import pandas as pd
import AoCHelper as helper
import numpy as np
import sympy
import re
from itertools import permutations


def calculateFirst(content, sum=0, index=0, executed=[]):
    for idx in range(index, len(content)):
        element = content[idx]
        ins, number = element.split()
        if idx in executed:
            break
        if ins == "acc":
            sum += int(number)
            executed.append(idx)
        if ins == "jmp":
            return calculateFirst(content, sum, int(idx) + int(number), executed)
    return sum


def calculateSecond(content, sum, index, executed):
    for idx in range(index, len(content)):
        element = content[idx]
        ins, number = element.split()
        if ins == "acc":
            sum += int(number)
        if (ins == "jmp" and idx != executed) or (ins == "nop" and idx == executed):
            return calculateSecond(content, sum, int(idx) + int(number), executed)
    return sum


def calculate():
    # Use a breakpoint in the code line below to debug your script.
    content = helper.splitFile("day8.txt", "\n")
    resOne = calculateFirst(content)
    listRange = list(range(0, 643))
    for index in listRange:
        try:
            resTwo = calculateSecond(content, 0, 0, index)
            print(resTwo)
            break
        except RecursionError as re:
            pass
    hej = ""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(calculate())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
