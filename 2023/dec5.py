from utils import aoc_helper as helper
from pathlib import Path


def parse_content(cnt) -> tuple[list[int], list]:
    seed_line, remainder = cnt[0], cnt[1:]
    seeds = [int(e) for e in seed_line.split(": ")[1].split(" ")]
    lines = [[x for x in e.split("\n") if x != ""] for e in remainder]

    def parse_part(part):
        name = part[0].replace(" map:", "").strip()
        mappings_list = [tuple(int(x) for x in e.split(" ")) for e in part[1:]]
        ranges = [(range(x, x+length), range(y, y+length)) for (y, x, length) in mappings_list]

        def mapping(x):
            for idx, (x_range, y_range) in enumerate(ranges):
                if x in x_range:
                    result = y_range.start + x - x_range.start
                    return result
            return x
        return mapping
    mappings = [parse_part(line) for line in lines]
    return seeds, mappings


def question_1(sds: list[int], mppgs: list) -> int:
    locations = []
    for s in sds:
        for m in mppgs:
            s = m(s)
        locations.append(s)
    return min(locations)


def question_2(sds: list[int], mppgs: list) -> int:
    pairs = [tuple(sds[i:i + 2]) for i in range(0, len(sds), 2)]
    seed_ranges = set.union(*[set(range(x, x+length)) for (x, length) in pairs])
    locations = []
    for r in seed_ranges:
        for x in r:
            for m in mppgs:
                x = m(x)
            locations.append(x)
    return min(locations)


if __name__ == '__main__':
    content = Path("data/day5.txt").read_text(encoding="UTF-8").split("\n\n")
    seeds, mappings = parse_content(content)

    question1 = question_1(seeds, mappings)
    print(f"Result 1: {str(question1)}")
    question2 = question_2(seeds, mappings)
    print(f"Result 2: {str(question2)}")
