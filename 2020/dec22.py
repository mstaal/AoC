# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import queue
import time
from collections import Counter, deque

import pandas as pd
from utils import aoc_helper as helper
import numpy as np
import sympy
import itertools
import re
import copy as cc
from functools import reduce
from itertools import permutations, combinations, chain, product


def playRoundInGameOne(game):
    player1 = game["Player 1:"]
    first1 = player1[0]
    player1.remove_inner(first1)
    player2 = game["Player 2:"]
    first2 = player2[0]
    player2.remove_inner(first2)
    if first1 > first2:
        player1.append(first1)
        player1.append(first2)
    elif first2 > first1:
        player2.append(first2)
        player2.append(first1)


def firstExercise(game):
    length = len(game["Player 1:"])
    while min([len(element) for element in game.values()]) > 0:
        playRoundInGameOne(game)
    winningCards = [element for element in game.values() if len(element) > 0][0]
    winningCards.reverse()
    count = 0
    for idx, element in enumerate(range(1, length + 1)):
        count += element * winningCards[idx]
    return count


def playRoundInGameTwo(game):
    result = ""
    player1 = game["Player 1:"]
    first1 = player1[0]
    player1.remove_inner(first1)
    remaining1 = len(player1)
    player2 = game["Player 2:"]
    first2 = player2[0]
    player2.remove_inner(first2)
    remaining2 = len(player2)
    if first1 <= remaining1 and first2 <= remaining2:
        gameRecursion = {}
        gameRecursion["Player 1:"] = player1[:first1]
        gameRecursion["Player 2:"] = player2[:first2]
        result = executeGameTwo(gameRecursion)[0]
        if result == "Player 1:":
            player1.append(first1)
            player1.append(first2)
        if result == "Player 2:":
            player2.append(first2)
            player2.append(first1)
    elif first1 > first2:
        player1.append(first1)
        player1.append(first2)
    elif first2 > first1 or result:
        player2.append(first2)
        player2.append(first1)


def executeGameTwo(game):
    history = ([], [])
    while min([len(element) for element in game.values()]) > 0:
        duplicateCheck = (len(history[0]) != len(set(history[0]))) or (len(history[1]) != len(set(history[1])))
        if duplicateCheck:
            return "Player 1:", game["Player 1:"]
        playRoundInGameTwo(game)
        history[0].append("".join([str(e) for e in game["Player 1:"]]))
        history[1].append("".join([str(e) for e in game["Player 2:"]]))
    winningCards = [key for key, value in game.items() if len(value) > 0][0]
    return winningCards, game[winningCards]


def secondExercise(game):
    winningCards = executeGameTwo(cc.deepcopy(game))
    lst = winningCards[1]
    length = len(winningCards)
    lst.reverse()
    count = 0
    for idx, element in enumerate(range(1, length + 1)):
        count += element * lst[idx]
    return count

def calculate():
    # Use a breakpoint in the code line below to debug your script.
    content = helper.splitFile("day22.txt", "\n\n")
    game = {element[0]: list(map(lambda x: int(x), element[1:])) for element in [element.split("\n") for element in content]}
    res1 = firstExercise(cc.deepcopy(game))
    res2 = secondExercise(cc.deepcopy(game))
    hhd = ""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calculate()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
