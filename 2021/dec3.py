# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from utils import aoc_helper as helper
import numpy as np


def firstExercise(content):
    array = np.array(content)
    rotated = np.rot90(np.rot90(np.rot90(array))).tolist()
    gammaCounts = [1 if sum([int(element) for element in lst]) > (len(rotated[0]) / 2) else 0 for lst in rotated]
    gammaConcatated = ''.join([str(element) for element in gammaCounts])
    epsilonCounts = [1 if sum([int(element) for element in lst]) < (len(rotated[0]) / 2) else 0 for lst in rotated]
    epsilonConcatated = ''.join([str(element) for element in epsilonCounts])

    gamma = int(gammaConcatated, 2)
    epsilon = int(epsilonConcatated, 2)
    return gamma * epsilon


def mostCommonOxygen(lst):
    numbers = [elem[0] for elem in lst]
    return 1 if numbers.count(1) >= numbers.count(0) else 0

def leastCommonCo2(lst):
    numbers = [elem[0] for elem in lst]
    return 0 if numbers.count(1) >= numbers.count(0) else 1

def calculateNumber(content, function):
    array = np.array(content)
    rotated = [[(int(element), (len(content) - 1) - idx) for idx, element in enumerate(lst)] for lst in np.rot90(np.rot90(np.rot90(array))).tolist()]
    indices = []
    for idx in range(0, len(rotated)):
        lst = [element for element in rotated[idx] if function(rotated[idx]) == element[0]]
        indices = [idx[1] for idx in lst]
        if len(indices) <= 1:
            break
        rotated = [[element for element in piece if element[1] in indices] for piece in rotated]
    base2 = ''.join(content[indices[0]])
    result = int(base2, 2)
    return result

def secondExercise(content):
    co2Number = calculateNumber(content.copy(), leastCommonCo2)
    oxygenNumber = calculateNumber(content.copy(), mostCommonOxygen)
    result = co2Number * oxygenNumber
    return result



def calculate():
    # Use a breakpoint in the code line below to debug your script.
    content = [list(element) for element in helper.splitFile("day3.txt", "\n")]

    firstExercise(content)
    secondExercise(content)
    hej = ""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calculate()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
