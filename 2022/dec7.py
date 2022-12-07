from utils import AoCHelper as helper
from pathlib import Path


def parse_content(content_list):
    direc = Path("/")
    dir_manager = {}
    for idx, line in enumerate(content_list):
        if "$" in line:
            _, cmd, *args = line.split(" ")
            if cmd == "cd":
                direc = (direc / Path(args[0])).resolve(strict=False)
        else:
            first, second = line.split(" ")
            sub_dir = dir_manager.get(direc, [])
            if first == "dir":
                sub_dir.append(Path(direc) / second)
            elif first.isdigit():
                sub_dir.append((int(first), second))
            dir_manager[direc] = sub_dir
    return dir_manager


def dir_expander(dir_manager):
    dir_manager_expanded = {}
    for dir_name, dir_content in dir_manager.items():
        files = [e for e in dir_content]
        while len(files) != len([e for e in files if isinstance(e, tuple)]):
            new_files = []
            for idx, entry in enumerate(files):
                if isinstance(entry, tuple):
                    new_files.append(entry)
                else:
                    new_files += dir_manager[entry]
            files = new_files
        dir_manager_expanded[dir_name] = files
    return dir_manager_expanded


@helper.profiler
def part1(dir_manager):
    expansion = dir_expander(dir_manager)
    size_count = {direc: sum(size for size, _ in entry) for direc, entry in expansion.items()}
    size_count_filtered = {direc: count for direc, count in size_count.items() if count <= 100000}
    relevant_total = sum(size_count_filtered.values())
    return relevant_total


@helper.profiler
def part2(dir_manager):
    expansion = dir_expander(dir_manager)
    size_count = {direc: sum(size for size, _ in entry) for direc, entry in expansion.items()}
    required_by_update = 30000000 - (70000000 - size_count[Path("/")])
    relevant_sizes = {key: size for key, size in size_count.items() if size >= required_by_update}
    minimal_size_choice = size_count[list(relevant_sizes.keys())[-1]]
    return minimal_size_choice


if __name__ == '__main__':
    content = Path("data/day7.txt").read_text().split("\n")
    dirs = parse_content(content)

    print(f"Result 1: {str(part1(dirs))}")
    print(f"Result 2: {str(part2(dirs))}")
