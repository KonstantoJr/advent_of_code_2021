import math
with open("input.txt", "r") as f:
    temp = f.read()
    temp = temp.strip().split("=")
    x = temp[1].split("..")
    x1, x2 = int(x[0]), int(x[1].split(",")[0])
    y = temp[2].split("..")
    y1, y2 = int(y[0]), int(y[1])

#print(x1, x2)
#print(y1, y2)

start_x, start_y = 0, 0
on_target = []
for i in range(x2):
    for j in range(y1, x2):
        done = False
        cur_y_max = -math.inf
        start_x, start_y = i, j
        cur_x, cur_y = 0, 0
        while not done:
            cur_x += start_x
            cur_y += start_y
            if cur_x >= x1 and cur_x <= x2:
                if cur_y >= y1 and cur_y <= y2:
                    on_target.append((i, j, cur_y_max))
                    done = True
            if cur_x > x2 or cur_y < y1:
                done = True
            cur_y_max = max(cur_y, cur_y_max)
            if start_x > 0:
                start_x -= 1
            elif start_x < 0:
                start_x += 1
            start_y -= 1

maxy = sorted(on_target, key=lambda x: x[2], reverse=True)
print(maxy[0])
