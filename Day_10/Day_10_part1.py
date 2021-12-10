inp = []
illegal_points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}
with open("input.txt", "r") as f:
    for i in f:
        tmp = i.strip()
        inp.append(tmp)
corrupted_line = []
for i in inp:
    opening_stack = []
    for j in i:
        if j not in [")", "]", "}", ">"]:
            opening_stack.append(j)
        elif j == ")" and opening_stack.pop() == "(":
            continue
        elif j == "]" and opening_stack.pop() == "[":
            continue
        elif j == "}" and opening_stack.pop() == "{":
            continue
        elif j == ">" and opening_stack.pop() == "<":
            continue
        else:
            corrupted_line.append(j)
            break

illegal_chars = {
    ")": 0,
    "]": 0,
    "}": 0,
    ">": 0
}

for i in corrupted_line:
    illegal_chars[i] += 1
res = [0, 0, 0, 0]
for cnt, key in enumerate(illegal_chars.keys()):
    res[cnt] = illegal_chars[key] * illegal_points[key]
print(sum(res))
