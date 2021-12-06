from aoc_tools import Advent_Timer


def read_input(filename="input.txt"):
    with open(filename, "r") as file:
        data = [int(x) for x in file.read().split(",")]
    return data


def evolve(system):
    temp = system[0]
    for i in range(1, 9):
        system[i-1] = system[i]
    system[6] += temp
    system[8] = temp


def fish_after_n_steps(fish, n):
    system = {x: 0 for x in range(9)}

    # initialise system
    for f in fish:
        system[f] += 1

    # evolve system
    for _ in range(n):
        evolve(system)

    # count fish
    return sum(list(system.values()))


if __name__ == "__main__":
    timer = Advent_Timer()

    # parse input
    data = read_input()
    print("Input parsed!")
    timer.checkpoint_hit()

    # star 1
    star_1_answer = fish_after_n_steps(data, 80)
    print("Star 1: {}".format(star_1_answer))
    timer.checkpoint_hit()

    # star 2
    star_2_answer = fish_after_n_steps(data, 256)
    print("Star 2: {}".format(star_2_answer))
    timer.checkpoint_hit()

    timer.end_hit()
