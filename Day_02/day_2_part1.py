puzzle_input = "input.txt"
moves = {
    "forward": 0,
    "down": 0,
    "up": 0
}
with open(puzzle_input, "r") as movement:
    for move in movement:
        cur = move.split(" ")
        moves[cur[0]] += int(cur[1])
    horizontal = moves["forward"]
    depth = moves["down"] - moves["up"]
print(horizontal, depth)
res = horizontal * depth
print(res)
