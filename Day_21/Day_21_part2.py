from itertools import combinations


def check_position(pos):
    if pos % 10 == 0:
        return 10
    else:
        return pos % 10


def game(p1, p1_score, p2, p2_score, roll, who):
    if p1_score >= 21:
        return "p1"
    if p2_score >= 21:
        return "p2"
    if not who:
        for dice in roll:
            p1 += dice
        p1 = check_position(p1)
        p1_score += p1
    else:
        for dice in roll:
            p2 += dice
        p2 = check_position(p2)
        p2_score += p2


with open("input.txt", "r") as f:
    p1 = int(f.readline().strip().split(":")[1])
    p2 = int(f.readline().strip().split(":")[1])

p1_wins, p2_wins = 0, 0

possible_rolls = list(combinations((1, 2, 3, 1, 2, 3, 1, 2, 3), 3))
