# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time
from collections import Counter

import pandas as pd
from utils import AoCHelper as helper
import numpy as np
import sympy
import itertools
import re
import copy as cc
from functools import reduce
from itertools import permutations, combinations, chain, product

signLambda = lambda letter: 1 if letter == "R" else -1

def generateRules(departure):
    rulesRough = [element.split(": ") for element in departure]
    rules = {element[0]: element[1] for element in rulesRough}
    for key in rules.keys():
        rule = rules[key].split(" or ")
        listOne = [int(el) for el in rule[0].split("-")]
        listTwo = [int(el) for el in rule[1].split("-")]
        ruleNew = list(set(range(listOne[0], listOne[1] + 1)).union(set(range(listTwo[0], listTwo[1] + 1))))
        rules[key] = ruleNew
    return rules


def firstExercise(departure, nearby):
    rulesFlattened = [element for element in generateRules(departure).values()]
    invalid = []
    nearbyFlattened = [int(item) for sublist in nearby for item in sublist]
    for piece in nearbyFlattened:
        valid = False
        for rule in rulesFlattened:
            if piece in rule:
                valid = True
                break
        if not valid:
            invalid.append(piece)
    return invalid


def validTickets(departure, nearby):
    invalidNumbers = firstExercise(departure, nearby)
    valid = []
    for ticket in nearby:
        if len(set([int(el) for el in ticket]).intersection(invalidNumbers)) == 0:
            valid.append(ticket)
    return valid


def getOrderingCandidate(valid, rules):
    orderingCandidate = {}
    for idx in range(0, len(valid[0])):
        elementsByIdx = [int(element[idx]) for element in valid]
        for key, rule in rules.items():
            if set(elementsByIdx) <= set(rule):
                order = orderingCandidate.get(idx, [])
                order.append(key)
                orderingCandidate[idx] = order
    return orderingCandidate


def getOrdering(orderingCandidate):
    ordering = {}
    for idx in range(1, len(orderingCandidate) + 1):
        orders = [item for item in orderingCandidate.items() if len(item[1]) == 1]
        order = orders[0][1][0]
        ordering[orders[0][0]] = order
        for lst in orderingCandidate.values():
            if order in lst:
                lst.remove_inner(order)
    return ordering


def secondExercise(departure, nearby, myticket, query):
    ordering = getOrdering(getOrderingCandidate(validTickets(departure, nearby), generateRules(departure)))
    orderSearchIndices = [element[0] for element in ordering.items() if query in element[1]]
    ticketRelevant = [element for idx, element in enumerate(myticket) if idx in orderSearchIndices]
    result = reduce(lambda a, b: a * b, ticketRelevant)
    return result


def calculate():
    # Use a breakpoint in the code line below to debug your script.
    content = helper.splitFile("day16.txt", "\n\n")
    departure = content[0].split("\n")
    myticket = [int(el) for el in content[1].split("\n")[1].split(",")]
    nearbyticket = [element.split(",") for element in content[2].split("\n")[1:]]

    firstExercise(departure, nearbyticket)
    secondExercise(departure, nearbyticket, myticket, "departure")
    hj = ""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calculate()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
