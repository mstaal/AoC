from utils import aoc_helper as helper
from pathlib import Path
import re


pattern1 = r"\d"

digits = dict(one="1", two="2", three="3", four="4", five="5", six="6", seven="7", eight="8", nine="9")
pattern2 = r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))"


def to_digit(text: str) -> str:
    return text if text.isdigit() else digits[text]


if __name__ == '__main__':
    content = Path("data/day1.txt").read_text(encoding="UTF-8").split("\n")
    question1 = sum([int(f"{x[0]}{x[-1]}") for x in [list(re.findall(pattern1, line)) for line in content]])

    question2 = sum([int(f"{x[0]}{x[-1]}") for x in [list(map(to_digit, re.findall(pattern2, line))) for line in content]])

    print(f"Result 1: {str(question1)}")
    print(f"Result 2: {str(question2)}")
