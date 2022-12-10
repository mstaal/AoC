import copy as cc
from utils import aoc_helper as helper


def flash_handling(content, memory):
    flashing = set((idx, idy) for idx in range(0, len(content)) for idy in range(0, len(content[0])) if content[idx][idy] > 9)
    flashing_filtered = set(flash for flash in flashing if flash not in memory)
    if len(flashing_filtered) == 0:
        return memory
    for x, y in flashing_filtered:
        for ax, ay in helper.get_neighbours_dict(content, x, y, ignore_none=True).keys():
            content[ax][ay] += 1
    memory = memory.union(flashing_filtered)
    return flash_handling(content, memory)


def perform_step(content):
    for idx in range(len(content)):
        for idy in range(len(content[0])):
            content[idx][idy] = content[idx][idy] + 1
    memory = flash_handling(content, set())
    for idx, idy in memory:
        content[idx][idy] = 0
    return memory


def exercise1(content):
    count = 0
    for idx in range(0, 100):
        memory = perform_step(content)
        count += len(memory)
    return count


def exercise2(content):
    count = 1
    memory = perform_step(content)
    while len(memory) != len(content) * len(content[0]):
        count += 1
        memory = perform_step(content)
    return count


if __name__ == '__main__':
    content = [[int(el) for el in element] for element in helper.splitFile("day11.txt", "\n")]
    print(f"Result 1: {str(exercise1(cc.deepcopy(content)))}")

    print(f"Result 2: {str(exercise2(cc.deepcopy(content)))}")
