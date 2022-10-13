from aoc_tools import Advent_Timer


NEIGHBOURS = {}
MAP_DATA = {}


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_neighbours(self):
        if self not in NEIGHBOURS:
            neighbours = []
            for delta_x in [-1, 1]:
                neighbour = Point(self.x + delta_x, self.y)
                if neighbour in MAP_DATA:
                    neighbours.append(neighbour)

            for delta_y in [-1, 1]:
                neighbour = Point(self.x, self.y + delta_y)
                if neighbour in MAP_DATA:
                    neighbours.append(neighbour)

            NEIGHBOURS[self] = neighbours
        
        return NEIGHBOURS[self]

    def is_low_point(self):
        low_point = True
        for neighbour in self.get_neighbours():
            if MAP_DATA[neighbour] <= MAP_DATA[self]:
                low_point = False
                break
        return low_point

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


def read_input(filename="input.txt"):
    with open(filename, "r") as file:
        data = [[int(x) for x in line.strip()] for line in file]
        map_data = {Point(i, j): data[i][j]
                    for i in range(len(data))
                    for j in range(len(data[i]))}                          
    return map_data


def star_1():
    total = 0
    low_points = []
    for point, height in MAP_DATA.items():
        if point.is_low_point():
            low_points.append(point)
            total += height
    return low_points, total + len(low_points)


def get_basin_size(low_point):
    basin_points = set([low_point])
    edge_points = set([low_point])
    while len(edge_points) > 0:
        new_points = set()
        for edge_point in edge_points:
            for neighbour in edge_point.get_neighbours():
                if neighbour not in basin_points and MAP_DATA[neighbour] < 9:
                    new_points.add(neighbour)
        edge_points = new_points
        basin_points.update(edge_points)
    return len(basin_points)


def star_2(low_points):
    basin_sizes = []
    for low_point in low_points:
        basin_sizes.append(get_basin_size(low_point))
    
    product = 1
    for size in sorted(basin_sizes)[-3:]:
        product *= size
        
    return product


if __name__ == "__main__":
    timer = Advent_Timer()

    # parse input
    MAP_DATA = read_input()
    print("Input parsed!")
    timer.checkpoint_hit()

    # star 1
    low_points, star_1_answer = star_1()
    print("Star 1: {}".format(star_1_answer))
    timer.checkpoint_hit()

    # star 2
    star_2_answer = star_2(low_points)
    print("Star 2: {}".format(star_2_answer))
    timer.checkpoint_hit()

    timer.end_hit()
