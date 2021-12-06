from aoc_tools import Advent_Timer


NEW_FISH_GESTATION = 9
OLD_FISH_GESTATION = 7


def read_input(filename="input.txt"):
    with open(filename, "r") as file:
        data = [int(x) for x in file.read().split(",")]
    return data


def evolve(system):
    birthing_fish = system[0]

    # decrease remaining days for each fish
    for i in range(1, NEW_FISH_GESTATION):
        system[i-1] = system[i]

    # add new babies
    system[NEW_FISH_GESTATION-1] = birthing_fish

    # reset new mothers
    system[OLD_FISH_GESTATION-1] += birthing_fish


def fish_after_n_steps(fish, n):
    system = [0] * NEW_FISH_GESTATION

    # initialise system
    for f in fish:
        system[f] += 1

    # evolve system
    for _ in range(n):
        evolve(system)

    # count fish
    return sum(system)


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
