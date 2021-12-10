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

def getNext(current, game):
    return current.next if current.next is not None else game["content"].head


def playRoundInGame(game, maxCandidates):
    current = game["current"]
    first = getNext(current, game)
    second = getNext(first, game)
    third = getNext(second, game)
    threeSet = {element.data for element in [first, second, third]}
    current.next = getNext(third, game)
    maxi = max(maxCandidates.difference(threeSet))
    candidates = set([current.data - idx for idx in range(1, 5) if current.data - idx > 0]).difference(threeSet)
    destinationData = max(candidates) if len(candidates) > 0 else maxi
    destination = game["content"][destinationData]
    third.next = destination.next
    destination.next = first
    game["current"] = getNext(current, game)



def secondExercise(game, length):
    count = 0
    maxi = max(game["content"].map.values())
    maxCandidates = set([maxi.data - idx for idx in range(0, 4)])
    while count < length:
        playRoundInGame(game, maxCandidates)
        count += 1


def calculate():
    # Use a breakpoint in the code line below to debug your script.
    content = [int(element) for element in list("739862541")]
    game = {}
    game["content"] = types.LinkedList(content)
    game["current"] = game["content"].head
    secondExercise(game, 100)
    print("Part 1: " + str(list(game["content"])))

    # Part 2
    t = time.process_time()
    lst = [element for element in content] + [idx for idx in range(len(content) + 1, 1000001)]
    game2 = {}
    game2["content"] = types.LinkedList(lst)
    game2["current"] = game2["content"].head
    secondExercise(game2, 10000000)
    one = game2["content"][1]
    print("Part 2: " + str(one.next.data * one.next.next.data))
    elapsed_time = time.process_time() - t
    print(str(elapsed_time))
    hhd = ""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calculate()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
