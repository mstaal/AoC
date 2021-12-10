# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
from functools import reduce
import numpy as np
import copy as cc
from itertools import permutations, combinations, chain, product

# https://code.activestate.com/recipes/384122/
# http://tomerfiliba.com/blog/Infix-Operators/
class Infix:
    def __init__(self, function):
        self.function = function

    def __ror__(self, other):
        return Infix(lambda x, self=self, other=other: self.function(other, x))

    def __or__(self, other):
        return self.function(other)

    def __rlshift__(self, other):
        return Infix(lambda x, self=self, other=other: self.function(other, x))

    def __rshift__(self, other):
        return self.function(other)

    def __call__(self, value1, value2):
        return self.function(value1, value2)


def adjac_helper(ele, sub = []):
  if not ele:
     yield sub
  else:
     yield from [idx for j in range(ele[0] - 1, ele[0] + 2)
                for idx in adjac_helper(ele[1:], sub + [j])]


def adjacent(element):
    adjacent = set([tuple(element) for element in list(adjac_helper(element))])
    adjacent.remove(element)
    return adjacent


def depth(lst):
    depth = lambda L: isinstance(L, list) and max(map(depth, L)) + 1
    return depth(lst)


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


def stringIndexLoop(text, index):
    return divmod(index, len(text))[1]


def splitFile(file, sep):
    with open(file) as file:
        content = list(file.read().split(sep))
    return content


def binaryParse(word, letter):
    number = 0
    for idx, val in enumerate(str(word)):
        factor = 2 ** (len(word) - 1 - idx)
        number = number + factor if str(val) == str(letter) else number
    return number


def baseToBinary(number, base=16):
    return bin(int(str(number), base))[2:]

def baseToHex(number, base=2):
    return hex(int(number, base))


def baseToBase10(number, base=2):
    return int(str(number), base)


def rotateArray90(array):
    return np.rot90(array)


def rotateArray180(array):
    return np.rot90(np.rot90(array))


def rotateArray270(array):
    return np.rot90(np.rot90(np.rot90(array)))


def rotateList90(lst):
    return rotateArray90(np.array(lst)).tolist()


def rotateList180(lst):
    return rotateArray180(np.array(lst)).tolist()


def rotateList270(lst):
    return rotateArray270(np.array(lst)).tolist()


def combinations(collection, repeat):
    return [list(x) for x in product(collection, repeat=repeat)]


def gcdExtended(a, b):
    # Base Case
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcdExtended(b % a, a)
    # Update x and y using results of recursive call
    x = y1 - (b // a) * x1
    y = x1
    return int(gcd), int(x), int(y)


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        gcd, x, y = gcdExtended(n_i, p)
        sum += a_i * y * p
    result = sum % prod
    return result
