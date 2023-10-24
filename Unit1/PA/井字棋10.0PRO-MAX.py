import random
import time

print("DownLoading    (Expect to download    170.52MB)")
for i in range(1, 10):
    print("———", end='')
    time.sleep(1)
    i += 1
print("\033[93m The game is ready.\033[0m")


def get_valid_bet_input(player_name):
    while True:
        try:
            bet = int(input(f"{player_name}, please place a bet: "))
            return bet
        except ValueError:
            print("\033[91mError Invalid input. \033[95mPlease enter a valid number for the bet.\033[0m")


def main():
    player1_ = get_valid_bet_input("Player 1(x)")
    player2_ = get_valid_bet_input("Player 2(o)")

    if player1_ != player2_:
        current_player = "X" if player1_ > player2_ else "O"
    else:
        current_player = random.choice(["X", "O"])

    print(f"Player {current_player} starts the game!")


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


def main_():  # 下赌注环节
    player1_ = get_valid_bet_input("Player 1(x)")
    player2_ = get_valid_bet_input("Player 2(o)")

    if player1_ > player2_:
        current_player = "X"
    elif player2_ > player1_:
        current_player = "O"
    else:
        current_player = random.choice(["X", "O"])

    print(f"Player {current_player} starts the game!")

    # 打印棋盘
    board = [" " for _ in range(9)]
    while True:
        print(f"{board[0]} | {board[1]} | {board[2]}")
        print("—————————")
        print(f"{board[3]} | {board[4]} | {board[5]}")
        print("—————————")
        print(f"{board[6]} | {board[7]} | {board[8]}")

        move = get_player_input(current_player)

        # 判断输入的数字是否有效

        if board[move] == " ":
            board[move] = current_player
        else:
            print("Invalid move. That position is already occupied. Try again.")
            continue

            # 判断是否有玩家获胜

        for Damn in range(0, 9, 3):
            if board[Damn] == board[Damn + 1] == board[Damn + 2] != " ":
                print(f"Player {current_player} wins the game!")
                print(f"Congratulations to Player {current_player} for winning {player1_ + player2_} dollars!")
                print("一看就是玩原神玩的（Doge")
                exit()
        for cock in range(3):
            if board[cock] == board[cock + 3] == board[cock + 6] != " ":
                print(f"\033[33;1mPlayer {current_player} wins the game!")
                print(f"\033[33;1mCongratulations to Player {current_player} for winning"
                      f" {player1_ + player2_} dollars! \033[0m")
                print("一看就是玩原神玩的（Doge")
                exit()
        if (board[0] == board[4] == board[8] != " ") or (board[2] == board[4] == board[6] != " "):
            print(f"\033[33;1mPlayer {current_player} wins the game!")
            print(f"\033[33;1mCongratulations to Player {current_player} for winning "
                  f"{player1_ + player2_} dollars! \033[0m")
            print("一看就是玩原神玩的（Doge")
            exit()
        # 判断是否有平局
        if " " not in board:
            print("\033[91No winner![1m")
            break

        # 切换玩家
        current_player = "X" if current_player == "O" else "O"


if __name__ == "__main__":
    main_()
