puzzle_input = "input.txt"
aim = 0
horizontal = 0
depth = 0
with open(puzzle_input, "r") as movement:
    for move in movement:
        cur = move.split(" ")
        if cur[0] == "down":
            aim += int(cur[1])
        elif cur[0] == "up":
            aim -= int(cur[1])
        else:
            horizontal += int(cur[1])
            depth += aim * int(cur[1])
res = horizontal * depth
print(horizontal, depth)
print(res)
