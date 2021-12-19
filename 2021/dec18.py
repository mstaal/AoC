import math

from utils import AoCHelper as helper
import json
import re
import copy as cp


d = "(\d)|(\d\d)|(\d\d\d)|(\d\d\d\d)|(\d\d\d\d\d)"
regex = f"(\[\[{d},{d}\],{d}\])|(\[{d},\[{d},{d}\]\])"


def insert_after_or_before(new, inner):
    start, end = str(new).replace(" ", "").split("x")
    start = start[0:len(start)-1]
    end = end[1:]

    matches_start = list(re.finditer(d, start))
    matches_end = list(re.finditer(d, end))
    if len(matches_start) == 0 and len(matches_end) == 0:
        return json.loads(str(new).replace(" ", "").replace("x", "0"))
    if len(matches_start) > 0:
        match_start = matches_start[-1]
        value_start = int(start[match_start.start():match_start.end()]) + inner[0]
        start = start[0:match_start.start()] + str(value_start) + start[match_start.end():]
    if len(matches_end) > 0:
        match_end = matches_end[0]
        value_end = int(end[match_end.start():match_end.end()]) + inner[1]
        end = end[0:match_end.start()] + str(value_end) + end[match_end.end():]
    result = json.loads(start + "0" + end)
    return result


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
                            for idw, elm_w in enumerate(elm_z):
                                if helper.depth(elm_w) >= 1:
                                    copy[idx][idy][idz][idw] = "x"
                                    complete = insert_after_or_before(copy, elm_w)
                                    return complete, True
    return input, False


def split(input):
    text_based = str(input).replace(" ", "")
    match_region = re.search("\d\d|\d\d\d", text_based)
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

