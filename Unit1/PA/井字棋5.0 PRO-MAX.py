
# 初始化游戏状态：
import random




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
qipan = [" " for _ in range(9)]
# 游戏主循环
while True:
    # 打印当前棋盘
    print(f"{qipan[0]} | {qipan[1]} | {qipan[2]}")
    print("---------")
    print(f"{qipan[3]} | {qipan[4]} | {qipan[5]}")
    print("---------")
    print(f"{qipan[6]} | {qipan[7]} | {qipan[8]}")
    # 玩家输入位置
    move = int(input(f"{current_player}，请选择一个位置 (1-9) 下棋：")) - 1
    # 检查是否有冲突的位置
    if move < 0 or move > 8 or qipan[move] != " ":
        print("无效的位置，请重新选择。")
        continue
    # 在棋盘上下棋
    qipan[move] = current_player

    # 检查是否有玩家连成3位数
    for i in range(0, 9, 3):
        if qipan[i] == qipan[i + 1] == qipan[i + 2] != " ":
            print(f"玩家{current_player} 赢得了比赛！")
            print(f"恭喜玩家{current_player} 获得 {player1_ + player2_}块钱！")
            exit()
    for i in range(3):
        if qipan[i] == qipan[i + 3] == qipan[i + 6] != " ":
            print(f"玩家{current_player} 赢得了比赛！")
            print(f"恭喜玩家{current_player} 获得 {player1_ + player2_}块钱！")
            exit()
    if (qipan[0] == qipan[4] == qipan[8] != " ") or (qipan[2] == qipan[4] == qipan[6] != " "):
        print(f"玩家{current_player} 赢得了比赛！")
        print(f"恭喜玩家{current_player} 获得 {player1_ + player2_}块钱！")
        exit()
    # 切换玩家
    if current_player == "1":
        current_player = "2"
    else:
        current_player = "1"
