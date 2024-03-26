
class Player:
    number = 1

    def __init__(self, sign):
        """Initializing player

        -attributes:
                    sign: str = x | o
                    id: int = 1 |2
        """
        self.sign = sign
        self.id = Player.number
        Player.number += 1
        
        
class Grid:

    def __init__(self):
        """
        attributes
                    board: List
                           representing 9 tic_tac_toe positions

                    board_text: str
                            to display it to user

                    empty_places: str
                            keeps record of grid empty places

        """
        self.board = [i+1 for i in range(0, 9)]
        self.board_text = ' (1)  |  (2)  |  (3)  \n (4)  |  (5)  |  (6)  \n (7)  |  (8)  |  (9)  '
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
        """Creates two player objects and run the game"""
        self.player1 = Player('X')
        self.player2 = Player('O')
        self.players = [self.player1, self.player2]
        self.grid = Grid()
        self.counter = 0

    def move(self, player: Player):
        """
        it validates player input and adds player sign to the grid.

        parameters:
                    player: Player

        adds players sign to the corresponding position
        """
        while True:
            position = int(input("Enter position: ")) - 1
            if position > 8 or position < 0:
                print('Invalid Position')
            if type(self.grid.board[position]) != int:
                print('The position is taken')
            else:
                break

        self.grid.board[position] = player.sign
        self.grid.board_text = self.grid.board_text.replace(f'({position+1})', player.sign)

    def check_win(self):
        """Checks the winning conditions"""
        for position in Game.WINNING_CONDITIONS.values():
            if self.grid.board[position[0]-1] == self.grid.board[position[1]-1] == self.grid.board[position[2]-1]:
                return True
        return False

    def check_draw(self):
        """Checks the draw condition"""
        return self.grid.empty_places == 0

    def run(self):
        """
        it will get grid numbers from player , adds player sign to it, decrease 1 from empty_places
           and checks for win or draw
        """

        print('------Welcome to The Game------')

        while True:
            print()
            print(self.grid.board_text)

            if self.counter % 2 == 0:
                self.move(self.player1)
            else:
                self.move(self.player2)

            self.grid.empty_places -= 1

            if self.check_win():
                text = f"player {(self.counter % 2)+1} ({self.players[(self.counter % 2)].sign}) has won the game "
                print(text)
                self.play_again()
                break

            if self.check_draw():
                print('Draw')
                self.play_again()
                break

            self.counter += 1

    def play_again(self):
        """
            asks the user to play again or not if yes it will call rerun function
                 else it will close the application
        """
        print()
        play_again = input('do you want to play again\n Y N\n ')
        if play_again.lower() == 'yes' or play_again.lower() == 'y':
            self.rerun()
        sys.exit()

    def rerun(self):
        """it will create another grid instance"""
        self.grid = Grid()
        self.counter += 1
        self.run()


if __name__ == '__main__':
    import sys
    Game().run()
