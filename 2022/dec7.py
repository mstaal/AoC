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
                dir_manager[direc] = sub_dir
            elif first.isdigit():
                sub_dir.append((int(first), second))
                dir_manager[direc] = sub_dir
    return dir_manager


def dir_expander(dir_manager):
    dir_size_manager = {}
    for dir_name, content in dir_manager.items():
        files = [e for e in content]
        while len(files) != len([e for e in files if isinstance(e, tuple)]):
            new_files = []
            for idx, entry in enumerate(files):
                if isinstance(entry, tuple):
                    new_files.append(entry)
                else:
                    new_files += dir_manager[entry]
            files = new_files
        dir_size_manager[dir_name] = files
    return dir_size_manager


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
    total_size = size_count[Path("/")]
    demanded_unused_space = 70000000 - total_size
    required = 30000000 - demanded_unused_space
    relevant_sizes = {key: size for key, size in size_count.items() if size >= required}
    minimal_size_choice = size_count[list(relevant_sizes.keys())[-1]]
    return minimal_size_choice


if __name__ == '__main__':
    content = Path("data/day7.txt").read_text().split("\n")
    dirs = parse_content(content)

    question1 = part1(dirs)
    question2 = part2(dirs)

    print(f"Result 1: {str(question1)}")
    print(f"Result 2: {str(question2)}")
