# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from collections import Counter

import pandas as pd
import AoCHelper as helper
import numpy as np
import sympy
from itertools import permutations


def decreases(number):
    text = str(number)
    for idx, val in enumerate(range(1, len(text))):
        numOne = int(text[idx])
        numTwo = int(text[val])
        if numTwo < numOne:
            return True
    return False


def adjacent(number):
    text = str(number)
    for idx, val in enumerate(range(1, len(text))):
        numOne = int(text[idx])
        numTwo = int(text[val])
        if numTwo == numOne:
            return True
    return False


def isValid(password):
    notDec = not decreases(password)
    adj = adjacent(password)
    return notDec and adj

def isValidStrict(password):
    myList = [int(element) for element in str(password)]
    mySet = set(myList)
    for number in mySet:
        if myList.count(number) == 2:
            return True
    return False

def calculate(right, down):
    # Use a breakpoint in the code line below to debug your script.
    input = list(range(right, down))
    answer = []
    count = 0
    for password in input:
        if isValid(password) and isValidStrict(password):
            print(password)
            count += 1
    hej = ""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(calculate(266666, 781584))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
