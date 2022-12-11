# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from collections import Counter

import pandas as pd
from utils import aoc_helper as helper
import numpy as np
import sympy
from itertools import permutations


def orbit(arg, dict, set, count):
    image = dict[arg]
    print("HdH")
    for element in image:
        if element in set:
            return orbit(element, dict, set, count)
    return count

def calculate():
    # Use a breakpoint in the code line below to debug your script.
    input = helper.split_file("test.txt", "\n")
    count = 0
    set = [element[0:3] for element in input]
    dict = {}
    for element in set:
        matches = [s[4:] for s in input if element + ")" in s]
        dict[element] = matches
    for element in set:
        count = orbit(element, dict, set, count)

    count = 0

    hej = ""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(calculate())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
