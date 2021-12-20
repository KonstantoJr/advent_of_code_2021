def find_new_pixel(num, algo):
    index = int(num, 2)
    return algo[index]


def find_neighbours(y, x):
    neighbours = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1), (0, 0), (0, 1),
                  (1, -1), (1, 0), (1, 1)]
    for i in range(len(neighbours)):
        neighbours[i] = neighbours[i][0] + y, neighbours[i][1] + x
    return neighbours


def add_margin(grid, margin, default):
    if default:
        wall = "."
    else:
        wall = "#"
    row = [wall * len(grid[0])]
    grid = margin * row + grid + margin * row
    for i in range(len(grid)):
        grid[i] = margin*wall + grid[i] + margin*wall
    return grid


def print_image(grid):
    for i in grid:
        print(i)
    print()


with open("input.txt", "r") as f:
    algorithm = f.readline().strip()
    grid = []
    for i in f:
        if i == "\n":
            continue
        else:
            grid.append(i.strip())


for _ in range(2):
    grid = add_margin(grid, 1, _ % 2 == 0)
    print("Step:", _)
    # print_image(grid)
    new_image = [""] * len(grid)
    for row in range(len(grid)):
        for pixel in range(len(grid[row])):
            neighbours = find_neighbours(row, pixel)
            output = ""
            for y, x in neighbours:
                if (y < 0 or y > len(grid)-1) or (x < 0 or x > len(grid[row])-1):
                    if (_ % 2) == 0:
                        output += "0"
                    else:
                        output += "1"
                else:
                    if grid[y][x] == "#":
                        output += "1"
                    else:
                        output += "0"
            new_image[row] += find_new_pixel(output, algorithm)
    grid = list(new_image)
# print_image(grid)
pixels = 0
for row in grid:
    for pixel in row:
        if pixel == "#":
            pixels += 1

print(pixels)
