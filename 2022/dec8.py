from utils import AoCHelper as helper
from pathlib import Path
from operator import mul
from functools import reduce


def get_rays(r, c, content_list) -> tuple[list, list, list, list]:
    top = [row[c] for row in content_list[:r]]
    bottom = [row[c] for row in content_list[r + 1:]]
    left = [col for col in content_list[r][:c]]
    right = [col for col in content_list[r][c + 1:]]
    return top, bottom, left, right


@helper.profiler
def part1(content_list):
    visible_count = 0
    for r, row in enumerate(content_list):
        for c, element in enumerate(row):
            top, bottom, left, right = get_rays(r, c, content_list)
            if any(len(e) == 0 or max(e) < element for e in [top, bottom, left, right]):
                visible_count += 1
    return visible_count


@helper.profiler
def part2(content_list):
    score = dict()
    for r, row in enumerate(content_list):
        for c, element in enumerate(row):
            a_top, a_bottom, a_left, a_right = get_rays(r, c, content_list)
            multipliers = []
            for lst in [list(reversed(a_top)), a_bottom, list(reversed(a_left)), a_right]:
                mult = 0
                for e in lst:
                    mult += 1
                    if element <= e:
                        break
                multipliers.append(mult)
            product = reduce(mul, multipliers, 1)
            if product > 0:
                score[(r, c)] = product
    max_score = max(score.values())
    return max_score


if __name__ == '__main__':
    content = Path("data/day8.txt").read_text().split("\n")
    content_2d = [[(int(i)) for i in list(e)] for e in content]

    print(f"Result 1: {str(part1(content_2d))}")
    print(f"Result 2: {str(part2(content_2d))}")
