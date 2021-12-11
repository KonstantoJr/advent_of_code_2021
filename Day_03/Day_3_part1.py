puzzle_input = "input.txt"
with open(puzzle_input, "r") as file:
    ones = 12*[0]
    for i in file:
        tmp = i.strip()
        for cnt, j in enumerate(tmp):
            if int(j) == 1:
                ones[cnt] += 1
gamma = ""
epsilon = ""
print(ones)
for i in ones:
    if i > 500:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

print(int(gamma), int(epsilon))
print(int(gamma, 2) * int(epsilon, 2))
