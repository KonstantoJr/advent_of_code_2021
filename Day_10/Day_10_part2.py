inp = []
illegal_points = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4
}
with open("input.txt", "r") as f:
    for i in f:
        tmp = i.strip()
        inp.append(tmp)
corrupted_line = []
incomplete = []
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
    else:
        if len(opening_stack) > 0:
            incomplete.append(opening_stack)

print(len(incomplete))
results = []
for i in incomplete:
    i.reverse()
    res = 0
    for j in i:
        res *= 5
        res += illegal_points[j]
    results.append(res)
results.sort()
print(results[int((len(results) - 1) / 2)])
