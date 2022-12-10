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
from itertools import permutations, combinations, chain, product


def calculate():
    # Use a breakpoint in the code line below to debug your script.
    content = [int(element) for element in helper.splitFile("day1.txt", "\n")]
    question1 = sum([int(content[i] < content[i+1]) for i in range(0, len(content)-1)])

    question2 = sum([int(content[i] + content[i+1] + content[i+2] < content[i+1] + content[i+2] + content[i+3]) for i in range(0, len(content)-3)])


    hej = ""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calculate()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
