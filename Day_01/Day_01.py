from aoc_tools import Advent_Timer


def read_input(filename="input.txt"):
    with open(filename, "r") as file:
        data = [int(line.strip()) for line in file]
    return data


def count_increases(measurements):
    count = 0
    for i in range(1, len(measurements)):
        if measurements[i] > measurements[i-1]:
            count += 1
    return count


if __name__ == "__main__":
    timer = Advent_Timer()

    # parse input
    data = read_input()
    print("Input parsed!")
    timer.checkpoint_hit()

    # star 1
    star_1 = count_increases(data)
    print("Start 1: {}".format(star_1))
    timer.checkpoint_hit()

    # star 2
    timer.checkpoint_hit()

    timer.end_hit()
