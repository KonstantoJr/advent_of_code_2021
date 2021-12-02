with open("Day_1/input.txt", "r") as file:
    cnt = 0
    increase = 0
    nums = []
    A = []
    B = []
    for i in file:
        cnt += 1
        if cnt == 4:
            B.append(int(i))
            if sum(A) < sum(B):
                increase += 1
            A = list(B)
            B.pop(0)
            cnt = 3
        elif cnt == 1:
            A.append(int(i))
        elif cnt == 2 or cnt == 3:
            A.append(int(i))
            B.append(int(i))

print(increase)
