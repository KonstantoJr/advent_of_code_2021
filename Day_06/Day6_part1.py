# 1 Lanterfish makes 1 new lanterfish every 7 days
# The process is not necessarily synchronized
puzzle_input = "input.txt"
with open(puzzle_input, "r") as file:
    initial_state = next(file).strip().split(",")

# Make str to int
for i in range(len(initial_state)):
    initial_state[i] = int(initial_state[i])

days = 80

for day in range(days):
    current_population = len(initial_state)
    for i in range(current_population):
        if initial_state[i] == 0:
            initial_state[i] = 6
            initial_state.append(8)
        else:
            initial_state[i] += -1

print(len(initial_state))
