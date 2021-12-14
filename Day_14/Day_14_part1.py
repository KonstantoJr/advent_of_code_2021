import math
with open("input.txt", "r") as f:
    initial_seq = f.readline().strip()
    polymer_template = dict()
    for i in f:
        if i != "\n":
            key, value = i.strip().split("->")
            polymer_template[key.strip()] = value.strip()


for i in range(10):
    new_seq = [initial_seq[0]]
    for j in range(len(initial_seq)-1):
        key = initial_seq[j] + initial_seq[j+1]
        new_seq.append(polymer_template[key])
        new_seq.append(initial_seq[j+1])
    initial_seq = "".join(new_seq)
elements = dict()
letters = []
for i in range(len(initial_seq)):
    if initial_seq[i] in elements:
        elements[initial_seq[i]] += 1
    else:
        elements[initial_seq[i]] = 1
most_common = 0
least_common = math.inf

for i in elements:
    most_common = max(most_common, elements[i])
    least_common = min(least_common, elements[i])

print(most_common - least_common)
