from tabnanny import check
from utils import aoc_helper as helper
from pathlib import Path


def pairwise(iterable):
    it = iter(iterable)
    a = next(it, None)

    for b in it:
        yield (a, b)
        a = b


def check_safe(report: list[int]) -> bool:
    report_a, report_b = sorted(report), sorted(report, reverse=True)
    distances = [b - a for a, b in pairwise(report_a)]
    if (report == report_a or report == report_b) and all([e > 0 and e <=3 for e in distances]):
        return True
    return False


def check_safe_adjusted(report: list[int]) -> bool:
    if check_safe(report):
        return True
    for idx, _ in enumerate(report):
        copy = report.copy()
        del copy[idx]
        if check_safe(copy):
            return True
    return False


def question_1(reports):
    safe_reports = [e for e in reports if check_safe(e)]
    count = len(safe_reports)
    return count


def question_2(reports):
    safe_reports = [e for e in reports if check_safe_adjusted(e)]
    count = len(safe_reports)
    return count


if __name__ == '__main__':
    content: list[str] = Path("2024/data/day2.txt").read_text(encoding="UTF-8").split("\n")
    reports = [list(map(int, e.split(" "))) for e in content]

    question1 = question_1(reports)
    question2 = question_2(reports)

    print(f"Result 1: {str(question1)}")
    print(f"Result 2: {str(question2)}")
