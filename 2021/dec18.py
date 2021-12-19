import math

from utils import AoCHelper as helper
from difflib import SequenceMatcher
import json
import re
import copy as cp


d = "(\d)|(\d\d)|(\d\d\d)|(\d\d\d\d)|(\d\d\d\d\d)"
regex = f"(\[\[{d},{d}\],{d}\])|(\[{d},\[{d},{d}\]\])"


def insert_after_or_before(old, new, old_inner, new_inner, previous):
    seq_match = SequenceMatcher(None, str(old).replace(" ", ""), str(new).replace(" ", ""))
    end_idx = seq_match.get_matching_blocks()[0].size
    start = str(old).replace(" ", "")[0:end_idx - 1]
    end = str(old).replace(" ", "")[end_idx + len(old_inner) - 1:]
    parsed_list = json.loads(old_inner)
    if previous:
        matches = list(re.finditer(d, start))
        if len(matches) == 0:
            return str(new).replace(" ", "")
        match = matches[-1]
        value = int(start[match.start():match.end()]) + parsed_list[0][0]
        start = start[0:match.start()] + str(value) + start[match.end():]
        return start + new_inner + end
    else:
        matches = list(re.finditer(d, end))
        if len(matches) == 0:
            return str(new).replace(" ", "")
        match = matches[0]
        value = int(end[match.start():match.end()]) + parsed_list[1][1]
        end = end[0:match.start()] + str(value) + end[match.end():]
        return start + new_inner + end


def explode(input):
    if helper.depth(input) <= 4:
        return input, False
    copy = cp.deepcopy(input)
    for idx, elm_x in enumerate(input):
        if helper.depth(elm_x) >= 4:
            for idy, elm_y in enumerate(elm_x):
                if helper.depth(elm_y) >= 3:
                    for idz, elm_z in enumerate(elm_y):
                        if helper.depth(elm_z) >= 2:
                            text_based = str(elm_z).replace(" ", "")
                            match = re.search(regex, text_based)
                            simple_list = json.loads(match.string)
                            if isinstance(simple_list[0], int):
                                previous = False
                                new_element = [simple_list[0] + simple_list[1][0], 0]
                            else:
                                previous = True
                                new_element = [0, simple_list[1] + simple_list[0][1]]
                            new_element_text = str(new_element).replace(" ", "")
                            new_text = text_based.replace(match.string, new_element_text, 1)
                            new_inner_list = json.loads(new_text)
                            copy[idx][idy][idz] = new_inner_list
                            complete_text = insert_after_or_before(input, copy, text_based, new_text, previous)
                            complete = json.loads(complete_text)
                            return complete, True
    return input, False


def split(input):
    text_based = str(input).replace(" ", "")
    match_region = re.search("\d\d", text_based)
    if match_region is None:
        return input, False
    element = int(text_based[match_region.regs[0][0]:match_region.regs[0][1]])
    new_inner_list = [math.floor(element / 2), math.ceil(element / 2)]
    new_list_text = str(new_inner_list).replace(" ", "")
    new_text_based = text_based.replace(str(element), new_list_text, 1)
    result = json.loads(new_text_based)
    return result, True


def one_calculation(added):
    while helper.depth(added) > 4:
        added = explode(added)[0]
    added, spl_result = split(added)
    if not spl_result:
        return added
    else:
        return one_calculation(added)


def calculate(content):
    result = content[0] if len(content) > 0 else None
    for idx, element in enumerate(content[1:]):
        added = [result, element]
        result = one_calculation(added)
    hhf = ""


if __name__ == '__main__':
    content = [json.loads(element) for element in helper.splitFile("day18.txt", "\n")]

    calculate(content)

    [split(split(element)[0]) for element in content]

