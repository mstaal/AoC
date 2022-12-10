# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from utils import aoc_helper as helper


def parseLine(line):
    first, second = line.split(" -> ")
    x1, y1 = first.split(",")
    x2, y2 = second.split(",")
    return (int(x1), int(y1)), (int(x2), int(y2))



def counter(parsed, partTwo=False):
    count = 0
    pointsCount = {}
    for elm in parsed:
        if elm[0][0] == elm[1][0]:
            pointsCount[elm[0]] = pointsCount.get(elm[0], 0) + 1
            pointsCount[elm[1]] = pointsCount.get(elm[1], 0) + 1
            minimum = min(elm[0][1], elm[1][1])
            diff = abs(elm[0][1] - elm[1][1])
            for idx in range(1, diff):
                point = elm[0][0], minimum + idx
                pointsCount[point] = pointsCount.get(point, 0) + 1
        elif elm[0][1] == elm[1][1]:
            pointsCount[elm[0]] = pointsCount.get(elm[0], 0) + 1
            pointsCount[elm[1]] = pointsCount.get(elm[1], 0) + 1
            minimum = min(elm[0][0], elm[1][0])
            diff = abs(elm[0][0] - elm[1][0])
            for idx in range(1, diff):
                point = minimum + idx, elm[0][1]
                pointsCount[point] = pointsCount.get(point, 0) + 1
        elif abs(elm[1][0] - elm[0][0]) == abs(elm[1][1] - elm[0][1]) and partTwo:
            pointsCount[elm[0]] = pointsCount.get(elm[0], 0) + 1
            pointsCount[elm[1]] = pointsCount.get(elm[1], 0) + 1
            xu = min(elm[0][0], elm[1][0])
            yu = elm[0][1] if xu == elm[0][0] else elm[1][1]
            if yu == min(elm[0][1], elm[1][1]):
                x = xu + 1
                y = yu + 1
                while x < max(elm[0][0], elm[1][0]):
                    pointsCount[(x, y)] = pointsCount.get((x, y), 0) + 1
                    x += 1
                    y += 1
            else:
                x = xu + 1
                y = yu - 1
                while x < max(elm[0][0], elm[1][0]):
                    pointsCount[(x, y)] = pointsCount.get((x, y), 0) + 1
                    x += 1
                    y -= 1
    for key in pointsCount.keys():
        if pointsCount[key] > 1:
            count += 1
    return count


def exercise1(parsed):
    return counter(parsed)


def exercise2(parsed):
    return counter(parsed, True)


def calculate():
    # Use a breakpoint in the code line below to debug your script.
    content = [element for element in helper.splitFile("day5.txt", "\n")]
    parsed = [parseLine(element) for element in content]

    q1 = exercise1(parsed)
    q2 = exercise2(parsed)

    hej = ""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calculate()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
