from aoc_tools import Advent_Timer


DIGITS = {
    "abcefg": "0",
    "cf": "1",
    "acdeg": "2",
    "acdfg": "3",
    "bcdf": "4",
    "abdfg": "5",
    "abdefg": "6",
    "acf": "7",
    "abcdefg": "8",
    "abcdfg": "9"
}



def read_input(filename="input.txt"):
    with open(filename, "r") as file:
        data = [[chars.split() for chars in line.strip().split(" | ")]
                for line in file]
    return data


def star_1(data):
    count = 0
    for screen in data:
        for chars in screen[1]:
            if len(chars) in set([2, 3, 4, 7]):
                count += 1
    return count


def decode_chars(chars_set):
    counts = {}
    known_chars = {}
    for chars in chars_set:
        for char in chars:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1

    # decode chars b, e and f
    for char, count in counts.items():
        if count == 6:
            known_chars[char] = "b"
        if count == 4:
            known_chars[char] = "e"
        if count == 9:
            known_chars[char] = "f"

    # decode char c
    for chars in chars_set:
        if len(chars) == 2:
            for char in chars:
                if char not in known_chars:
                    known_chars[char] = "c"

    # decode chars a and d
    for chars in chars_set:
        if len(chars) == 3:
            for char in chars:
                if char not in known_chars:
                    known_chars[char] = "a"
        if len(chars) == 4:
            for char in chars:
                if char not in known_chars:
                    known_chars[char] = "d"

    for char in "abcdefg":
        if char not in known_chars:
            known_chars[char] = "g"

    return known_chars


def apply_code(code, chars):
    string = "".join(sorted(code[char] for char in chars))
    return DIGITS[string]


def star_2(data):
    total = 0
    for inputs, outputs in data:
        code = decode_chars(inputs)
        str_num = "".join(apply_code(code, chars) for chars in outputs)
        total += int(str_num)
    return total


if __name__ == "__main__":
    timer = Advent_Timer()

    # parse input
    data = read_input()
    print("Input parsed!")
    timer.checkpoint_hit()

    # star 1
    star_1_answer = star_1(data)
    print("Star 1: {}".format(star_1_answer))
    timer.checkpoint_hit()

    # star 2
    star_2_answer = star_2(data)
    print("Star 2: {}".format(star_2_answer))
    timer.checkpoint_hit()

    timer.end_hit()
