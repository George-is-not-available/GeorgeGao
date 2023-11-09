class GameBoard:
    def __init__(self):
        self.board = [[' '] * 3 for _ in range(3)]

    def display_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def check_winner(self, player):
        # Implement the logic to check for a winner
        pass

    def make_move(self, row, col, symbol):
        # Implement the logic to make a move
        pass


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def make_move(self):
        # Implement the logic for the player to make a move
        pass


class Game:
    def __init__(self, player1, player2):
        self.board = GameBoard()
        self.players = [player1, player2]

    def start_game(self):
        # Implement the logic to start the game
        pass

    def play_turn(self, player):
        # Implement the logic for a player's turn
        pass


# Example usage:
player1 = Player("Player 1", "X")
player2 = Player("Player 2", "O")
tic_tac_toe_game = Game(player1, player2)
tic_tac_toe_game.board.display_board()
