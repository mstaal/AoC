from utils import AoCHelper as helper


def get_content_map(content):
    map = {x[0]: set(y[1] for y in content if x[0] == y[0]) for x in content}
    map.update({x[1]: map.get(x[1], set()).union(set(y[0] for y in content if x[1] == y[1])) for x in content})
    map.pop("end")
    return map


def generate_paths(map, memory, lower_case_limit):
    if len([elm[-1] for elm in memory if elm[-1] != "end"]) == 0:
        return memory
    next_memory = []
    for v in memory:
        last = v[-1]
        if last == "end":
            next_memory.append(v)
        nexts = sorted(map.get(last, set()))
        for next in nexts:
            lower_case = [elm for elm in v + [next] if elm.islower()]
            counts = len([lower_case.count(elm) for elm in lower_case if lower_case.count(elm) > 1])
            if (next.isupper() or counts < lower_case_limit) and next != "start":
                next_memory.append(v + [next])
    return generate_paths(map, next_memory, lower_case_limit)


def exercise(map, lowercase_limit):
    start_candidates = [[x] for idx, x in enumerate(sorted(map.get("start", set())))]
    all_paths = generate_paths(map, start_candidates, lowercase_limit)
    result = len(all_paths)
    return result


if __name__ == '__main__':
    content = [element.split("-") for element in helper.splitFile("day12.txt", "\n")]
    map = get_content_map(content)
    print(f"Result 1: {str(exercise(map, 2))}")

    print(f"Result 1: {str(exercise(map, 3))}")