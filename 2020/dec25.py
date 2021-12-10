# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import queue
import time
from collections import Counter, deque

import pandas as pd
import AoCHelper as helper
import abcTypes as types
import numpy as np
import sympy
import itertools
import re
import copy as cc
from functools import reduce
from itertools import permutations, combinations, chain, product


def getLoopSize(subject, publickey):
    value = 1
    loopsize = 0
    while value != publickey:
        value = (value * subject) % 20201227
        loopsize +=1
    return loopsize


def transformSubject(subject, loopsize):
    value = 1
    count = 0
    while count < loopsize:
        value = (value * subject) % 20201227
        count +=1
    return value


def calculate():
    # Use a breakpoint in the code line below to debug your script.
    # Part 1
    content = [int(element) for element in helper.splitFile("day25.txt", "\n")]
    card = content[0]
    door = content[1]
    encryptionDoor = transformSubject(door, getLoopSize(7, card))
    encryptionCard = transformSubject(card, getLoopSize(7, door))


    # Part 2
    hfhhf = ""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calculate()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
