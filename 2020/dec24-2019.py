from utils import aoc_helper as helper


def calculate():
    # Use a breakpoint in the code line below to debug your script
    hej = ""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    content = helper.split_file("test.txt", "\n")
    matrix = [list(element.replace("#", "1").replace(".", "0")) for element in content]
    for flist in matrix:
        for slist in flist:
            f
    print(calculate())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
