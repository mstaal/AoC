from utils import AoCHelper as helper

signLambda = lambda letter: 1 if letter == "R" else -1

def generateFirst(content, face, coords, dirs):
    nextDirLambda = lambda next: dirs[divmod(next, 4)[1]]
    for element in content:
        letter, number = element[0], int(element[1:])
        currentDir = dirs.index(face)
        if letter == "F":
            coords[face] = max(coords[face] + number, 0)
        if letter in ["R", "L"]:
            face = nextDirLambda(currentDir + signLambda(letter) * int(number / 90))
        if letter in dirs:
            nextDir = nextDirLambda(dirs.index(letter) - 2)
            s = coords.get(nextDir, 0)
            coords[nextDir] = max(s - number, 0)
            coords[letter] = coords.get(letter, 0) + number - s if coords.get(nextDir, 0) <= 0 else coords[letter]
    sum = abs(coords["E"]-coords["W"]) + abs(coords["N"] - coords["S"])
    return sum

def generateSecond(content, coords, dirs, waypoint):
    nextDirLambda = lambda next: dirs[divmod(next, 4)[1]]
    for element in content:
        letter, number = element[0], int(element[1:])
        newWaypoint = {}
        waykeys = list(waypoint.keys())
        turn = int(number / 90)
        if letter == "F":
            for key in waykeys:
                coords[key] = max(coords.get(key, 0) + waypoint[key] * number, 0)
        if letter in ["R", "L"]:
            for key in waykeys:
                newWaypoint[nextDirLambda(dirs.index(key) + signLambda(letter)*turn)] = waypoint.get(key, 0)
            waypoint = newWaypoint
        if letter in dirs:
            nextDir = nextDirLambda(dirs.index(letter) - 2)
            s = waypoint.get(nextDir, 0)
            waypoint[nextDir] = max(s - number, 0)
            waypoint[letter] = waypoint.get(letter, 0) + number - s if waypoint.get(nextDir, 0) <= 0 else waypoint[letter]
    sum = abs(coords["E"]-coords["W"]) + abs(coords["N"] - coords["S"])
    return sum

def calculate():
    # Use a breakpoint in the code line below to debug your script.
    content = helper.splitFile("day12.txt", "\n")
    dirs = ["E", "S", "W", "N"]
    generateFirst(content, "E", {"E": 0, "S": 0, "W": 0, "N": 0}, dirs)
    generateSecond(content, {"E": 0, "S": 0, "W": 0, "N": 0}, dirs, {"E": 10, "N": 1})
    hh = ""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calculate()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
