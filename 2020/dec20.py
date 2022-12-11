# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time
from collections import Counter

import pandas as pd
from utils import aoc_helper as helper
import numpy as np
import sympy
import itertools
import re
import copy as cc
from functools import reduce
from itertools import permutations, combinations, chain, product


def getMeta(tile, key):
    result = {}
    result["top"] = tile[0]
    result["bottom"] = tile[-1]
    result["left"] = "".join([element[0] for element in tile])
    result["right"] = "".join([element[-1] for element in tile])
    result["tile"] = np.array([list(element) for element in tile])
    result["orientation"] = 0
    result["flipped"] = False
    result["key"] = key
    return result


def rotateMeta(meta):
    rotated = {}
    rotated["top"] = meta["left"]
    rotated["right"] = meta["top"]
    rotated["bottom"] = meta["right"]
    rotated["left"] = meta["bottom"]
    rotated["tile"] = np.rot90(meta["tile"], k=3)
    rotated["orientation"] = (meta["orientation"] + 1) % 4
    rotated["flipped"] = meta["flipped"]
    rotated["key"] = meta["key"]
    return rotated


def flipMeta(meta):
    flipped = {}
    flipped["top"] = meta["top"][::-1]
    flipped["right"] = meta["left"]
    flipped["left"] = meta["right"]
    flipped["bottom"] = meta["bottom"][::-1]
    flipped["tile"] = np.fliplr(meta["tile"])
    flipped["orientation"] = meta["orientation"]
    flipped["flipped"] = not meta["flipped"]
    flipped["key"] = meta["key"]
    return flipped


def getAllVersions(meta):
    lst = [meta]
    lst.append(rotateMeta(lst[-1]))
    lst.append(rotateMeta(lst[-1]))
    lst.append(rotateMeta(lst[-1]))
    lst.append(flipMeta(lst[0]))
    lst.append(flipMeta(lst[1]))
    lst.append(flipMeta(lst[2]))
    lst.append(flipMeta(lst[3]))
    return lst


def getMatchingPair(meta, possibilities):
    lst = getAllVersions(meta)
    for poss in possibilities:
        lst2 = getAllVersions(poss)
        for item in lst:
            for next in lst2:
                if item["right"] == next["left"]:
                    return item, next
    return None

def getCornerCounts(tilesMeta):
    counts = {}
    for key, meta in tilesMeta.items():
        lst = getAllVersions(meta)
        for extrakey, extravalue in {k: v for k, v in tilesMeta.items() if k != key}.items():
            lst2 = getAllVersions(extravalue)
            count = counts.get(key, 0)
            for item in lst:
                for next in lst2:
                    if item["bottom"] == next["top"] or item["right"] == next["left"]:
                        counts[key] = count + 1
    return counts


def firstExercise(tilesMeta):
    counts = getCornerCounts(tilesMeta)
    countsFiltered = {key: value for key, value in counts.items() if value == 2}
    prod = reduce(lambda a, b: a * b, countsFiltered.keys())
    return prod


def secondExercise(tilesMeta, square):
    counts = getCornerCounts(tilesMeta)
    corners = {key: tilesMeta[key] for key, value in counts.items() if value == 2}
    border = {key: tilesMeta[key] for key, value in counts.items() if value == 3}
    inner = {key: tilesMeta[key] for key, value in counts.items() if value == 4}
    for corner in corners:
        borderPiece = [tilesMeta[corner]]
        cornerMeta = borderPiece[0]
        while len(borderPiece) < 11:
            for piece in border:
                orientation = 0
                meta = piece
                flipped = flipMeta(meta)
                count = 0
        hhf = ""
    available = list(tilesMeta.keys())
    result = [[tilesMeta[available[0]]]]
    available.remove(available[0])
    for idx in range(0, square):
        lst = result[idx]
        while len(lst) < 12:
            for key in available:
                meta = tilesMeta[key]
                flipped = flipMeta(meta)
                count = 0
                while count < 4:
                    last = lst[-1]
                    if last["right"] == meta["left"]:
                        lst.append(meta)
                        available.remove(meta["key"])
                        count = 4
                    elif last["right"] == flipped["left"]:
                        lst.append(flipped)
                        available.remove(flipped["key"])
                        count = 4
                    else:
                        print(meta["key"])
                        meta = rotateMeta(meta)
                        flipped = flipMeta(meta)
                        count += 1
            jjfjf = ""

def calculate():
    # Use a breakpoint in the code line below to debug your script.
    content = helper.split_file("day20.txt", "\n\n")
    tiles = {int(element[0].replace("Tile ", "").replace(":", "")): element[1:] for element in [element.split("\n") for element in content]}
    tilesMeta = {key: getMeta(value, key) for key, value in tiles.items()}
    square = int(np.sqrt(len(tiles)))

    res1 = firstExercise(tilesMeta)
    secondExercise(tilesMeta, square)
    hj = ""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calculate()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
