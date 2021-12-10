# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
import numpy as np
import sympy
from itertools import permutations


def csvToStringList(filename, sep):
    return list(map(lambda x: str(x[0]), pd.read_csv(filename, sep).values))


def csvToIntList(filename, sep):
    return list(map(lambda x: int(x[0]), pd.read_csv(filename, sep).values))


def csvToList(filename, sep):
    return list(map(lambda x: x[0], pd.read_csv(filename, sep).values))


def print_prompt():
    # Use a breakpoint in the code line below to debug your script.
    numbers = csvToList("day1.txt", "\n")

    setlist = set(permutations(numbers, 3))

    for element in setlist:
        if element[0] + element[1] + element[2] == 2020:
            print(element)
            break


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_prompt()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
