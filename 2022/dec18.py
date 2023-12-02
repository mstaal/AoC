from utils import aoc_helper as helper
from pathlib import Path
from scipy.spatial import ConvexHull, Delaunay
import numpy as np

from utils.aoc_types import T

eps = np.finfo(np.float32).eps


class Cube:
    def __init__(self, x, y, z, radius=1):
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius

        self.points = [T(self.x, self.y, self.z), T(self.x + self.radius, self.y, self.z),
                       T(self.x, self.y + self.radius, self.z), T(self.x, self.y, self.z + self.radius),
                       T(self.x + self.radius, self.y + self.radius, self.z + self.radius),
                       T(self.x, self.y + self.radius, self.z + self.radius),
                       T(self.x + self.radius, self.y, self.z + self.radius),
                       T(self.x + self.radius, self.y + self.radius, self.z)]

    def __contains__(self, item):
        return all((element - item).length() <= T(1, 1, 1).length() for element in self.points)

    def contains(self, item):
        return __contains__(self, item)


class CubeCollection:
    def __init__(self, collection: list[Cube]):
        self.cubes = collection

    def __contains__(self, item):
        return any(item in cube for cube in self.cubes)


def parse_input(input):
    x, y, z = input
    side_1 = tuple((x + idx, y + idy, z) for idx in range(0, 2) for idy in range(0, 2))
    side_2 = tuple((x + idx, y + idy, z+1) for idx in range(0, 2) for idy in range(0, 2))
    side_3 = tuple((x + idx, y, z + idz) for idx in range(0, 2) for idz in range(0, 2))
    side_4 = tuple((x + idx, y+1, z + idz) for idx in range(0, 2) for idz in range(0, 2))
    side_5 = tuple((x, y + idy, z + idz) for idy in range(0, 2) for idz in range(0, 2))
    side_6 = tuple((x+1, y+idy, z + idz) for idy in range(0, 2) for idz in range(0, 2))
    sides = [side_1, side_2, side_3, side_4, side_5, side_6]
    return sides


@helper.profiler
def part1(content_input):
    open_sides = set()
    for idc, cube in enumerate(content_input):
        remaining = set(e for i, r in enumerate(content_input) if i != idc for e in r)
        open_sides.update(set(cube).difference(remaining))
    return open_sides


@helper.profiler
def part2(content_input):
    open_sides = set()
    for idc, cube in enumerate(content_input):
        remaining = set(e for i, r in enumerate(content_input) if i != idc for e in r)
        points = np.array([np.array(t) for i, r in enumerate(content_input) if i != idc for e in r for t in e])
        hull = ConvexHull(points)
        A, b = hull.equations[:, :-1], hull.equations[:, -1:]
        contained = all(np.all(np.asarray(cube[0]) @ A.T + b.T < eps, axis=1))
        diff = set(cube).difference(remaining)
        a = Cube(0, 0, 0)
        if T(1, 0, 0) in a:
            hej = ""
        if not contained:
            open_sides.update(diff)
    return open_sides


if __name__ == '__main__':
    content = [parse_input(tuple([int(i) for i in e.split(",")])) for e in Path("data/day18-sample.txt").read_text().split("\n")]

    print(f"Result 2: {str(part2(content))}")
    print(f"""Result 1: {str(len(part1(content)))}""")
