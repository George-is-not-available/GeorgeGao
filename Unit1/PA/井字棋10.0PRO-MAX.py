import random


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
                print("Invalid position. Please enter a number between 1 to 9.")
        except ValueError:
            print("Please enter a number.")
            invalid_input_count += 1
            if invalid_input_count >= 2:
                print("Wait...................")
                print('\033[91mWhat are you Fa*king doing??????\n'
                      '\033[96mAre you STUPID??????\n \033[93m'
                      'Please enter a number between 1 to 9 \033[0m \n '
                      '\033[94mDamn it!  \n \033[93mCan\'t you understand what i\'m talking about??? \n '
                      '\033[33mI really don\'t know what\'s going on in your head!\n \033[95m'
                      'Come on, please play by the rules!\033[0m \n')
            else:
                print("\033[91mDamn it!"
                      "What's problem with you?\033[0m")

def main():
    player1_ = get_valid_bet_input("Player 1(x)")
    player2_ = get_valid_bet_input("Player 2(o)")

    current_player = ""
    if player1_ > player2_:
        current_player = "X"
    elif player2_ > player1_:
        current_player = "O"
    else:
        current_player = random.choice(["X", "O"])

    print(f"Player {current_player} starts the game!")

    board = [" " for _ in range(9)]



    while True:
        print(f"{board[0]} | {board[1]} | {board[2]}")
        print("---------")
        print(f"{board[3]} | {board[4]} | {board[5]}")
        print("---------")
        print(f"{board[6]} | {board[7]} | {board[8]}")

        move = get_player_input(current_player)

        if board[move] == " ":
            board[move] = current_player
        else:
            print("Invalid move. That position is already occupied. Try again.")
            continue

        for i in range(0, 9, 3):
            if board[i] == board[i + 1] == board[i + 2] != " ":
                print(f"Player {current_player} wins the game!")
                print(f"Congratulations to Player {current_player} for winning {player1_ + player2_} dollars!")
                exit()

        for i in range(3):
            if board[i] == board[i + 3] == board[i + 6] != " ":
                print(f"Player {current_player} wins the game!")
                print(f"Congratulations to Player {current_player} for winning {player1_ + player2_} dollars!")
                exit()

        if (board[0] == board[4] == board[8] != " ") or (board[2] == board[4] == board[6] != " "):
            print(f"Player {current_player} wins the game!")
            print(f"Congratulations to Player {current_player} for winning {player1_ + player2_} dollars!")
            exit()

        if " " not in board:
            print("It's a tie!")
            break

        current_player = "X" if current_player == "O" else "O"


if __name__ == "__main__":
    main()
