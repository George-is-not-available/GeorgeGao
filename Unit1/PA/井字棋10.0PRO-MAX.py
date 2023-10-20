import random

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
                      'Are you STUPID??????\n'
                      'Please enter a number between 1 to 9 \n '
                      'Damn it! \n Can\'t you understand what i\'m talking about??? \n '
                      'I really don\'t know what\'s going on in your head! '
                      'Fu*k you!\033[0m \n')
            else:
                print("Please try again!")
                continue

import random

def main():
    while True:
        try:
            player1_ = int(input("Player 1(x), please place a bet: "))
            player2_ = int(input("Player 2(o), please place a bet: "))
            if player1_ != player2_:
                current_player = "X" if player1_ > player2_ else "O"
            else:
                current_player = random.choice(["X", "O"])
            print(f"Player {current_player} starts the game!")
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for the bet.")



    board = [" " for _ in range(9)]

    while True:
        print(f"{board[0]} | {board[1]} | {board[2]}")
        print("——————————")
        print(f"{board[3]} | {board[4]} | {board[5]}")
        print("——————————")
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
                break

        for i in range(3):
            if board[i] == board[i + 3] == board[i + 6] != " ":
                print(f"Player {current_player} wins the game!")
                print(f"Congratulations to Player {current_player} for winning {player1_ + player2_} dollars!")
                break

        if (board[0] == board[4] == board[8] != " ") or (board[2] == board[4] == board[6] != " "):
            print(f"Player {current_player} wins the game!")
            print(f"Congratulations to Player {current_player} for winning {player1_ + player2_} dollars!")
            break

        if " " not in board:
            print(f"No winner! {player1_ + player2_} will be cleared.")
            break

        current_player = "X" if current_player == "O" else "O"



if __name__ == "__main__":
    main()
