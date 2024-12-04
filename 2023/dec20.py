from __future__ import annotations
from utils import aoc_helper as helper
from pathlib import Path
from collections import deque


class Module:
    def __init__(self, module_id: str, module_type: str, map_to: list[str]):
        self.module_id = module_id
        self.module_type = module_type
        self.map_to = map_to
        self.on = False
        self.pulse = "low" if module_type is None else None
        self.memory = dict()
        self.low_pulse_count = 0
        self.high_pulse_count = 0

    def __repr__(self):
        return f"({self.module_id}, {self.module_type}, {self.map_to}, {self.low_pulse_count}, {self.high_pulse_count} {self.pulse}, {self.memory})"

    def set_pulse(self, pulse: str, set_by: Module):
        if self.module_type == "%":
            if set_by.pulse == "low":
                self.on = not self.on

            self.pulse = pulse



def parse_entry(entry: list[str]):
    start, to = entry
    to_splitted = to.split(", ")
    if start == "broadcaster":
        return (None, "broadcaster"), to_splitted
    module_type, module_id = start[0], start[1:]
    return (module_type, module_id), to_splitted


def convert_to_dict(parsed: list[tuple[tuple[str, str], list[str]]]):
    representation = {module_id: (module_type, to_splitted, dict()) for (module_type, module_id), to_splitted in parsed}
    for module_id, (module_type, to_splitted, metadata) in representation.items():
        if module_type is None:
            metadata["pulse"] = "low"
        elif module_type == "%":
            metadata["on"] = False
        elif module_type == "&":
            metadata["memory"] = {k: "low" for k in representation}
    modules = {module_id: Module(module_id, module_type, to_splitted) for (module_type, module_id), to_splitted in parsed}
    return modules


@helper.profiler
def question_1(representation) -> int:
    all_ids = set(representation.keys())
    queue = deque()
    for _ in range(1):
        queue.append(representation["broadcaster"])
        while queue:
            current_module = queue.popleft()
            if current_module.module_type is None:
                for upcoming in current_module.map_to:
                    upcoming_module = representation[upcoming]
                    upcoming_module.set_pulse(current_module.pulse, current_module)
                    queue.append(upcoming_module)
            elif current_module.module_type == "%":  # Flipflop
                if current_module.pulse == "low":
                    current_module.flip_on()
                    for upcoming in current_module.map_to:
                        upcoming_module = representation[upcoming]
                        upcoming_module.set_pulse("high" if current_module.on else "low", current_module)
                        queue.append(upcoming_module)
            elif current_module.module_type == "&":  # Conjunction
                memory = {e for e in {current_module.memory.get(k, "low") for k in all_ids}}
                pulse_to_send = "high" if all(e == "high" for e in memory) else "low"
                for upcoming in current_module.map_to:
                    upcoming_module = representation[upcoming]
                    upcoming_module.set_pulse(pulse_to_send, current_module)
                    queue.append(upcoming_module)
    return ""


@helper.profiler
def question_2(input_lst) -> int:
    return ""


if __name__ == '__main__':
    parsed = [parse_entry(e.split(" -> ")) for e in Path("data/day20.txt").read_text(encoding="UTF-8").split("\n")]
    dict_rep = convert_to_dict(parsed)
    q1 = question_1(dict_rep)
    print(f"Result 1: {str(q1)}")
    q2 = question_2(parsed)
    print(f"Result 2: {str(q2)}")
