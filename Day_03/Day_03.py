from aoc_tools import Advent_Timer
from numpy import array


def read_input(filename="input.txt"):
    with open(filename, "r") as file:
        data = [array([int(char) for char in line.strip()]) for line in file]
        num_length = len(data[0])
    return data, num_length


def bin_array_to_dec(bin_array):
    bin_string = "".join(str(int) for int in bin_array)
    return int(bin_string, 2)


def consumption_vals(data, num_length):
    gamma = [0]*num_length
    epsilon = [0]*num_length

    counts = sum(data)
    half = len(data)//2

    for i in range(num_length):
        more_ones = int(counts[i] > half)
        gamma[i] = more_ones
        epsilon[i] = 1-more_ones

    return bin_array_to_dec(gamma), bin_array_to_dec(epsilon)


if __name__ == "__main__":
    timer = Advent_Timer()

    # parse input
    data, num_length = read_input()
    print("Input parsed!")
    timer.checkpoint_hit()

    # star 1
    gamma, epsilon = consumption_vals(data, num_length)
    print("Star 1: {}".format(gamma*epsilon))
    timer.checkpoint_hit()

    # star 2
    timer.checkpoint_hit()

    timer.end_hit()
