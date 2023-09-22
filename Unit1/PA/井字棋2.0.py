import random

# 初始化棋盘
board = [" " for _ in range(9)]

# 打印棋盘
def print_board():
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("---------")

# 判断是否有胜者
def check_winner(player):
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

# 玩家下棋
def player_move():
    while True:
        try:
            move = int(input("请选择一个位置(1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == " ":
                board[move] = "X"
                break
            else:
                print("无效的位置，请重新选择。")
        except ValueError:
            print("请输入有效的数字(1-9)。")

# AI下棋
def ai_move():
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            if check_winner("O"):
                return
            board[i] = " "
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            if check_winner("X"):
                board[i] = "O"
                return
            board[i] = " "
    while True:
        move = random.randint(0, 8)
        if board[move] == " ":
            board[move] = "O"
            break

# 主游戏循环
while True:
    print_board()
    player_move()
    if check_winner("X"):
        print_board()
        print("下次我AI1一定会赢的！")
        break
    print_board()
    ai_move()
    if check_winner("O"):
        print_board()
        print("毫无胜算！")
        break
