# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from utils import AoCHelper as helper


def calculate_consumption(content, transform=lambda number: number):
    minimum = min(content)
    maximum = max(content)
    final = min([sum([transform(abs(position - elm)) for elm in content]) for position in range(minimum, maximum)])
    return final


def calculate():
    # Use a breakpoint in the code line below to debug your script.
    content = [int(element) for element in helper.splitFile("day7.txt", ",")]

    print("Start 1:")
    result = calculate_consumption(content)
    print("Result: " + str(result))

    print("Start 2:")
    result2 = calculate_consumption(content, lambda number: divmod(number * (number + 1), 2)[0])
    print("Result: " + str(result2))

    hej = ""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calculate()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
