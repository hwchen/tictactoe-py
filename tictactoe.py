# Program to play Tic Tac Toe. No Gui
# AI: if any line has two pieces, play on empty spot. else play in center, then
# corner. Hard-coded!
# I don't feel like adding GUI to this right now.

class TTT():
    """Contains state of board, methods to make a move"""
    """Two players: 1 and 2"""
    """ grid state is kept in 0,1,2; only labelled on output"""
    player_label = ["_", "X", "O"]

    def __init__(self):
        #redo grid, the coordinates are backwards for x and y
        self.grid = [[0 for x in range(3)] for x in range(3)]
        print("Welcome to TicTacToe!\n")
        print("Player X goes first:\n")
    
    def __repr__(self):
        res = "\n"
        for i in range(3):
            res += ("%d " % i)
            for j in range(3):
                res += (" %s " % (TTT.player_label[self.grid[i][j]]))
            res += ("\n")
        res += ("   0  1  2")
        return res

    def __str__(self):
        return self.__repr__() 

    def add_move(self, (x,y), player):
        """modifies grid by adding move at position x,y with Player.
        Internally, player 1 is X. player is an Int."""
        self.grid[x][y] = player

    def prompt_move(self, player):
        """prompts player for move, checks if valid move, then
        calls add_move"""
        print("Player %s's turn: " % TTT.player_label[player])

        input_flag = False
        while not input_flag: 
            try:
                movex = int (raw_input('Enter row coord : '))
                movey = int (raw_input('Enter col coord : '))
                if movex in range(3) and movey in range(3):
                    if self.grid[movex][movey] == 0:
                        input_flag = True
                    else:
                        print("Move already taken!\n")
                else: 
                    print("Incorrect Input, please try again!\n")
            except ValueError:
                print("Numbers only\n")

        self.add_move((movex, movey), player)
        
    def check_status(self):
        """Checks, in order: 3 in a row for player 1, then player 2,
        then if board is full then draw.
        Returns 0 for unresolved
        returns 1 for player 1 win
        returns 2 for player 2 win
        returns 3 for draw. """

        #Check if any tile has two neighbors for player 1, then 2  
        #eight winning conditions * 2 players

        for i in range(3):
            if self.grid[i][0]==self.grid[i][1] and self.grid[i][1]==self.grid[i][2]:
                return self.grid[i][0]
            elif self.grid[0][i]==self.grid[1][i] and self.grid[1][i]==self.grid[2][i]:
                return self.grid[0][i]
        #Diagonals
        if self.grid[0][0]==self.grid[1][1] and self.grid[1][1]==self.grid[2][2]:
            return self.grid[0][0]
        elif self.grid[2][0]==self.grid[1][1] and self.grid[1][1]==self.grid[0][2]:
            return self.grid[2][0]

        #draw
        for i in range(3):
            for j in range(3):
                if self.grid[i][j] == 0:
                    return 0
        return 3; 

    def ai(self):
        """First play at third spot if two in a row; then center then
        corners"""
        player = 2
        #check rows 
        #row 0
        if self.grid[0][0]==self.grid[0][1] and self.grid[0][0] != 0 and self.grid[0][2] == 0:
            self.add_move((0,2), player)
        elif self.grid[0][0]==self.grid[0][2] and self.grid[0][0] != 0 and self.grid[0][1] == 0:
            self.add_move((0,1), player)
        elif self.grid[0][1]==self.grid[0][2] and self.grid[0][1] != 0 and self.grid[0][0] == 0:
            self.add_move((0,0), player)

        #row 1
        elif self.grid[1][0]==self.grid[1][1] and self.grid[1][0] != 0 and self.grid[1][2] == 0:
            self.add_move((1,2), player)
        elif self.grid[1][0]==self.grid[1][2] and self.grid[1][0] != 0 and self.grid[1][1] == 0:
            self.add_move((1,1), player)
        elif self.grid[1][1]==self.grid[1][2] and self.grid[1][1] != 0 and self.grid[1][0] == 0:
            self.add_move((1,0), player)
        #row 2
        elif self.grid[2][0]==self.grid[2][1] and self.grid[2][0] != 0 and self.grid[2][2] == 0:
            self.add_move((2,2), player)
        elif self.grid[2][0]==self.grid[2][2] and self.grid[2][0] != 0 and self.grid[2][1] == 0:
            self.add_move((2,1), player)
        elif self.grid[2][1]==self.grid[2][2] and self.grid[2][1] != 0 and self.grid[2][0] == 0:
            self.add_move((2,0), player)

        #check columns
        #column 0
        elif self.grid[0][0]==self.grid[1][0] and self.grid[0][0] != 0 and self.grid[2][0] == 0:
            self.add_move((2,0), player)
        elif self.grid[0][0]==self.grid[2][0] and self.grid[0][0] != 0 and self.grid[1][0] == 0:
            self.add_move((1,0), player)
        elif self.grid[1][0]==self.grid[2][0] and self.grid[1][0] != 0 and self.grid[0][0] == 0:
            self.add_move((0,0), player)
        #column 1
        elif self.grid[0][1]==self.grid[1][1] and self.grid[0][1] != 0 and self.grid[2][1] == 0:
            self.add_move((2,1), player)
        elif self.grid[0][1]==self.grid[2][1] and self.grid[0][1] != 0 and self.grid[1][1] == 0:
            self.add_move((1,1), player)
        elif self.grid[1][1]==self.grid[2][1] and self.grid[1][1] != 0 and self.grid[0][1] == 0:
            self.add_move((0,1), player)
        #column 2
        elif self.grid[0][2]==self.grid[1][2] and self.grid[0][2] != 0 and self.grid[2][2] == 0:
            self.add_move((2,2), player)
        elif self.grid[0][2]==self.grid[2][2] and self.grid[0][2] != 0 and self.grid[1][2] == 0:
            self.add_move((1,2), player)
        elif self.grid[1][2]==self.grid[2][2] and self.grid[1][2] != 0 and self.grid[0][2] == 0:
            self.add_move((0,2), player)

        #Diagonals
        elif self.grid[0][0]==self.grid[2][2] and self.grid[0][0] != 0 and self.grid[1][1] == 0: 
            self.add_move((1,1), player)
        elif self.grid[0][0]==self.grid[1][1] and self.grid[0][0] != 0 and self.grid[2][2] == 0: 
            self.add_move((2,2), player)
        elif self.grid[1][1]==self.grid[2][2] and self.grid[1][1] != 0 and self.grid[0][0] == 0:
            self.add_move((0,0), player)
        elif self.grid[0][2]==self.grid[1][1] and self.grid[0][2] != 0 and self.grid[2][0] == 0: 
            self.add_move((2,0), player)
        elif self.grid[0][2]==self.grid[2][0] and self.grid[0][2] != 0 and self.grid[1][1] == 0:
            self.add_move((1,1), player)
        elif self.grid[1][1]==self.grid[2][0] and self.grid[1][1] != 0 and self.grid[0][2] == 0:
            self.add_move((0,2), player)

        #center 
        elif self.grid[1][1]==0:
            self.add_move((1,1), player)

        #special case, if two adjacent in-betweens, play at that corner
        elif self.grid[0][1]==self.grid[1][0] and self.grid[0][0] == 0: 
            self.add_move((0,0), player)
        elif self.grid[0][1]==self.grid[1][2] and self.grid[0][2] == 0: 
            self.add_move((0,2), player)
        elif self.grid[2][1]==self.grid[1][0] and self.grid[2][0] == 0: 
            self.add_move((2,0), player)
        elif self.grid[2][1]==self.grid[1][2] and self.grid[0][2] == 0:
            self.add_move((0,2), player)
       
        #else random corner
        elif self.grid[0][0] == 0:
            self.add_move((0,0), player)
        elif self.grid[2][0] == 0:
            self.add_move((2,0), player)
        elif self.grid[0][2] == 0:
            self.add_move((0,2), player)
        else:
            self.add_move((2,2), player)

if __name__ == '__main__':
    game = TTT()
#    game.add_move((0,1),1)
    print(game)

    turn = 1
    game_over = False
    while not game_over:
        if turn == 1:
            game.prompt_move(turn)
        else:
            game.ai()
        print(game)
        status = game.check_status()
        if status == 0:
            if turn == 1:
                turn = 2
            else:
                turn = 1
        elif status == 1:
            print("Player X wins!")
            game_over = True
        elif status == 2:
            print("Player O wins!")
            game_over = True
        elif status == 3:
            print("It's a draw!")
            game_over = True

   
