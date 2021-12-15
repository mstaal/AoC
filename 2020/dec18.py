import utils.AoCHelper as helper
from utils.abcTypes import Infix


# https://code.activestate.com/recipes/384122/
# http://tomerfiliba.com/blog/Infix-Operators/
mul = Infix(lambda x, y: x * y)
add = Infix(lambda x, y: x + y)


if __name__ == '__main__':
    content = helper.splitFile("day18.txt", "\n")
    firstExercise = sum([eval(element.replace("+", "|add|").replace("*", "|mul|")) for element in content])
    secondExercise = sum([eval(element.replace("*", "|mul|")) for element in content])
    print(f"Result 1: {str(firstExercise)}")
    print(f"Result 3: {str(secondExercise)}")
