from collections import Counter

import pandas as pd


def csvToStringList(filename, sep):
    return list(map(lambda x: str(x[0]), pd.read_csv(filename, sep, header=None).values))


def csvToIntList(filename, sep):
    return list(map(lambda x: int(x[0]), pd.read_csv(filename, sep, header=None).values))


def csvToList(filename, sep):
    return list(map(lambda x: x[0], pd.read_csv(filename, sep, header=None).values))


def csvCommaToList(filename):
    return list(map(lambda x: x, pd.read_csv(filename, ",", header=None).values[0]))


def csvCommaToIntList(filename):
    return list(map(lambda x: int(x), pd.read_csv(filename, ",", header=None).values[0]))


def isValid(word):
    colonSplit = word.split(":")
    ruleSplit = colonSplit[0].split(" ")
    interval = ruleSplit[0].split("-")
    start = int(interval[0])
    end = int(interval[1])
    character = ruleSplit[1]
    password = colonSplit[1][1:]
    occurences = Counter(password)[character]
    answer = start <= occurences <= end
    return answer


def isValid2(word):
    colonSplit = word.split(":")
    ruleSplit = colonSplit[0].split(" ")
    interval = ruleSplit[0].split("-")
    start = int(interval[0])
    end = int(interval[1])
    character = ruleSplit[1]
    password = colonSplit[1][1:]
    wordCharacter1 = password[start-1]
    wordCharacter2 = password[end-1]
    answer = (wordCharacter1 == character and wordCharacter2 != character) or (wordCharacter2 == character and wordCharacter1 != character)
    return answer


def print_prompt():
    # Use a breakpoint in the code line below to debug your script.
    numbers = csvToList("day2.txt", "\n")
    c = len(numbers)

    count = sum(isValid2(word) for word in numbers)

    hej = 22


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_prompt()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
