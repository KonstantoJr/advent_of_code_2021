def rotate(l, x):
    x %= len(l)
    if x == 0:
        return l.copy()
    ans = l[x:]+l[0:x]
    return ans


def all_orientations():
    all_signs = [(1, 1, 1), (-1, -1, 1), (-1, 1, -1), (1, -1, -1)]
    prim1 = [(0, 1), (1, 1), (2, 1)]
    prim2 = [(1, 1), (0, 1), (2, -1)]
    all = []
    for i in all_signs:
        for j in range(len(prim1)):
            cur = rotate(prim1, j)
            all.append([(cur[t][0], cur[t][1]*i[t]) for t in range(3)])

    for i in all_signs:
        for j in range(len(prim2)):
            cur = rotate(prim2, j)
            all.append([(cur[t][0], cur[t][1]*i[t]) for t in range(3)])
    # print(all)
    return all


with open("input.txt", "r") as f:
    scanners = []
    cur_scanner = -1
    for row in f:
        row = row.strip()
        if row == "":
            continue
        elif "scanner" in row:
            scanners.append([])
            cur_scanner += 1
        else:
            scanners[cur_scanner].append([int(x) for x in row.split(',')])

total = len(scanners)

pos = [None] * total
pos[0] = (0, 0, 0)
orientations = all_orientations()
done = set([0])
undone = set(range(1, total))
# print(undone)
match = 12

while len(undone) != 0:
    i = done.pop()
    new_done = set()
    for j in undone:
        isdone = False
        for ori in orientations:
            if isdone:
                break
            new_points = []
            for point in scanners[j]:
                # print(scanners[j])
                new_points.append([point[ori[t][0]]*ori[t][1]
                                  for t in range(3)])
            for t0 in scanners[i]:
                if isdone:
                    break
                for t in new_points:
                    x, y, z = [t0[iter]-t[iter] for iter in range(3)]
                    all_points_i = set([tuple(T) for T in scanners[i]])
                    all_points_j = set()
                    for T in new_points:
                        all_points_j.add(tuple([T[0]+x, T[1]+y, T[2]+z]))
                    if len(all_points_j.intersection(all_points_i)) >= match:
                        new_done.add(j)
                        isdone = True
                        pos[j] = (x, y, z)
                        scanners[j] = list(all_points_j)
                        break
    undone -= new_done
    done |= new_done

all_points = set()
for i in scanners:
    for j in i:
        all_points.add(tuple(j))
print(len(all_points))
