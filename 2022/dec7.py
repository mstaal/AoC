from utils import aoc_helper as helper
from pathlib import Path


@helper.profiler
def parse_content(content_list):
    current_dir = Path("/")
    dir_manager = {}
    for line in content_list:
        if "$" in line:
            _, cmd, *args = line.split(" ")
            if cmd == "cd":
                current_dir = (current_dir / Path(args[0])).resolve(strict=False)
        else:
            first, second = line.split(" ")
            sub_dir = dir_manager.get(current_dir, [])
            if first == "dir":
                sub_dir.append(Path(current_dir) / second)
            elif first.isdigit():
                sub_dir.append((int(first), second))
            dir_manager[current_dir] = sub_dir
    return dir_manager


@helper.profiler
def dir_expander(dir_manager):
    dir_manager_expanded = {}
    for dir_name, dir_content in dir_manager.items():
        files = [e for e in dir_content]
        while len(files) != len([e for e in files if isinstance(e, tuple)]):
            new_files = []
            for entry in files:
                if isinstance(entry, tuple):
                    new_files.append(entry)
                else:
                    new_files += dir_manager[entry]
            files = new_files
        dir_manager_expanded[dir_name] = files
    return dir_manager_expanded


@helper.profiler
def part1(dir_manager):
    size_count = {direc: sum(size for size, _ in entry) for direc, entry in dir_manager.items()}
    size_count_filtered = {direc: count for direc, count in size_count.items() if count <= 100000}
    relevant_total = sum(size_count_filtered.values())
    return relevant_total


@helper.profiler
def part2(dir_manager):
    size_count = {direc: sum(size for size, _ in entry) for direc, entry in dir_manager.items()}
    required_by_update = 30000000 - (70000000 - size_count[Path("/")])
    relevant_sizes = {key: size for key, size in size_count.items() if size >= required_by_update}
    minimal_size_choice = size_count[list(relevant_sizes.keys())[-1]]
    return minimal_size_choice


if __name__ == '__main__':
    content = Path("data/day7.txt").read_text().split("\n")
    dirs = parse_content(content)
    manager = dir_expander(dirs)

    print(f"Result 1: {str(part1(manager))}")
    print(f"Result 2: {str(part2(manager))}")
