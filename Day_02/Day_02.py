from aoc_tools import Advent_Timer


MOVE_DEFINITIONS_1 = {
    "forward": (lambda pos, dist: (pos.x + dist, pos.depth, pos.aim)),
    "down": (lambda pos, dist: (pos.x, pos.depth + dist, pos.aim)),
    "up": (lambda pos, dist: (pos.x, pos.depth - dist, pos.aim))
}


MOVE_DEFINITIONS_2 = {
    "forward": (lambda pos, dist: (pos.x + dist,
                                   pos.depth + pos.aim*dist,
                                   pos.aim)),
    "down": (lambda pos, dist: (pos.x, pos.depth, pos.aim + dist)),
    "up": (lambda pos, dist: (pos.x, pos.depth, pos.aim - dist))
}


class Position:
    def __init__(self, x=0, depth=0, aim=0):
        self.x = x
        self.depth = depth
        self.aim = aim

    def make_move(self, move, move_defs):
        direction, dist = move

        self.x, self.depth, self.aim = move_defs[direction](self, dist)


def read_input(filename="input.txt"):
    with open(filename, "r") as file:
        data = [line.strip().split() for line in file]
        data_cast = [(direction, int(dist)) for direction, dist in data]
    return data_cast


def make_all_moves(move_set, move_definitions):
    position = Position()

    for move in move_set:
        position.make_move(move, move_definitions)

    return position


if __name__ == "__main__":
    timer = Advent_Timer()

    # parse input
    data = read_input()
    print("Input parsed!")
    timer.checkpoint_hit()

    # star 1
    position_1 = make_all_moves(data, MOVE_DEFINITIONS_1)
    print("Star 1: {}".format(position_1.x * position_1.depth))
    timer.checkpoint_hit()

    # star 2
    position_2 = make_all_moves(data, MOVE_DEFINITIONS_2)
    print("Star 2: {}".format(position_2.x * position_2.depth))
    timer.checkpoint_hit()

    timer.end_hit()
