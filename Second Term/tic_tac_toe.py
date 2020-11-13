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

def human_move():
    """Get human move. to use ( move = human_move() )"""
    move = None
    while move == None:
        move = ask_number("Where will you move? (0 - 8): ",0,NUM_SQUARES)
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
    display_instructions()
    turn = X
    computer,human = pieces()
    board = new_board()
    while True:
        display_board(board)
        move = human_move()
        board[move] = turn
        turn = next_turn(turn)



main()

