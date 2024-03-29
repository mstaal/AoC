import utils.aoc_helper as helper
from utils.aoc_types import Infix


# https://code.activestate.com/recipes/384122/
# http://tomerfiliba.com/blog/Infix-Operators/
mul = Infix(lambda x, y: x * y)
add = Infix(lambda x, y: x + y)


if __name__ == '__main__':
    content = helper.split_file("day18.txt", "\n")
    firstExercise = sum([eval(element.replace("+", "|add|").replace("*", "|mul|")) for element in content])
    secondExercise = sum([eval(element.replace("*", "|mul|")) for element in content])
    print(f"Result 1: {str(firstExercise)}")
    print(f"Result 3: {str(secondExercise)}")
