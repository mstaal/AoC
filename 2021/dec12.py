from utils import AoCHelper as helper


def generate_paths(map, wip, done, lower_case_limit):
    if len(wip) == 0:
        return done
    next_wip = []
    for v in wip:
        last = v[-1]
        if last == "end":
            done.append(v)
        nexts = sorted(map.get(last, set()))
        for next in nexts:
            lower_case = [elm for elm in v + [next] if elm.islower()]
            counts = len([lower_case.count(elm) for elm in lower_case if lower_case.count(elm) > 1])
            if next.isupper() or counts < lower_case_limit:
                next_wip.append(v + [next])
    return generate_paths(map, next_wip, done, lower_case_limit)


def exercise(map, lowercase_limit):
    start_candidates = [[x] for idx, x in enumerate(sorted(map.get("start", set())))]
    all_paths = generate_paths(map, start_candidates, [], lowercase_limit)
    result = len(all_paths)
    return result


if __name__ == '__main__':
    content = [element.split("-") for element in helper.splitFile("day12.txt", "\n")]
    map = {x[0]: set(y[1] for y in content if x[0] == y[0]) for x in content}
    map.update({x[1]: map.get(x[1], set()).union(set(y[0] for y in content if x[1] == y[1])) for x in content})
    for key, value in map.items():
        map[key] = set(filter(lambda x: x != "start", value))
    map.pop("end")
    print(f"Result 1: {str(exercise(map, 2))}")

    print(f"Result 2: {str(exercise(map, 3))}")
