def calculate(grid: dict):
    overlap = 0
    for i in range(1000):
        for j in range(1000):
            if grid[i][j] >= 2:
                overlap += 1
    return overlap


puzzle_input = "input.txt"
with open(puzzle_input, "r") as file:
    row = [0]*1000
    grid = {x: list(row) for x in range(1000)}
    for i in file:
        nums = i.strip().split(",")
        y1, x2 = nums[1].split(" -> ")
        x1, y2 = nums[0], nums[-1]
        if int(x1) == int(x2):
            if int(y1) - int(y2) < 0:
                offset = 1
            else:
                offset = -1
            for j in range(int(y1), int(y2)+offset, offset):
                grid[j][int(x1)] += 1
        elif int(y1) == int(y2):
            if int(x1) - int(x2) < 0:
                offset = 1
            else:
                offset = -1
            for j in range(int(x1), int(x2)+offset, offset):
                grid[int(y1)][j] += 1

res = calculate(grid)
print(res)
