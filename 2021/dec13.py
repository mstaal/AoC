from utils import aoc_helper as helper
import terminalplot as tp


def exercise(coordinates, folds):
    copy = coordinates.copy()
    for c, size in folds:
        temp = set()
        for x, y in copy:
            if c == "y":
                temp.add((x, size - abs(y - size)))
            if c == "x":
                temp.add((size - abs(x - size), y))
        copy = temp
    return copy


if __name__ == '__main__':
    coordinates_content, fold_content = [element for element in helper.splitFile("day13.txt", "\n\n")]
    coordinates = set((int(elm.split(",")[0]), int(elm.split(",")[1])) for elm in coordinates_content.split("\n"))
    folds = [(c[-1], int(number)) for c, number in [elm.split("=") for elm in fold_content.split("\n")]]

    print(f"Result 1: {str(len(exercise(coordinates, folds[0:1])))}")
    print("Result 2:")
    points_to_plot = [helper.reflect_points_x(p, True) for p in exercise(coordinates, folds)]
    tp.plot([x for x, y in points_to_plot], [y for x, y in points_to_plot], 10, 60)
