from random import randint

board = []
#Erzeuge ein Spielfeld im Textformat
for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)

#erzeuge ein feindliches Schiff (nur ein Feld)
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    #was kommt hier rein?

ship_row = random_row(board)
ship_col = random_col(board)

#debugging parameters
#print ship_row
#print ship_col

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!


for turn in range(5):
    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col:"))
    #[..]
