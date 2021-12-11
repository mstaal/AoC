import copy as cc
from utils import AoCHelper as helper


def flash_handling(content, memory):
    flashing = {(idx, idy): content[idx][idy] for idx in range(0, len(content)) for idy in range(0, len(content[0])) if content[idx][idy] > 9}
    flashing_filtered = {k: v for k, v in flashing.items() if k not in memory.keys()}
    if len(flashing_filtered) == 0:
        return memory
    for x, y in flashing_filtered.keys():
        for ax, ay in helper.get_neighbours(content, x, y, ignore_none=True).keys():
            content[ax][ay] += 1
    memory.update(flashing_filtered)
    return flash_handling(content, memory)


def perform_step(content):
    for idx in range(len(content)):
        for idy in range(len(content[0])):
            content[idx][idy] = content[idx][idy] + 1
    memory = flash_handling(content, {})
    for idx, idy in memory.keys():
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
