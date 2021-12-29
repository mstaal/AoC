from utils import AoCHelper as helper


def velocity_at_time(velocity, t):
    x = max(velocity[0] - (t - 1) if velocity[0] > 0 else (velocity[0] + (t - 1) if velocity[0] < 0 else 0), 0)
    y = velocity[1] - (t - 1)
    return x, y


def move(velocity, area):
    info = {"h": 0, "point": (0, 0), "t": 1, "velocity": velocity, "works": False}
    while True:
        vel = velocity_at_time(velocity, info["t"])
        info["point"] = (info["point"][0] + vel[0], info["point"][1] + vel[1])
        info["h"] = max(info["h"], info["point"][1])
        if area[0][0] <= info["point"][0] <= area[0][1] and area[1][0] <= info["point"][1] <= area[1][1]:
            info["works"] = True
            return info
        if info["point"][0] > area[0][1] or info["point"][1] < area[1][1]:
            return info
        info["t"] += 1


def exercise1(area, velocities):
    results = [move(vel, area) for vel in velocities]
    results_filtered = [x for x in results if x["works"]]
    maximum = max([r["h"] for r in results_filtered])
    max_results = [res for res in results_filtered if res["h"] == maximum]
    return maximum


if __name__ == '__main__':
    content = helper.splitFile("day17.txt", "\n")
    input = [elm[2:].split("..") for elm in [element.replace("target area: ", "").split(", ") for element in content][0]]
    area = ((int(input[0][0]), int(input[0][1])), (int(input[1][0]), int(input[1][1])))
    velocities = [(x, y) for x in range(0, area[0][1]) for y in range(-abs(area[1][0]), abs(area[1][0]))]
    res1 = exercise1(area, velocities)
    print(f"Result 1: {str(res1)}")


