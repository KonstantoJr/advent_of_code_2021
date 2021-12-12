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


paths = [(['start'], True)]
completepaths = []

while paths:
    path, flag = paths.pop()
    finalcave = path[-1]
    neighbors = cave_system[finalcave]
    for cave in neighbors:
        if cave == 'end':
            completepaths.append((path+[cave], flag))
        elif cave == 'start':
            continue
        elif (cave.isupper()) or (cave not in path):
            paths.append((path+[cave], flag))
        elif flag:
            paths.append((path+[cave], False))

print(len(completepaths))
