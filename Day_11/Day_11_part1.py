grid = []
with open("input.txt", "r") as f:
    for line in f:
        grid.append(list(line.strip()))
for i in range(len(grid)):
    for j in range(len(grid)):
        grid[i][j] = int(grid[i][j])


flashed = []


def neighbors(rowNumber, colNumber):
    result = []
    for rowAdd in range(-1, 2):
        newRow = rowNumber + rowAdd
        if newRow >= 0 and newRow <= len(grid)-1:
            for colAdd in range(-1, 2):
                newCol = colNumber + colAdd
                if newCol >= 0 and newCol <= len(grid)-1:
                    if newCol == colNumber and newRow == rowNumber:
                        continue
                    result.append((newRow, newCol))
    return result


squids_flashed = 0


def flash(row, col):
    global flashed
    this_neighbors = neighbors(row, col)
    for new_row, new_col in this_neighbors:
        if (new_row, new_col) not in flashed:
            grid[new_row][new_col] += 1
            if grid[new_row][new_col] > 9:
                flashed.append((new_row, new_col))
                flash(new_row, new_col)


for i in range(100):
    flashed = []
    for row in range(len(grid)):
        for col in range(len(grid)):
            grid[row][col] += 1

    for row in range(len(grid)):
        for col in range(len(grid)):
            if (row, col) not in flashed:
                if grid[row][col] > 9:
                    flashed.append((row, col))
                    flash(row, col)
    for row in range(len(grid)):
        for col in range(len(grid)):
            if grid[row][col] > 9:
                squids_flashed += 1
                grid[row][col] = 0


print(squids_flashed)
for i in grid:
    print(i)
