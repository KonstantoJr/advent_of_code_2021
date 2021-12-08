def movement(start, stop):
    to_move = list(range(1, abs(start-stop)+1))
    return sum(to_move)


def today_input():
    puzzle_input = "input.txt"

    with open(puzzle_input, "r") as file:
        pos = next(file).strip().split(",")

    tmp = map(int, pos)
    pos = list(tmp)
    return pos


pos = today_input()
min_fuel = 10**10
for i in range(max(pos)):
    stop = i
    fuel = 0
    for j in range(len(pos)):
        fuel += movement(pos[j], stop)
    min_fuel = min(fuel, min_fuel)
print(min_fuel)
