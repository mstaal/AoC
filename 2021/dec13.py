from utils import AoCHelper as helper
import numpy as np
import matplotlib.pyplot as plt


def exercise(coordinates, folds):
    for c, size in folds:
        temp = set()
        for x, y in coordinates:
            if c == "y":
                temp.add((x, size - abs(y - size) if y > size else y))
            if c == "x":
                temp.add((size - abs(x - size) if x > size else x, y))
        coordinates = temp
    return coordinates


def plot(coordinates, folds):
    result = exercise(coordinates, folds)
    points = [np.array(p).dot([[1, 0], [0, -1]]) for p in list(result)]
    plt.scatter([x for x, y in points], [y for x, y in points])
    plt.show()


if __name__ == '__main__':
    coordinates_content, fold_content = [element for element in helper.splitFile("day13.txt", "\n\n")]
    coordinates = set((int(elm.split(",")[0]), int(elm.split(",")[1])) for elm in coordinates_content.split("\n"))
    folds = [(c[-1], int(number)) for c, number in [elm.split("=") for elm in fold_content.split("\n")]]

    print(f"Result 1: {str(len(exercise(coordinates, folds[0:1])))}")
    plot(coordinates, folds)
