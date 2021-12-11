def check_bingo(board: list):
    win_row = [1, 1, 1, 1, 1]
    if win_row in board:
        return True
    for col in range(5):
        collumn = []
        for row in range(5):
            if board[row][col] == 1:
                collumn.append(1)
        if collumn == win_row:
            return True
    return False


def calculate_res(marks: list, board: list):
    sum = 0
    for row in range(5):
        for col in range(5):
            if marks[row][col] == 0:
                sum += int(board[row][col])
    return sum


puzzle_input = "input.txt"
with open(puzzle_input, "r") as file:
    draw = [next(file).strip().split(",")]
    boards = []
    for i in file:
        if i != "\n":
            tmp = i.strip().split(" ")
            for i in range(5):
                if "" in tmp:
                    tmp.pop(tmp.index(""))
            boards.append(tmp)
# In boards every boards[i*5:(i+1)*5] has one board
draw_results = {x: [[0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0]] for x in range(int(len(boards)/5))}
draw_wins = [0] * int(len(boards)/5)
last_win = [1] * int(len(boards)/5)
draw = draw[0]
done = False
winning_board = -1
winning_draw = -1
for num in draw:
    for board in range(int(len(boards)/5)):
        for row_n, row in enumerate(boards[board*5:(board+1)*5]):
            for col_n, col in enumerate(row):
                if num == col:
                    draw_results[board][row_n][col_n] = 1
        if check_bingo(draw_results[board]) and not draw_wins[board]:
            draw_wins[board] = 1
            winning_board = board
            winning_draw = num
            if draw_wins == last_win:
                done = True
                break
    if done:
        break


sum = calculate_res(draw_results[winning_board],
                    boards[winning_board*5:(winning_board+1)*5])
print(int(winning_draw) * sum)
