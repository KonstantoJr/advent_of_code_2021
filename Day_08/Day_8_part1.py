digits = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdgf",
}


def get_input():
    tmp = []
    with open("input.txt", "r")as file:
        for i in file:
            tmp.append(i.strip().split())
    return tmp


my_in = get_input()
res = 0
for i in my_in:
    for j in range(1, 5):
        if len(i[-j]) == 2 or len(i[-j]) == 4 or len(i[-j]) == 3 or len(i[-j]) == 7:
            res += 1
print(res)
