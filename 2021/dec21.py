from utils import aoc_helper as helper


def dice(times):
    return times % 100 + 1


def playgame(player1, player2):
    times = 0
    while True:
        roll1 = dice(times) + dice(times+1) + dice(times+2)
        times += 3
        player1["current"] = (player1["current"] - 1 + roll1) % 10 + 1
        player1["points"] += player1["current"]
        if player1["points"] >= 1000:
            break

        roll2 = dice(times) + dice(times+1) + dice(times+2)
        times += 3
        player2["current"] = (player2["current"] - 1 + roll2) % 10 + 1
        player2["points"] += player2["current"]
        if player2["points"] >= 1000:
            break
    res1 = times * min(player1["points"], player2["points"])
    return res1


def playgame_2(players, current, dice_num, remaining):
    while True:

        roll1 = dice(dice_num) + dice(dice_num+1) + dice(dice_num+2)
        player1["current"] = (player1["current"] - 1 + roll1) % 10 + 1
        player1["points"] += player1["current"]
        if player1["points"] >= 21:
            break
    return "res1"

if __name__ == '__main__':
    content = [e.split(" starting position: ") for e in helper.split_file("day21.txt", "\n")]
    player1 = {"player": content[0][0], "current": int(content[0][1]), "points": 0}
    player2 = {"player": content[1][0], "current": int(content[1][1]), "points": 0}
    players = {"P1": player1, "P2": player2}
    res = playgame(player1, player2)
    res2 = playgame_2(players, "P1", 0, 3)
    hfhf = ""

