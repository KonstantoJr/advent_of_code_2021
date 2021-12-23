def check_dice(dice):
    if dice == 101:
        return 1
    else:
        return dice


def check_position(pos):
    if pos % 10 == 0:
        return 10
    else:
        return pos % 10


with open("input.txt", "r") as f:
    p1 = int(f.readline().strip().split(":")[1])
    p2 = int(f.readline().strip().split(":")[1])


dice_rolled = 0
p1_score = 0
p2_score = 0
dice_value = 1
while True:
    dice_rolled += 3
    for i in range(3):
        p1 += dice_value
        dice_value += 1
        dice_value = check_dice(dice_value)
    p1 = check_position(p1)
    p1_score += p1
    if p1_score >= 1000:
        break
    dice_rolled += 3
    for i in range(3):
        p2 += dice_value
        dice_value += 1
        dice_value = check_dice(dice_value)

    p2 = check_position(p2)
    p2_score += p2
    if p2_score >= 1000:
        break
print(p1_score, p2_score)
print(min(p1_score, p2_score) * dice_rolled)
