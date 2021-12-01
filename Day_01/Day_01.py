from aoc_tools import Advent_Timer


def read_input(filename="input.txt"):
    with open(filename, "r") as file:
        data = [int(line.strip()) for line in file]
    return data


def count_rolling_average_increases(sample_size, measurements):
    count = 0
    for i in range(sample_size, len(measurements)):
        if measurements[i] > measurements[i-sample_size]:
            count += 1
    return count


if __name__ == "__main__":
    timer = Advent_Timer()

    # parse input
    data = read_input()
    print("Input parsed!")
    timer.checkpoint_hit()

    # star 1
    star_1 = count_rolling_average_increases(1, data)
    print("Start 1: {}".format(star_1))
    timer.checkpoint_hit()

    # star 2
    star_2 = count_rolling_average_increases(3, data)
    print("Start 2: {}".format(star_2))
    timer.checkpoint_hit()

    timer.end_hit()
