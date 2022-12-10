# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from collections import Counter

import pandas as pd
from utils import aoc_helper as helper
import numpy as np
import sympy
import re
from itertools import permutations


def isValidPassport(passport):
    return all(substring in passport for substring in ["ecl:", "pid:", "eyr:", "hcl:", "byr:", "hgt:", "iyr:"])


def intervalCheck(piece, index, start, end, count):
    return count + 1 if start <= int(piece[index:]) <= end else count


def hgt(piece, count):
    hgt = piece[4:]
    end = hgt[-2] + hgt[-1]
    if end == "cm":
        return intervalCheck(hgt.replace("cm", ""), 0, 150, 193, count)
    elif end == "in":
        return intervalCheck(hgt.replace("in", ""), 0, 59, 76, count)
    else:
        return count


def hcl(piece, count):
    match = bool(re.match("^[a-f0-9]*$", piece[5:]))
    return count + 1 if piece[4] == "#" and match else count


def pid(piece, count):
    pid = piece[4:]
    match = bool(re.match("^[0-9]*$", pid))
    return count + 1 if len(pid) == 9 and match else count


def ecl(piece, count):
    eclEnd = piece[4:]
    allowed = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return count + 1 if len(eclEnd) == 3 and eclEnd in allowed else count


def isValidPassportStrict(passport):
    elements = list(re.split('\n| ', passport))
    count = 0
    for piece in elements:
        if "byr:" in piece:
            count = intervalCheck(piece, 4, 1920, 2002, count)
        if "iyr:" in piece:
            count = intervalCheck(piece, 4, 2010, 2020, count)
        if "eyr:" in piece:
            count = intervalCheck(piece, 4, 2020, 2030, count)
        if "hgt:" in piece:
            count = hgt(piece, count)
        if "hcl:" in piece:
            count = hcl(piece, count)
        if "pid:" in piece:
            count = pid(piece, count)
        if "ecl:" in piece:
            count = ecl(piece, count)

    answer = count >= 7
    return answer


def calculate():
    # Use a breakpoint in the code line below to debug your script.
    content = helper.splitFile("day4.txt", "\n\n")

    count = 0
    for passport in content:
        if(isValidPassportStrict(passport)):
            count += 1
    hej = ""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(calculate())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
