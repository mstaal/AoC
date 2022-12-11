from utils import aoc_helper as helper


def exercise(polymer, insertion_rules, counter):
    pair_count = {pair: polymer.count(pair) for pair in insertion_rules}
    char_count = {char: polymer.count(char) for char in insertion_rules.values()}
    for idx in range(0, counter):
        temp_count = {}
        for r_key, r_value in insertion_rules.items():
            first = r_key[0] + r_value
            second = r_value + r_key[1]
            to_add = pair_count.get(r_key, 0)
            temp_count[r_key] = temp_count.get(r_key, 0) - to_add
            temp_count[first] = temp_count.get(first, 0) + to_add
            temp_count[second] = temp_count.get(second, 0) + to_add
            char_count[r_value] = char_count.get(r_value, 0) + to_add
        pair_count = {k: v + v_t for k, v in pair_count.items() for k_t, v_t in temp_count.items() if k == k_t}
    return max(char_count.values()) - min(char_count.values())


if __name__ == '__main__':
    polymer, lines_raw = [element for element in helper.split_file("day14.txt", "\n\n")]
    insertion_rules = {element.split(" -> ")[0]: element.split(" -> ")[1] for element in lines_raw.split("\n")}

    print(f"Result 1: {str(exercise(polymer, insertion_rules, 10))}")
    print(f"Result 2: {str(exercise(polymer, insertion_rules, 40))}")
