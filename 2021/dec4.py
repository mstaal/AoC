# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from utils import AoCHelper as helper
import numpy as np
import copy


def firstExercise(numbers, content):
    final = None
    finalNumber = None
    finalIndex = -1
    for num in numbers:
        for elm in content:
            current = elm[0]
            for idx in range(0, len(current)):
                for idy in range(0, len(current)):
                    candidate = current[idx][idy]
                    if candidate[0] == num:
                        current[idx][idy] = (current[idx][idy][0], True)
            array = np.array(current)
            rotated = np.rot90(array)
            for rot in array:
                count = len([el for el in rot if el[1]])
                if count >= 5:
                    final = array
                    finalNumber = num
                    finalIndex = elm[2]
                    break
            for rot in rotated:
                count = len([el for el in rot if el[1]])
                if count >= 5:
                    final = array
                    finalNumber = num
                    finalIndex = elm[2]
                    break
            if final is not None:
                break
        if final is not None:
            break
    summing = sum([element[0] for element in helper.flatten(final.tolist()) if not element[1]])
    result = summing * finalNumber
    return (result, finalIndex)


def secondExercise(numbers, content):
    cp = copy.deepcopy(content)
    result = firstExercise(numbers, cp)
    filter = [element for element in cp if element[2] != result[1]]
    if len(filter) > 0:
        return secondExercise(numbers, filter)
    else:
        return result


def calculate():
    # Use a breakpoint in the code line below to debug your script.
    content = [element for element in helper.splitFile("day4.txt", "\n\n")]
    numbers = [int(element) for element in content[0].split(",")]
    boardsList = [[inner.split(" ") for inner in element.split("\n")] for element in content[1:]]
    boards = [([[(int(number), False) for number in lsst if number != ''] for lsst in lst], False, idx) for idx, lst in enumerate(boardsList)]

    result1 = firstExercise(numbers, copy.deepcopy(boards))
    result2 = secondExercise(numbers, copy.deepcopy(boards))
    hej = ""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calculate()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
