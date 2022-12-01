from utils import AoCHelper as helper
from pathlib import Path


if __name__ == '__main__':
    # calories = array([sum([int(e) for e in element.split("\n")]) for element in helper.splitFile("day1.txt", "\n\n")])
    content = Path("data/day1.txt").read_text(encoding="UTF-8")
    calories = sorted((sum((int(e) for e in element.split("\n"))) for element in content.split("\n\n")), reverse=True)

    question1 = calories[0]
    question2 = sum(calories[0:3])
    # Alternative: https://stackoverflow.com/questions/6910641/how-do-i-get-indices-of-n-maximum-values-in-a-numpy-array
    # question2 = sum([calories[i] for i in calories.argsort()[-3:][::-1]])
    print(f"Result 1: {str(question1)}")
    print(f"Result 2: {str(question2)}")