from utils import aoc_helper as helper


def parseLine(line):
    mode, rest = line.split(" ")
    x_part, y_part, z_part = rest.split(",")
    x = tuple([int(e) for e in x_part[2:].split("..")])
    y = tuple([int(e) for e in y_part[2:].split("..")])
    z = tuple([int(e) for e in z_part[2:].split("..")])
    return mode, x, y, z


def limitRange(left, right):
    return range(max(-50, left), min(50, right)+1)


def get_ons_ex1(content):
    overview = set()
    for idx, elm in enumerate(content):
        print(idx)
        if elm[0] == "on":
            overview.update((x, y, z) for x in limitRange(elm[1][0], elm[1][1]) for y in limitRange(elm[2][0], elm[2][1]) for z in limitRange(elm[3][0], elm[3][1]))
        else:
            overview.difference_update((x, y, z) for x in limitRange(elm[1][0], elm[1][1]) for y in limitRange(elm[2][0], elm[2][1]) for z in limitRange(elm[3][0], elm[3][1]))
    return len(overview)


if __name__ == '__main__':
    content = [parseLine(e) for e in helper.splitFile("day22.txt", "\n")]
    result1 = get_ons_ex1(content)
    hfh = ""

