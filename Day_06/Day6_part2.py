# 1 Lanterfish makes 1 new lanterfish every 7 days
# The process is not necessarily synchronized

puzzle_input = "input.txt"
with open(puzzle_input, "r") as file:
    initial_state = next(file).strip().split(",")

tmp = map(int, initial_state)
initial_state = list(tmp)

fish_counters = [0] * 9

for i in initial_state:
    fish_counters[i] += 1

days = 256

for day in range(days):
    for i in range(len(fish_counters) - 1):
        cur = fish_counters[i]
        fish_counters[i] = fish_counters[i+1]
        if i == 0:
            born = cur
    fish_counters[8] = born
    fish_counters[6] += born

res = sum(fish_counters)
print(res)
