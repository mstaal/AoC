# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from collections import Counter

import pandas as pd
import AoCHelper as helper
import numpy as np
import sympy
from itertools import permutations



def calculate():
    # Use a breakpoint in the code line below to debug your script
    hej = ""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    content = helper.splitFile("test.txt", "\n")
    matrix = [list(element.replace("#", "1").replace(".", "0")) for element in content]
    for flist in matrix:
        for slist in flist:
            f
    print(calculate())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
