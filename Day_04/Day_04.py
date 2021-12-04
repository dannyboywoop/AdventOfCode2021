from aoc_tools import Advent_Timer


class BingoCard:
    def __init__(self, card_string):
        self.grid = [row.split() for row in card_string.split("\n")]
        self.create_map()

    def create_map(self):
        self.map = {}

        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                self.map[self.grid[i][j]] = [i, j, False]

    def mark_card(self, num):
        if num in self.map:
            self.map[num][2] = True
            return self.check_for_win(*self.map[num])
        else:
            return False

    def check_for_win(self, row, col, *args):
        # check row
        row_win = True
        for j in range(len(self.grid[row])):
            row_win &= self.map[self.grid[row][j]][2]

        # check col
        col_win = True
        for i in range(len(self.grid)):
            col_win &= self.map[self.grid[i][col]][2]
        
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


def star_1(sequence, cards):
    winning_card, winning_num = find_winning_card(sequence, cards)
    
    total = 0
    for num, val in winning_card.map.items():
        if not val[2]:
            total += int(num)
    
    return total * int(winning_num)


if __name__ == "__main__":
    timer = Advent_Timer()

    # parse input
    sequence, cards = read_input()
    print("Input parsed!")
    timer.checkpoint_hit()

    # star 1
    star_1_answer = star_1(sequence, cards)
    print("Star_1: {}".format(star_1_answer))
    timer.checkpoint_hit()

    # star 2
    timer.checkpoint_hit()

    timer.end_hit()
