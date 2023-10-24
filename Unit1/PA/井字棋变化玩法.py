import time
import os
import random
# 系统清屏操作
def clear():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')
moves = []
def get_valid_bet_input(player_name):
    while True:
        try:
            bet = int(input(f"{player_name}, please place a bet: "))
            return bet
        except ValueError:
            print("\033[91mError Invalid input. \033[95mPlease enter a valid number for the bet.\033[0m")

def get_player_input(current_player, moves, board, move_count):
    while True:
        try:
            if move_count >= 7:
                removed_move = moves.pop(0)
                board[removed_move] = " "  # 清除第一个棋子
            move_ = int(input(f"Player {current_player}, choose a position (1-9) to play: "))
            if 1 <= move_ <= 9:
                return move_ - 1  # 调整索引以匹配列表的索引
            else:
                print("Oh Dash! Please enter a number between 1 to 9.")
        except ValueError:
            print("\n loading")
            for damn in range(1, 7):
                print(".", end='')
                time.sleep(1)
                damn += 1
            print('\n \033[94mDamn\033[91m What are you Fa*king doing??????\n')
            time.sleep(2)
            print('\033[96m一看就是玩原神玩的,都玩傻了.\n \033[93m')
            time.sleep(2)
            print('Please enter a number between 1 to 9 \033[0m \n ')
            time.sleep(1)
            print('\033[94mDamn it!')
            time.sleep(2)
            print('\n\033[93mCan\'t you understand what i\'m talking about??? \n ')
            time.sleep(2)
            print('\033[33mI really don\'t know what\'s going on in your head!\n \033[95m')
            time.sleep(2)
            print("\033[95mCome on, please play by the rules!\033[0m \n")
        else:
            print("\033[91m"
                  "What's problem with you?\033[0m")
            move_count += 1  # 更新移动计数

def main():
    print("DownLoading    (Expect to download    170.52MB)")
    for i in range(1, 20):
        print("———", end='')
        time.sleep(1)
        i += 1
    print("\n \033[93m The game is ready.\033[0m")
    time.sleep(5)
    os.system('cls' if os.name == 'nt' else 'clear')  # 清屏

    player1_ = get_valid_bet_input("Player 1(x)")
    player2_ = get_valid_bet_input("Player 2(o)")

    if player1_ != player2_:
        current_player = "X" if player1_ > player2_ else "O"
    else:
        current_player = random.choice(["X", "O"])

    print(f"Player {current_player} starts the game!")

    board = [" " for _ in range(9)]
    move_count = 0  # 初始化移动计数
    moves = []  # 初始化 moves 列表

    while True:
        print(f"{board[0]} | {board[1]} | {board[2]}")
        print("—————————")
        print(f"{board[3]} | {board[4]} | {board[5]}")
        print("—————————")
        print(f"{board[6]} | {board[7]} | {board[8]}")

        move = get_player_input(current_player, moves, board, move_count)

        if board[move] == " ":
            board[move] = current_player
            move_count += 1  # 更新移动计数
        else:
            print("Invalid move. That position is already occupied. Try again.")

        # ... 检查胜利和平局的代码 ...

        current_player = "X" if current_player == "O" else "O"

if __name__ == "__main__":
    main()
