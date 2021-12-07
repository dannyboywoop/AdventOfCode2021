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


def sum_natural_numbers(x):
    return (x + 1) * x // 2


def fuel_cost_2(data, point):
    total = 0
    for x in data:
        total += sum_natural_numbers(abs(point-x))
    return total


def best_spot_2(data):
    x = sum(data) // len(data)
    x_fuel = fuel_cost_2(data, x)
    min_found = False

    while not min_found:
        right_pos_fuel = fuel_cost_2(data, x + 1)
        if right_pos_fuel < x_fuel:
            x += 1
            x_fuel = right_pos_fuel
            continue

        left_pos_fuel = fuel_cost_2(data, x - 1)
        if left_pos_fuel < x_fuel:
            x -= 1
            x_fuel = left_pos_fuel
            continue

        break
    return x_fuel


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
    star_1_answer = best_spot_2(data)
    print("Star 1: {}".format(star_1_answer))
    timer.checkpoint_hit()

    timer.end_hit()
