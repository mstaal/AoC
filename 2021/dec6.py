# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from utils import aoc_helper as helper


def calculateEx1(content, days):
    cp = content.copy()
    for day in range(0, days):
        length = len(cp)
        for idx in range(0, length):
            element = cp[idx]
            if element > 0:
                cp[idx] -= 1
            elif element == 0:
                cp[idx] = 6
                cp.append(8)
    final = len(cp)
    return final


def calculateEx2(content, days):
    dictionary = {}
    for element in content:
        dictionary[element] = dictionary.get(element, 0) + 1
    for day in range(0, days):
        zero = dictionary.get(0, 0)
        one = dictionary.get(1, 0)
        two = dictionary.get(2, 0)
        three = dictionary.get(3, 0)
        four = dictionary.get(4, 0)
        five = dictionary.get(5, 0)
        six = dictionary.get(6, 0)
        seven = dictionary.get(7, 0)
        eight = dictionary.get(8, 0)

        dictionary[0] = one
        dictionary[1] = two
        dictionary[2] = three
        dictionary[3] = four
        dictionary[4] = five
        dictionary[5] = six
        dictionary[6] = zero + seven
        dictionary[7] = eight
        dictionary[8] = zero
    final = sum([val for val in dictionary.values()])
    return final


def countOp(number, days):
    new_days = max(0, days - number)
    if days == 0:
        return 1
    elif number == 0 and days > 0:
        return countOp(0, new_days - 7) + countOp(0, new_days - 9)
    else:
        return countOp(0, new_days)


def calculate():
    # Use a breakpoint in the code line below to debug your script.
    content = [int(element) for element in helper.split_file("day6.txt", ",")]

    print("Start 1:")
    #result = sum([countOp(element, 80) for element in content])
    result = calculateEx2(content, 80)
    print("Result: " + str(result))

    print("Start 2:")
    result2 = calculateEx2(content, 256)
    print("Result:" + str(result2))

    hej = ""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calculate()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
