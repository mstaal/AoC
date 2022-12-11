import re

from utils import aoc_helper as helper

directions = {
    'e': (2, 0),
    'se': (1, -1),
    'sw': (-1, -1),
    'w': (-2, 0),
    'nw': (-1, 1),
    'ne': (1, 1)
}




def regexSplitter(text, regex):
    result = []
    while len(text) > 0:
        match = re.match(regex, text)
        piece = text[match.start():match.end()]
        result.append(piece)
        text = text[match.end():]
    return result


def neighbors(tile):
    yield from ((tile[0] + dx, tile[1] + dy) for dx, dy in directions.values())


def partTwo(blackTiles):
    for day in range(100):
        newTiles = set()

        affectedTiles = blackTiles.copy()
        for tile in blackTiles:
            affectedTiles.update(neighbors(tile))

        for tile in affectedTiles:
            nbCount = len([n for n in blackTiles if n in neighbors(tile)])
            if tile in blackTiles:
                if nbCount in [1, 2]:
                    newTiles.add(tile)
            else:
                if nbCount == 2:
                    newTiles.add(tile)

        blackTiles = newTiles
        print("Day: " + str(day))

    print("length: " + str(len(blackTiles)))
    return len(blackTiles)


def walk(matches):
    coordinates = []
    for match in matches:
        x, y = 0, 0
        for dir in match:
            dx, dy = directions[dir]
            x += dx
            y += dy
        coordinates.append((x, y))
    return coordinates



def calculate():
    # Use a breakpoint in the code line below to debug your script.
    # Part 1
    content = helper.split_file("day24.txt", "\n")
    regex = "(e|se|sw|w|nw|ne)"
    matches = [regexSplitter(element, regex) for element in content]
    coordinates = walk(matches)
    counts = {element: coordinates.count(element) for element in coordinates}
    blackTiles = {element for element, count in counts.items() if count % 2 == 1}
    count = len(blackTiles)

    # Part 2
    partTwo(blackTiles)
    day1 = {element: True for element, count in counts.items()}

    hfhhf = ""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calculate()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
