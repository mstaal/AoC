from utils import aoc_helper as helper
from pathlib import Path


def compute_register(content_list):
    register = [1]
    for idx, cmd in enumerate(content_list):
        _, *rest = cmd.split(" ")
        register.append(register[-1])
        if len(rest) > 0:
            register.append(register[-1]+int(rest[0]))
    return register


@helper.profiler
def part1(content_list):
    return sum([(20+i*40) * compute_register(content_list)[:240][(20+i*40)-1] for i in range(6)])


@helper.profiler
def part2(content_list):
    register = compute_register(content_list)
    text = ""
    for group in [register[i:i + 40] for i in range(0, len(register)-1, 40)]:
        sprite = 0
        line = ""
        for current_pixel, element in enumerate(group):
            line += "#" if current_pixel in range(sprite, sprite+3) else "."
            sprite = group[current_pixel + 1] - 1 if current_pixel+1 < len(group) else None
        text += f"\n{line}"
    return text


if __name__ == '__main__':
    content = Path("data/day10.txt").read_text().split("\n")

    print(f"Result 1: {str(part1(content))}")
    print(f"Result 2: {str(part2(content))}")
