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


def countYes(group):
    withoutBreak = group.replace("\n", "")
    charList = list(withoutBreak)
    charSet = set(charList)
    count = len(charSet)
    return count

def countYesStrict(group):
    lists, hhg = group.split("\n")
    sets = [set(element) for element in lists]
    inters = sets[0]
    for oneSet in sets:
        inters = inters.intersection(oneSet)
    return len(inters)

def calculate():
    # Use a breakpoint in the code line below to debug your script.
    content = helper.splitFile("day6.txt", "\n\n")

    count = 0
    for element in content:
        count += countYesStrict(element)



    hej = ""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(calculate())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
