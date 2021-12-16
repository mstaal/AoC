# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from collections import Counter

import pandas as pd
from utils import AoCHelper as helper
import numpy as np
import sympy
from itertools import permutations

def fewestZeros(counters):
    zeroCounters = [element['0'] for element in counters]
    minNum = min(zeroCounters)
    for idx, val in enumerate(zeroCounters):
        if val == minNum:
            return idx


def getMultiple(slicing):
    counters = [Counter(element) for element in slicing]
    fewestZerosIdx = fewestZeros(counters)
    oneCounter = counters[fewestZerosIdx]
    mult = int(oneCounter['1']) * int(oneCounter['2'])
    return mult


def putLayersTogether(slices):
    layer = list(slices[0])
    for slice in slices:
        for idx in range(0, len(slice)):
            if layer[idx] == '2':
                char = slice[idx]
                layer[idx] = char
                hj = ""
    result = ''.join(layer)
    return result


def calculate():
    # Use a breakpoint in the code line below to debug your script.
    input = helper.splitFile("test.txt", "\n")[0]
    pixelCount = 25*6
    slicing = [input[i: i + pixelCount] for i in range(0, len(input), pixelCount)]
    mult = getMultiple(slicing)

    oneLayer = putLayersTogether(slicing)


    hej = ""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(calculate())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
