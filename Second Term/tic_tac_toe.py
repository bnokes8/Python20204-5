#Tic Tac Toe
#Plays the game of tic tac toe against a human opponent
# Brady Nokes 11/20


# Global Constants
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9

# Function definitions
#########################################
def display_instructions():
    """Display game instructions. to use ( display_instructions() )"""
    print(
        """
        Welcome to the greatest intellectual challenge of all time: Tic-Tac-Toe.
        This will be a showdown between your human brain and my silicon processor.

        You will make your move known by entering a number, 0-8. The number
        will correspond to the board position as illustrated:

                                    \t0  |  1  |  2
                                    \t-----------
                                    \t3  |  4  |  5
                                    \t-----------
                                    \t6  |  7  |  8

        Prepare yourself human. The ultimate battle is about to begin. \n
        """
        )

def next_turn(currentTurn):
    """this function switches the turn in the game. to use (turn = next_turn(currentTurn))"""
    if currentTurn == X:
        return O
    else:
        return X
    
def pieces():
    """Determine if player or computer goes first. to use ( computer,human = pieces() )"""
    goFirst = ask_yes_no("Do you require the first move? (y/n): ")
    if goFirst == "y" or goFirst == "yes":
        human = X
        computer = O
        print("\nThen take the first move. You will need it.")
    else:
        print("\nYour bravery will be your undoing... I will go first.")
        human = O
        computer = X
    return computer, human



def ask_yes_no(question) :
    """Ask a yes or no question and get back a yes or no
    answer. to use (answer = ask_yes_no(question)) """
    response = None
    while response not in ("y","n","yes","no"):
        response = input(question).lower()
    return response


def new_board():
    """Create new game board full of empty spaces. to use ( board = new_board() )"""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)


    return board

def display_board(board):
    """Display game board on screen. to use ( display_board(board) )"""
    print(str.format("\t{}      |       {}      |       {}  ",board[0],board[1],board[2],))
    print("\t","-----------------")
    print(str.format("\t{}      |       {}      |       {}  ",board[3],board[4],board[5],))
    print("\t","-----------------")
    print(str.format("\t{}      |       {}      |       {}  ",board[6],board[7],board[8],))

def legal_move(board):
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves
    

def human_move(board):
    """Get human move. to use ( move = human_move() )"""
    legal = legal_move(board)
    move = None
    while move not in legal:
        move = ask_number("Where will you move? (0 - 8): ",0,NUM_SQUARES)
        if move not in legal:
            print("\nSquare is occupied foolish0 human choose another one\n")
    print("Fine")
    return move

def winner(board):
    """Determine the game winner"""
    WAYS_TO_WIN = ((0,1,2), #top row
                   (0,4,8), #diagonal
                   (2,4,6),#diagonal
                   (1,4,7),# middle
                   (3,4,5),
                   (6,7,8),
                   (0,3,6),
                   (2,5,8)
                   )
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
    if EMPTY  not in board:
        return TIE
    
    return None

def computer_move(board, computer, human):
    """Make Computer move"""
    # make a copy to work with since function will be changing list
    board = board[:]
    BEST_MOVES2 = (4,0,2,6,8,1,3,5,7)
    BEST_MOVES1 = (0,8,2,6,4,1,3,5,7)
##    (4,1,3,5,7,0,2,6,8) unbeatable
    print("I shall take the number", end =" ")
    
    # if pc can win, take that move
    for move in legal_move(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        board[move] = EMPTY

    #if human can win block that move
    for move in legal_move(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        board[move] = EMPTY
    # since no one can win on next move,pick best open square
    if computer == X:
        for move in BEST_MOVES1:
            if move in legal_move(board):
                print(move)
                return move
    else:
          for move in BEST_MOVES2:
            if move in legal_move(board):
                print(move)
                return move

def ask_number(question,low,high):
    """ Ask for a number within a range. to use ( answer = ask_number(question,low,high) )"""
    response = None
    while response not in range(low,high):
        response = int(input(question))
    return response
##########################################


# main Game
def main():
    players = input("1 or 2 players")
    display_instructions()
    turn = X
    computer,human = pieces()
    board = new_board()
    while not winner(board):
        if players == "2":
            display_board(board)
            move = human_move(board)
            board[move] = turn
            turn = next_turn(turn)
        else:
            if turn == human:
                move = human_move(board)
                board[move] = turn
                display_board(board)
            else:
                move = computer_move(board,computer,human)
                board[move] = turn
                display_board(board)
            turn = next_turn(turn)
    win = winner(board)
    print(win)



main()

