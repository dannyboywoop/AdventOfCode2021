from aoc_tools import Advent_Timer
from numpy import sign


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return str((self.x, self.y))

    def __repr__(self):
        return self.__str__()


class Line:
    def __init__(self, line_str):
        self.end_points = [Point(*[int(val) for val in point_str.split(",")])
                           for point_str in line_str.split("->")]
        self.enumerate_points()

    def is_diagonal(self):
        return (self.end_points[0].x != self.end_points[1].x
                and self.end_points[0].y != self.end_points[1].y)

    def enumerate_points(self):
        self.points = [self.end_points[0]]
        point = self.end_points[0]
        x_dir = sign(self.end_points[1].x-self.end_points[0].x)
        y_dir = sign(self.end_points[1].y-self.end_points[0].y)
        while point != self.end_points[1]:
            point = Point(point.x + x_dir, point.y + y_dir)
            self.points.append(point)


def read_input(filename="input.txt"):
    with open(filename, "r") as file:
        data = [Line(line.strip()) for line in file]
    return data


def find_overlaps(lines):
    occurrences = {}
    for line in lines:
        if line.is_diagonal():
            continue

        for point in line.points:
            if point not in occurrences:
                occurrences[point] = 1
            else:
                occurrences[point] += 1

    return len(occurrences) - list(occurrences.values()).count(1)


if __name__ == "__main__":
    timer = Advent_Timer()

    # parse input
    lines = read_input()
    print("Input parsed!")
    timer.checkpoint_hit()

    # star 1
    star_1_answer = find_overlaps(lines)
    print("Star 1: {}".format(star_1_answer))
    timer.checkpoint_hit()

    # star 2
    timer.checkpoint_hit()

    timer.end_hit()
