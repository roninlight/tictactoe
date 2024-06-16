import random

class Player():
    def __init__(self,letter):
        self.letter = letter

class ComputerRandomMove(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        square = random.choice(game.available_move())
        return square

class HumanPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)
    
    def get_move(self,game):
        valid_move = False
        val = 0
        while not valid_move:
            try:
                square = input( f"{self.letter}'s move pick a spot from 0-8:")
                val = int(square)
                if val in game.available_move():
                    valid_move = True
                else:
                    print("Invalid move. Please try again.")
            except ValueError:
                print("Invalid input please try again")
        return val

class Tictactoe():
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_winner = None
    
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('|' + '|'.join(row) + '|')

    @staticmethod
    def print_board_num():
        board_num = [[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]
        for row in board_num:
            print('|' + '|'.join(row) + '|')
    
    def available_move(self):
        return [ i for i,spot in enumerate(self.board) if spot == " "]
    
    #this function should return true if there are empty spaces left on the board
    def empty_square(self):
        return " " in self.board

    def num_of_empty_square(self):
        return self.board.count(" ")

    def make_move(self,square,letter):
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square,letter):
                self.current_winner = letter
            return True
        return False
    def winner(self,square,letter):
        row_ind = square//3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all(spot == letter for spot in row):
            return True
        
        col_index = square%3
        colm = self.board[col_index::3]
        if all(spot == letter for spot in colm):
            return True
        if square%2 == 0:
            dgn_1 = self.board[0::4]
            if all(spot == letter for spot in dgn_1):
                return True
            dgn_1 = self.board[2:8:2]
            if all(spot == letter for spot in dgn_1):
                return True
        return False
            



def play(game,x_player,o_player,print_game= True):
    if print_game:
        game.print_board_num() 
    letter = "X"
    while game.empty_square():
        if letter == "X":
            square= x_player.get_move(game)
        else:
            square = o_player.get_move(game)
        
        if game.make_move(square,letter):
            print(f"{letter}'s makes a move at {square}")
            game.print_board()
            print("")
            if game.current_winner:
                print(f'{letter} wins')
                return letter
        if letter == "X":
            letter = "O"
        else:
            letter = "X"
    print("it's a tie")

if __name__ == "__main__":
    game  = Tictactoe()
    x_player = ComputerRandomMove("X")
    o_player = HumanPlayer("O")

    play(game,x_player,o_player)
