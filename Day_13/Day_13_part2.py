def folding(axis: str, grid: list, line: int):
    if axis == "x":
        new_grid = [["."]*line for i in range(len(grid))]
        new_grid_up = [["."]*line for i in range(len(grid))]
        new_grid_down = [["."]*line for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(line):
                if new_grid_up[i][j] != "#":
                    new_grid_up[i][j] = grid[i][j]
            for j in range(1, line + 1):
                if new_grid_down[i][j-1] != "#":
                    new_grid_down[i][j-1] = grid[i][j + line]
        temp = [
            list(reversed(new_grid_down[i])) for i in range(len(new_grid_down))]
        new_grid_down = temp
    if axis == "y":
        new_grid = [["."]*len(grid[0]) for i in range(line)]
        new_grid_up = [["."]*len(grid[0]) for i in range(line)]
        new_grid_down = [["."]*len(grid[0]) for i in range(line)]
        for i in range(len(grid[0])):
            for j in range(line):
                if new_grid_up[j][i] != "#":
                    new_grid_up[j][i] = grid[j][i]
            for j in range(1, line + 1):
                if new_grid_down[j-1][i] != "#":
                    new_grid_down[j-1][i] = grid[j+line][i]
        new_grid_down.reverse()
    for i in range(len(new_grid_down)):
        for j in range(len(new_grid_down[0])):
            if new_grid_down[i][j] == "#":
                new_grid[i][j] = new_grid_down[i][j]
            elif new_grid_up[i][j] == "#":
                new_grid[i][j] = new_grid_up[i][j]
            else:
                new_grid[i][j] = "."
    return new_grid


with open("input.txt", "r") as f:
    fold = False
    foldx = []
    foldy = []
    grid = [["."]*1311 for i in range(895)]
    for i in f:
        if i == "\n":
            fold = True
        if fold:
            curr_fold = i.strip().split("=")
            if curr_fold != [""]:
                if curr_fold[0][-1] == "x":
                    foldx.append(curr_fold[-1])
                else:
                    foldy.append(curr_fold[-1])
        else:
            x, y = i.split(",")
            grid[int(y)][int(x)] = "#"
cnt = 0
while True:
    if len(foldx) > cnt:
        grid = folding("x", grid, int(foldx[cnt]))
    if len(foldy) > cnt:
        grid = folding("y", grid, int(foldy[cnt]))
    if len(foldy) < cnt and len(foldx) < cnt:
        break
    cnt += 1

with open("grid.txt", "w") as f:
    for rows in grid:
        row = ""
        for cell in rows:
            row += cell
        f.write(row + "\n")
print("Answer is in file \"grid.txt\"")
