## All directions for traversing af grid
all_directions = list(set([(x, y) for x in [-1, 0, 1] for y in [-1, 0, 1]]).difference([(0, 0)]))
all_directions_dict = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0), 'NW': (-1, 1), 'NE': (1, 1), 'SE': (1, -1), 'SW': (-1, -1)}

## North, south, east, west
cardinal_directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
cardinal_directions_dict = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}

## All directions for traversing 3d grid
all_directions_3d = list(set([(x, y, z) for x in [-1, 0, 1] for y in [-1, 0, 1] for z in [-1, 0, 1]]).difference([(0, 0, 0)]))
cardinal_directions_3d = [(-1, 0, 0), (0, -1, 0), (0, 0, -1), (0, 0, 1), (0, 1, 0), (1, 0, 0)]
