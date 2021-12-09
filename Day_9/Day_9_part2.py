from functools import reduce
from operator import mul


def get_neighbors(x, y, grid):
    neighbors = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    vals = []
    for dx, dy in neighbors:
        nx, ny = x+dx, y+dy
        if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
            vals.append((nx, ny))
    return vals


def bfs(x, y, grid, visited):
    visited.add((x, y))
    for nx, ny in set(get_neighbors(x, y, grid)) - visited:
        if grid[ny][nx] == 9:
            continue
        visited.add((nx, ny))
        visited |= bfs(nx, ny, grid, visited)
    return visited


grid = []
with open("input.txt", "r") as file:
    for i in file:
        tmp = []
        i = i.strip()
        for j in i:
            tmp.append(int(j))
        grid.append(tmp)


visited = set()
basins = set()

for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == 9 or (x, y) in visited:
            continue
        basin = bfs(x, y, grid, set())
        visited |= basin
        basins.add(tuple(sorted(basin)))

print(reduce(mul, sorted([len(x) for x in basins])[::-1][:3]))
