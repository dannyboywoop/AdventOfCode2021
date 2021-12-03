from aoc_tools import Advent_Timer


def read_input(filename="input.txt"):
    with open(filename, "r") as file:
        data = [line.strip().split() for line in file]
    return data


def make_move(move, depth, position):
    direction, distance = move

    if direction == "forward":
        position += int(distance)
    elif direction == "down":
        depth += int(distance)
    elif direction == "up":
        depth -= int(distance)

    return depth, position


def make_all_moves(move_set):
    position = 0
    depth = 0

    for move in move_set:
        depth, position = make_move(move, depth, position)

    return depth, position


if __name__ == "__main__":
    timer = Advent_Timer()

    # parse input
    data = read_input()
    print("Input parsed!")
    timer.checkpoint_hit()

    # star 1
    depth, position = make_all_moves(data)
    print("Star 1: {}".format(depth*position))
    timer.checkpoint_hit()

    # star 2
    timer.checkpoint_hit()

    timer.end_hit()
