def find_common(nums: list):
    ones = 12*[0]
    for i in nums:
        tmp = i.strip()
        for cnt, j in enumerate(tmp):
            if int(j) == 1:
                ones[cnt] += 1
    most = ""
    least = ""
    for i in range(12):
        if ones[i] >= len(nums)//2:
            most += "1"
            least += "0"
        else:
            most += "0"
            least += "1"
    return most, least


puzzle_input = "input.txt"
with open(puzzle_input, "r") as file:
    nums = []
    for i in file:
        tmp = i.strip()
        nums.append(tmp)
oxygen = []
co2 = []

most, least = find_common(nums)

oxygen = list(nums)
co2 = list(nums)

for i in range(12):
    if len(oxygen) == 1:
        break
    most, least = find_common(oxygen)
    tmp = []
    for j in oxygen:
        if most[i] == j[i]:
            tmp.append(j)
    oxygen = list(tmp)

for i in range(12):
    if len(co2) == 1:
        break
    most, least = find_common(co2)
    tmp = []
    for j in co2:
        if least[i] == j[i]:
            tmp.append(j)
    co2 = list(tmp)

print(int(oxygen[0], 2), int(co2[0], 2))
print(int(oxygen[0], 2) * int(co2[0], 2))
