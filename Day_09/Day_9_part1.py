grid = []
with open("input.txt", "r") as file:
    for i in file:
        tmp = []
        i = i.strip()
        for j in i:
            tmp.append(int(j))
        grid.append(tmp)


max_y = len(grid)
max_x = len(grid[0])
low_points = {}
for x in range(max_x):
    for y in range(max_y):
        is_lower = True
        # Check X
        cur = grid[y][x]
        if x > 0 and x < max_x-1:
            if grid[y][x] >= grid[y][x+1]:
                is_lower = False
            if grid[y][x] >= grid[y][x-1]:
                is_lower = False
        elif x == 0:
            if grid[y][x] >= grid[y][x+1]:
                is_lower = False
        elif x == max_x - 1:
            if grid[y][x] >= grid[y][x-1]:
                is_lower = False
        # Check Y
        if y > 0 and y < max_y - 1:
            if grid[y][x] >= grid[y+1][x]:
                is_lower = False
            if grid[y][x] >= grid[y-1][x]:
                is_lower = False
        elif y == 0:
            if grid[y][x] >= grid[y+1][x]:
                is_lower = False
        elif y == max_y - 1:
            if grid[y][x] >= grid[y-1][x]:
                is_lower = False
        if is_lower:
            low_points[(y, x)] = grid[y][x]


res = 0
for i in low_points.keys():
    res += int(low_points[i]) + 1
print(res)
