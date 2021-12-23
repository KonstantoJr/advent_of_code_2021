def create_cube():
    pass


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

for i in range(20):
    print(regions[i])
