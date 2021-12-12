cave_system = dict()
with open("input.txt", "r") as f:
    for line in f.readlines():
        a, b = line.strip().split('-')
        if a not in cave_system:
            cave_system[a] = []
        if b not in cave_system:
            cave_system[b] = []
        cave_system[a] += [b]
        cave_system[b] += [a]


paths = [['start']]
completepaths = []

while paths:
    path = paths.pop()
    finalcave = path[-1]
    neighbors = cave_system[finalcave]
    for cave in neighbors:
        if cave == 'end':
            completepaths.append(path+[cave])
        elif (cave.isupper()) or (cave not in path):
            paths.append(path+[cave])

print(len(completepaths))
