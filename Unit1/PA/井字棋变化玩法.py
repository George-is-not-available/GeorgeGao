import time
import os
import random


# 清屏操作
def clear():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')


# 获取有效下注输入
def get_valid_bet_input(player_name):
    while True:
        try:
            bet = int(input(f"{player_name}, please place a bet: "))
            return bet
        except ValueError:
            print("Error: Invalid input. Please enter a valid number for the bet.")



def get_player_input(current_player):
    invalid_input_count = 0
    while True:
        try:
            move = int(input(f"Player {current_player}, choose a position (1-9) to play: "))
            if 1 <= move <= 9:
                return move - 1  # 调整索引以匹配列表的索引
            else:
                print("\033[94m Oh Dash!\033[35m Please enter a number between 1 to 9.\033[0m")
        except ValueError:
            print("Please enter a number.")
            invalid_input_count += 1
            if invalid_input_count >= 2:
                import time
                print("Wait")



# 获取玩家的输入
def _player_input(current_player, moves, board):
    while True:
        try:
            if len(moves) >= 6:
                removed_move = moves.pop(0)
                board[removed_move] = " "
            move_ = int(input(f"Player {current_player}, choose a position (1-9) to play: "))
            if 1 <= move_ <= 9 and board[move_ - 1] == " ":
                return move_ - 1
            else:
                print("Invalid move. Please enter a number between 1 to 9 in an empty position.")
        except ValueError:
            for fuck in range(1, 10):
                print(".", end='')
                time.sleep(1)
                fuck += 1
                print('\n \033[94mDamn\033[91m What are you Fa*king doing??????\n')
                time.sleep(2)
                print('\033[96m一看就是玩原神玩的,都玩傻了.\n \033[93m')
                time.sleep(2)
                print('Please enter a number between 1 to 9 \033[0m \n ')
                time.sleep(2)
                print('\033[94mDamn it!  \n \033[93mCan\'t you understand what i\'m talking about??? \n ')
                time.sleep(2)
                print('\033[33mI really don\'t know what\'s going on in your head!\n \033[95m')
                time.sleep(2)
                print('Come on, please play by the rules!\033[0m \n')
                time.sleep(3)
        else:
            print("\033[91m"
                "What's problem with you?\033[0m")


# 检查游戏是否结束的逻辑
def check_game_over(board, current_player):
    # 检查游戏是否结束的逻辑
    pass


# 主游戏逻辑
def main():
    print("DownLoading    (Expect to download    170.52MB)")
    for i in range(1, 10):
        print("———", end='')
        time.sleep(1)
        i += 1
    print("\033[93m The game is ready.\033[0m")
    print("\n\033[95m声明：\033[0m")
    print("\033[91m注意请不要在下棋过程中输入字符串或大于9的数字（下赌注除外）！！！\033[0m")
    player1_bet = get_valid_bet_input("Player 1 (X)")
    player2_bet = get_valid_bet_input("Player 2 (O)")

    if player1_bet != player2_bet:
        current_player = "X" if player1_bet > player2_bet else "O"
    else:
        current_player = random.choice(["X", "O"])

    print(f"Player {current_player} starts the game!\n")

    board = [" " for _ in range(9)]
    moves = []

    while True:
        print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n{board[0]} | {board[1]} | {board[2]}\n"
              "——————————\n"
              f"{board[3]} | {board[4]} | {board[5]}\n"
              "——————————\n"
              f"{board[6]} | {board[7]} | {board[8]}\n")

        move = _player_input(current_player, moves, board)
        board[move] = current_player
        moves.append(move)

        # 判断是否有玩家获胜
        for Damn in range(0, 9, 3):
            if board[Damn] == board[Damn + 1] == board[Damn + 2] != " ":
                print(f"\033[93mPlayer {current_player} wins the game!")
                print(f"Congratulations to Player {current_player} for winning {player1_bet + player2_bet} dollars!")
                print("一看就是玩原神玩的（Doge\033[0m")
                exit()
        for cock in range(3):
            if board[cock] == board[cock + 3] == board[cock + 6] != " ":
                print(f"\03393mPlayer {current_player} wins the game!")
                print(f"\03393mCongratulations to Player {current_player} for winning"
                      f" {player1_bet + player2_bet} dollars! \033[0m")
                print("一看就是玩原神玩的（Doge")
                exit()
        if (board[0] == board[4] == board[8] != " ") or (board[2] == board[4] == board[6] != " "):
            print(f"\033[93mPlayer {current_player} wins the game!")
            print(f"\033[93mCongratulations to Player {current_player} for winning "
                  f"{player1_bet + player2_bet} dollars! \033[0m")
            print("一看就是玩原神玩的（Doge")
            exit()
        # 判断是否有平局
        if " " not in board:
            print("\033[91No winner![1m")
            break
        # 检查游戏是否结束
        game_over = check_game_over(board, current_player)
        if game_over:
            print(f"Player {current_player} wins!")
            break

        current_player = "X" if current_player == "O" else "O"


if __name__ == "__main__":
    main()
