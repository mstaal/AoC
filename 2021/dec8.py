# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from utils import aoc_helper as helper


def decode(content):
    split = lambda text: ["".join(sorted(element)) for element in text.split(" ")]
    patterns = split(content[0])
    output = split(content[1])
    basic_filter = lambda number: [ptrn for ptrn in patterns if len(ptrn) == number]
    number_dict = {1: basic_filter(2)[0], 4: basic_filter(4)[0], 7: basic_filter(3)[0], 8: basic_filter(7)[0]}
    adv_filter = lambda number, idx, diff: [ptrn for ptrn in patterns if len(ptrn) == number and len(set(ptrn).difference(number_dict[idx])) == diff]
    not_filter = lambda number, lst=[]: [pattern for pattern in patterns if len(pattern) == number and not lst.__contains__(pattern)]
    number_dict[3] = adv_filter(5, 1, 3)[0]
    number_dict[6] = adv_filter(6, 7, 4)[0]
    number_dict[5] = adv_filter(5, 6, 0)[0]
    number_dict[9] = "".join(sorted(set(number_dict[4]).union(number_dict[5])))
    number_dict[0] = not_filter(6, [number_dict[6], number_dict[9]])[0]
    number_dict[2] = not_filter(5, [number_dict[3], number_dict[5]])[0]
    pattern_dict = helper.reverse_dict(number_dict)

    calc = int("".join([str(pattern_dict[element]) for element in output]))
    return calc


def calculate():
    # Use a breakpoint in the code line below to debug your script.
    content = [element for element in helper.split_file("day8.txt", "\n")]
    exer1content = helper.flatten([element.split(" | ")[1].split(" ") for element in content])
    exer1result = len([elm for elm in exer1content if [2, 3, 4, 7].__contains__(len(elm))])
    print("Result 1: " + str(exer1result))

    exer2content = [(elm[0], elm[1]) for elm in [element.split(" | ") for element in content]]
    exer2result = sum([decode(element) for element in exer2content])
    print("Result 2: " + str(exer2result))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calculate()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
