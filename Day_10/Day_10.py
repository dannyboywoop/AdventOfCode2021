from aoc_tools import Advent_Timer


OPEN_SYMBOLS = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}
CLOSE_SYMBOLS = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<"
}
SYNTAX_ERRORS = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}
MISSING_ERRORS = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}


def read_input(filename="input.txt"):
    with open(filename, "r") as file:
        data = [line.strip() for line in file]
    return data


def check_if_corrupted(line):
    open_brackets = []
    for char in line:
        if char in OPEN_SYMBOLS:
            open_brackets.append(char)
        elif CLOSE_SYMBOLS[char] != open_brackets.pop():
            return char


def star_1(data):
    corrupted_chars = []
    uncorrupted_lines = []
    for line in data:
        corrupted_char = check_if_corrupted(line)
        if corrupted_char is None:
            uncorrupted_lines.append(line)
        else:
            corrupted_chars.append(corrupted_char)

    score = 0
    for char in corrupted_chars:
        score += SYNTAX_ERRORS[char]

    return score, uncorrupted_lines


def find_remaining_brackets(line):
    open_brackets = []
    for char in line:
        if char in OPEN_SYMBOLS:
            open_brackets.append(char)
        else:
            open_brackets.pop()

    remaining = [OPEN_SYMBOLS[char] for char in reversed(open_brackets)]
    return remaining


def star_2(data):
    points = []
    for line in data:
        total = 0
        for char in find_remaining_brackets(line):
            total *= 5
            total += MISSING_ERRORS[char]
        points.append(total)

    points.sort()
    return points[len(points)//2]


if __name__ == "__main__":
    timer = Advent_Timer()

    # parse input
    data = read_input()
    print("Input parsed!")
    timer.checkpoint_hit()

    # star 1
    star_1_answer, uncorrupted_lines = star_1(data)
    print("Star 1: {}".format(star_1_answer))
    timer.checkpoint_hit()

    # star 2
    star_2_answer = star_2(uncorrupted_lines)
    print("Star 2: {}".format(star_2_answer))
    timer.checkpoint_hit()

    timer.end_hit()
