from aoc_tools import Advent_Timer


def read_input(filename="input.txt"):
    with open(filename, "r") as file:
        data = [int(x) for x in file.read().split(",")]
    return data


def fuel_cost_1(data, point):
    total = 0
    for x in data:
        total += abs(point-x)
    return total


def best_spot_1(data):
    data.sort()
    mid, odd = divmod(len(data), 2)
    if odd:
        return fuel_cost_1(data, data[mid-1])
    else:
        return fuel_cost_1(data, data[mid])


if __name__ == "__main__":
    timer = Advent_Timer()

    # parse input
    data = read_input()
    print("Input parsed!")
    timer.checkpoint_hit()

    # star 1
    star_1_answer = best_spot_1(data)
    print("Star 1: {}".format(star_1_answer))
    timer.checkpoint_hit()

    # star 2
    timer.checkpoint_hit()

    timer.end_hit()
