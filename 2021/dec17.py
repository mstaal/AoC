from utils import AoCHelper as helper


def velocity_at_time(velocity, t):
    x = max(velocity[0] - (t - 1) if velocity[0] > 0 else (velocity[0] + (t - 1) if velocity[0] < 0 else 0), 0)
    y = velocity[1] - (t - 1)
    return x, y


def move(velocity, area):
    h = 0
    point = (0, 0)
    if area[0][0] <= point[0] <= area[0][1] and area[1][0] <= point[1] <= area[1][1]:
        return point, 0, velocity, True
    t = 0
    while True:
        vel = velocity_at_time(velocity, t)
        point = (point[0] + vel[0], point[1] + vel[1])
        h = max(h, point[1])
        if area[0][0] <= point[0] <= area[0][1] and area[1][0] <= point[1] <= area[1][1]:
            return point, h, velocity, True
        if point[0] > area[0][1] or point[1] < area[1][1]:
            return point, h, velocity, False
        t += 1



if __name__ == '__main__':
    content = helper.splitFile("day17.txt", "\n")
    input = [elm[2:].split("..") for elm in [element.replace("target area: ", "").split(", ") for element in content][0]]
    area = ((int(input[0][0]), int(input[0][1])), (int(input[1][0]), int(input[1][1])))
    velocities = [(x, y) for x in range(0, area[0][1]) for y in range(-abs(area[1][0]), abs(area[1][0]))]
    results = [move(vel, area) for vel in velocities]
    results_filtered = [x for x in results if x[3]]
    correct = [res for res in results_filtered if res[1] == max([r[1] for r in results_filtered])]
    res = move((7, 2), area)

    print(f"Result 1: {str(move((7, 2)))}")

