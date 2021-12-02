with open("Day_1/input.txt", "r") as file:
    increase = -1
    prev = -1
    for i in file:
        if int(i) > prev:
            increase += 1
        prev = int(i)
print(increase)
