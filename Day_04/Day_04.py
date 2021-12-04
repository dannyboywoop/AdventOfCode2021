from aoc_tools import Advent_Timer


class BingoCard:
    class Spot:
        def __init__(self, row, col, marked=False):
            self.row = row
            self.col = col
            self.marked = marked

        def mark(self):
            self.marked = True

    def __init__(self, card_string):
        self.grid = [row.split() for row in card_string.split("\n")]
        self.create_map()

    def create_map(self):
        self.map = {}

        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                self.map[self.grid[i][j]] = self.Spot(i, j)

    def mark_card(self, num):
        if num in self.map:
            self.map[num].mark()
            return self.check_for_win(self.map[num])
        else:
            return False

    def check_for_win(self, spot):
        # check row
        row_win = True
        for j in range(len(self.grid[spot.row])):
            row_win &= self.map[self.grid[spot.row][j]].marked

        # check col
        col_win = True
        for i in range(len(self.grid)):
            col_win &= self.map[self.grid[i][spot.col]].marked

        return row_win or col_win


def read_input(filename="input.txt"):
    with open(filename, "r") as file:
        sequence = file.readline().strip().split(",")
        card_strings = file.read().strip().split("\n\n")
        cards = [BingoCard(card_string) for card_string in card_strings]
    return sequence, cards


def find_winning_card(sequence, cards):
    for num in sequence:
        winner = None
        for card in cards:
            if card.mark_card(num):
                winner = (card, num)
                break
        if winner is not None:
            break
    return winner


def calculate_score(winning_card, winning_num):
    total = 0
    for num, spot in winning_card.map.items():
        if not spot.marked:
            total += int(num)

    return total * int(winning_num)


def find_losing_card(sequence, cards):
    remaining_cards = set(range(len(cards)))

    # perform sequence
    for num in sequence:
        winning_card_nums = []

        # mark remaining cards
        for card_num in remaining_cards:
            if cards[card_num].mark_card(num):
                winning_card_nums.append(card_num)

        # discard cards that have won
        for card_num in winning_card_nums:
            remaining_cards.remove(card_num)

        # if this was the last card to win, return
        if len(remaining_cards) == 0:
            return cards[winning_card_nums[0]], num


if __name__ == "__main__":
    timer = Advent_Timer()

    # parse input
    sequence, cards = read_input()
    print("Input parsed!")
    timer.checkpoint_hit()

    # star 1
    winning_card, winning_num = find_winning_card(sequence, cards)
    star_1_answer = calculate_score(winning_card, winning_num)
    print("Star_1: {}".format(star_1_answer))
    timer.checkpoint_hit()

    # star 2
    remaining_sequence = sequence[sequence.index(winning_num)::]
    losing_card, losing_num = find_losing_card(remaining_sequence, cards)
    star_2_answer = calculate_score(losing_card, winning_num)
    print("Star_2: {}".format(star_2_answer))
    timer.checkpoint_hit()

    timer.end_hit()
