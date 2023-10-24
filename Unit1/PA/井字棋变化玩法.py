import time
import random



def player_choose_play(player):
    while True:
        try:
            player_choose = int(input(f"{player}, 你想玩《原版》还是玩《7步删》？"
                                      f"\n想玩《原版》输1，《7步删》输2: "))
            if player_choose == 1:
                play_original_version()
                break  # 游戏完成后退出循环
            elif player_choose == 2:
                play_seven_steps_version()
                break  # 游戏完成后退出循环
            else:
                print("无效选择，请输入 1 或 2。")
        except ValueError:
            print("Error: 无效输入，请输入 1 或 2。")


def print_board(board):
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i + 1]} | {board[i + 2]}")
        if i < 6:
            print("—————————")


def get_valid_bet_input(player_name):
    while True:
        try:
            bet = int(input(f"{player_name}, please place a bet: "))
            return bet
        except ValueError:
            print("Error: Invalid input. Please enter a valid number for the bet.")


def check_winner(board, player):
    for combo in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:
        if all(board[i] == player for i in combo):
            return True
    return False


def play_original_version():
    print("Downloading... (Expect to download 170.52MB)")
    for i in range(2, 10):
        print("——————", end='')
        time.sleep(1)
    print("\033[93m The game is ready.\033[0m")

    player1_bet = get_valid_bet_input("Player 1 (x)")
    player2_bet = get_valid_bet_input("Player 2 (o)")

    if player1_bet != player2_bet:
        current_player = "X" if player1_bet > player2_bet else "O"
    else:
        current_player = random.choice(["X", "O"])

    print(f"\033[98m Player {current_player} starts the game![0m")

    board = [" " for _ in range(9)]
    move_count = 0

    while True:
        print_board(board)
        move = get_player_input(current_player, board)
        board[move] = current_player
        move_count += 1

        if move_count >= 5 and check_winner(board, current_player):
            print_board(board)
            print(f"\033[93mPlayer {current_player} wins the game!")
            winnings = player1_bet + player2_bet
            print(f" Congratulations to Player {current_player} for winning {winnings} dollars!"
                  f"一看就是玩原神玩的（doge\033[0m")
            exit()

        if move_count == 9:
            print_board(board)
            print("\033[1mNo winner[0m")
            exit()

        current_player = "X" if current_player == "O" else "O"


def get_player_input(current_player, board):
    while True:
        try:
            move = int(input(f"Player {current_player}, choose a position (1-9) to play: "))
            if 1 <= move <= 9:
                if board[move - 1] == " ":
                    return move - 1  # 调整索引以匹配列表的索引
                else:
                    print("Invalid move. That position is already occupied. Try again.")
            else:
                print("\033[94m Oh Dash!\033[35m Please enter a number between 1 to 9.\033[0m")
        except ValueError:
            for _ in range(1, 10):
                print(".", end='')
                time.sleep(1)
            print('\n \033[94mDamn\033[91m What are you doing??????\n')
            time.sleep(2)
            print('\033[96m一看就是玩原神玩多了。\n \033[93m')
            time.sleep(2)
            print('Please enter a number between 1 to 9.\033[0m \n ')
            time.sleep(2)
            print('\033[94mDamn it!  \n \033[93mCan\'t you understand what I\'m talking about??? \n ')
            time.sleep(2)
            print("\033[33mI really don‘t know what’s going on in your head!\n \033[95m")
            time.sleep(2)
            print('Come on, please play by the rules!\033[0m \n')


def play_seven_steps_version():
    print("Downloading... (Expect to download 217.52MB)")
    for i in range(1, 15):
        print("———", end='')
        time.sleep(1)
    print("\033[93m The game is ready.\033[0m")
    print("\n\033[95m声明：\033[0m")
    print("\033[91m注意请不要在下棋过程中输入字符串或大于9的数字（下赌注除外）！！！\033[0m")

    player1_bet = get_valid_bet_input("Player 1 (X)")
    player2_bet = get_valid_bet_input("Player 2 (O)")

    if player1_bet != player2_bet:
        current_player = "X" if player1_bet > player2_bet else "O"
    else:
        current_player = random.choice(["X", "O"])

    print(f"\033[98mPlayer {current_player} starts the game!\n \033[0m")

    board = [" " for _ in range(9)]
    move_count = 0

    while True:
        print_board(board)
        move = get_player_input(current_player, board)
        board[move] = current_player
        move_count += 1

        if move_count >= 5:
            print_board(board)
            print(f"\033[93mPlayer {current_player} wins the game!")
            winnings = player1_bet + player2_bet
            print(f"[93mCongratulations to Player {current_player} for winning {winnings} dollars!"
                  f"一看就是玩原神玩的（doge\033[0m")
            exit()

        current_player = "X" if current_player == "O" else "O"


if __name__ == "__main__":
    player_choose_play("Player")
