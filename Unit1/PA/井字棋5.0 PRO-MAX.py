# 初始化游戏状态：1
import random
i = 0
# 赌注设置（谁下的多谁先开始）：
player1_ = int(input("玩家1，请下赌注："))
# （玩家赌注）设置变量 ↑
player2_ = int(input("玩家2，请下赌注："))
# （玩家赌注）设置变量 ↑

# 决定先手（谁下的赌注最多谁开始）
if player1_ > player2_:             # 2个变量做对比
    current_player = "1"
elif player2_ > player1_:           # 2个变量做对比
    current_player = "2"
else:
    current_player = random.choice(["1", "2"])
print(f"{current_player} 先手开始游戏！")
# 初始化游戏棋盘
board = [" " for _ in range(9)]
# 游戏主循环
while True:
    # 打印当前棋盘
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("——————————————————————")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("——————————————————————")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    # 玩家输入位置
    move = int(input(f"{current_player}，请选择一个位置 (1-9) 下棋："))
    # 检查是否有冲突的位置
    if move < 0 or move > 8 or board[move] != " ":
        print("无效的位置，请重新选择。")
        continue
    # 在棋盘上下棋
    board[move] = current_player

    # 检查是否有玩家连成3位数
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] != " ":
            print(f"玩家{current_player} 赢得了比赛！")
            print(f"恭喜玩家{current_player} 获得 {player1_ + player2_}块钱！")
            exit()
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] != " ":
            print(f"玩家{current_player} 赢得了比赛！一看这位就是玩原神玩的（bu shi")
            print(f"{current_player} 获得 {player1_ + player2_}块钱！")
            exit()
    if (board[0] == board[4] == board[8] != " ") or (board[2] == board[4] == board[6] != " "):
        print(f"玩家{current_player} 赢得了比赛！一看这位就是玩原神玩的（bu shi")
        print(f"{current_player} 获得 {player1_ + player2_}块钱！")
        exit()
    # 开始后切换玩家下棋
    if current_player == "1":
        current_player = "2"
    else:
        current_player = "1"
