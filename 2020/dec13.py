from utils import aoc_helper as helper

# Chinese remainder theorem

signLambda = lambda letter: 1 if letter == "R" else -1

def firstExercise(timestamp, secondLine):
    result = []
    resultSecond = []
    lst = [int(number) for number in secondLine.replace("x,", "").split(",")]
    for element in lst:
        sample = [i * element for i in range(0, timestamp)]
        filter_res = min([i for i in sample if i >= timestamp])
        result.append((filter_res, element))
        resultSecond.append(filter_res)
    mini = min(resultSecond)
    _, id = list(filter(lambda x: x[0] == mini, result))[0]
    res = (mini - timestamp) * id
    return res


def secondCalc(secondLine):
    timesMap = {}
    timeTuples = []
    times = []
    lst = [number for number in secondLine.split(",")]
    for idx, element in enumerate(lst):
        if element != "x":
            timeTuples.append((int(element), idx))
            timesMap[int(element)] = idx
            times.append(int(element))
    return timesMap, timeTuples, min(times), max(times)


def secondExercise(timeTuples):
    text = ""
    for element in timeTuples:
        text += "(n + " + str(element[1]) + ") mod " + str(element[0]) + " = 0, "
    text = text[:-2]
    return text

def calculate():
    # Use a breakpoint in the code line below to debug your script.
    timestamp, secondLine = helper.splitFile("day13.txt", "\n")
    print(f"Result 1: {firstExercise(int(timestamp), secondLine)}")

    calcs = secondCalc(secondLine)
    print(f"Result 2 (Wolfram): {secondExercise(calcs[1])}")

    n = [i[0] for i in calcs[1]]
    a = [-1*i[1] for i in calcs[1]]
    print(f"{helper.chinese_remainder(n, a)}")


if __name__ == '__main__':
    calculate()
