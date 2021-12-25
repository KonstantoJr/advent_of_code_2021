def create_cube(xcoords, ycoords, zcoords):
    cubes = set()
    # print(xcoords)
    for x in range(xcoords[0], xcoords[1]+1):
        for y in range(ycoords[0], ycoords[1]+1):
            for z in range(zcoords[0], zcoords[1]+1):
                cubes.add((x, y, z))
    return cubes


with open("input.txt", "r") as f:
    temp = []
    for i in f:
        temp.append(i.strip())


regions = []
for j in temp:
    mode = True if j.split()[0] == "on" else False
    j = j.split()[1:]
    j = "".join(j)
    j = j.split(",")
    t = []
    for i in j:
        x, y = int(i.split("=")[1].split("..")[0]), int(
            i.split("=")[1].split("..")[1])
        t.append((x, y))
    regions.append([mode, t])

on_cubes = set()
for i in range(20):
    # print(regions[i])
    cubes = create_cube(regions[i][1][0], regions[i][1][1], regions[i][1][2])
    if regions[i][0]:
        on_cubes = on_cubes.union(cubes)
    else:
        on_cubes = on_cubes.difference(cubes)

print(len(on_cubes))
