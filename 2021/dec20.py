from utils import aoc_helper as helper
import numpy as np
import copy as cc


def apply_once(input, algorithm, v):
    embedded = helper.embed_matrix(cc.deepcopy(input), v, np.int64, 2)
    copy = cc.deepcopy(embedded)
    for idx, elm_x in enumerate(embedded):
        for idy, elm_y in enumerate(elm_x):
            if 0 < idx < len(embedded) - 1 and 0 < idy < len(elm_x) - 1:
                adj = list(helper.get_neighbours_dict(embedded, idx, idy).keys())
                adj.append((idx, idy))
                adj = sorted(adj)
                pixels = ''.join([str(embedded[x][y]) for x, y in adj])
                number = int(pixels, 2)
                translate = int(algorithm[number])
                copy[idx][idy] = translate
    for idx, elm_x in enumerate(embedded):
        for idy, elm_y in enumerate(elm_x):
            if idx == 0 or idx == len(embedded) - 1 or idy == 0 or idy == len(elm_x) - 1:
                copy[idx][idy] = copy[1][1]
    return copy


@helper.profiler
def apply(image, algorithm, times):
    if times <= 0:
        return image
    else:
        result = apply_once(image, algorithm, 0)
        for i in range(1, times):
            result = apply_once(result, algorithm, result[0][0])
        return result, np.sum(result == 1)


if __name__ == '__main__':
    algorithm, image_raw = helper.split_file("day20.txt", "\n\n")
    algorithm = algorithm.replace("#", str(1)).replace(".", str(0))
    image_raw = image_raw.replace("#", str(1)).replace(".", str(0))
    image = np.array([list(elm) for elm in image_raw.split("\n")]).astype(np.int64)
    applied1, count1 = apply(image, algorithm, 2)
    print(f"Result 1: {str(count1)}")

    applied2, count2 = apply(image, algorithm, 50)
    print(f"Result 2: {str(count2)}")

