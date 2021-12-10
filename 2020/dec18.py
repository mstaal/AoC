# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time
from collections import Counter

import pandas as pd
import AoCHelper as helper
from AoCHelper import Infix
import numpy as np
import sympy
import itertools
import re
import copy as cc
from functools import reduce
from itertools import permutations, combinations, chain, product

signLambda = lambda letter: 1 if letter == "R" else -1


# https://code.activestate.com/recipes/384122/
# http://tomerfiliba.com/blog/Infix-Operators/
mul = Infix(lambda x, y: x * y)
add = Infix(lambda x, y: x + y)



def calculate():
    # Use a breakpoint in the code line below to debug your script.
    content = helper.splitFile("day18.txt", "\n")
    firstExercise = sum([eval(element.replace("+", "|add|").replace("*", "|mul|")) for element in content])
    secondExercise = sum([eval(element.replace("*", "|mul|")) for element in content])

    hj = ""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calculate()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
