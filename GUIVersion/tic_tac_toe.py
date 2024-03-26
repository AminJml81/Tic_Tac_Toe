class Player:
    number = 1

    def __init__(self, sign):
        """Initializing player

        -attributes:
                    sign: str = x | o
                    id: int = 1 | 2
        """
        self.sign = sign
        self.id = Player.number
        Player.number += 1


class Grid:

    def __init__(self):
        self.board = [i + 1 for i in range(0, 9)]
        self.empty_places = 9


class Game:

    WINNING_CONDITIONS = {
        # horizontal positions
        1: (1, 2, 3),
        2: (4, 5, 6),
        3: (7, 8, 9),
        # vertical positions
        4: (1, 4, 7),
        5: (2, 5, 8),
        6: (3, 6, 9),
        # diagonal positions
        7: (1, 5, 9),
        8: (3, 5, 7),
    }

    def __init__(self):
        """Creates two player objects and the grid """
        self.player1 = Player('X')
        self.player2 = Player('O')
        self.players = [self.player1, self.player2]
        self.grid = Grid()

    def check_win(self):
        """Checks the winning conditions"""
        for position in Game.WINNING_CONDITIONS.values():
            if self.grid.board[position[0] - 1] == self.grid.board[position[1] - 1] == self.grid.board[position[2] - 1]:
                return True
        return False

    def check_draw(self):
        """Checks the draw condition"""
        return self.grid.empty_places == 0
