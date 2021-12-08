def get_input():
    tmp = []
    with open("input.txt", "r")as file:
        for i in file:
            tmp.append(i.strip().split())
    return tmp


digits = {
    "abcefg": "0",
    #
    "cf": "1",
    "acdeg": "2",
    "acdfg": "3",
    #
    "bcdf": "4",
    "abdfg": "5",
    "abdefg": "6",
    #
    "acf": "7",
    #
    "abcdefg": "8",
    "abcdfg": "9"
}

my_in = get_input()
common_config = ["a", "b", "c", "d", "e", "f", "g"]
res = 0
for i in my_in:
    cur_config = ["-" for x in range(7)]
    five_len = []
    six_len = []
    for j in range(10):
        if len(i[j]) == 7:
            eight = i[j]
        if len(i[j]) == 2:
            one = i[j]
        if len(i[j]) == 4:
            four = i[j]
        if len(i[j]) == 3:
            seven = i[j]
        if len(i[j]) == 5:
            five_len.append(i[j])
        if len(i[j]) == 6:
            six_len.append(i[j])
    bd = []
    cf = [one[0], one[1]]
    for letter in four:
        if letter not in one:
            bd.append(letter)
    for letter in seven:
        if letter not in one:
            a = letter
    eg = []
    for letter in eight:
        if letter not in bd and letter not in cf and letter not in a:
            eg.append(letter)
    cnt = 0
    for j in range(3):
        if bd[0] in five_len[j]:
            cnt += 1
    if cnt == 3:
        d = bd[0]
        b = bd[1]
    else:
        d = bd[1]
        b = bd[0]
    cnt = 0
    for j in range(3):
        if cf[0] in six_len[j]:
            cnt += 1
    if cnt == 3:
        f = cf[0]
        c = cf[1]
    else:
        f = cf[1]
        c = cf[0]
    cnt = 0
    for j in range(3):
        if eg[0] in five_len[j]:
            cnt += 1
    if cnt == 3:
        g = eg[0]
        e = eg[1]
    else:
        g = eg[1]
        e = eg[0]
    cur_config = [a, b, c, d, e, f, g]
    cur_digits = ""
    for j in range(4, 0, -1):
        tmp = []
        for letter in i[-j]:
            ind = cur_config.index(letter)
            tmp.append(common_config[ind])
        tmp.sort()
        tmp = "".join(tmp)
        cur_digits += digits[tmp]
    res += int(cur_digits)
print(res)
