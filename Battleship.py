from random import randint

#Diese Variable wird das Spielfeld. Zu Beginn ist es leer.
board = []
#Erzeuge ein Spielfeld im Textformat
for x in range(5):
    board.append(["O"] * 5) #Hier wird eine Zeile mit 5 Os als Liste dem Spielfeld hinzugefuegt.

#Hier wird eine Methode beschrieben, die dann das Spielfeld erzeugt.
def print_board(board):
    for row in board:
        print " ".join(row)

#Hier beginnt nun das Starten der Oberfläche
print "Let's play Battleship!"
print_board(board)  #hier wird unser erzeugtes Spielfeld in die Methode zum Erzeugen hinzugefuegt

#erzeuge ein feindliches Schiff (nur ein Feld)
#Kann man das Schiff auch vergroessern?
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    #was kommt hier rein? Das musst DU vervollstaendigen

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
    """Aufgaben:
            - geratene Felder sollen durch ein "x" gekennzeichnet werden
            - das feindliche Schiff soll sich im Feld verstecken
            - du sollst eine Gewinnmethode einbauen. Wenn man das Schiff trifft -> sieg. Sonst hat man nach x Runden verloren.
            - Baue noch ein, was dir spontan einfaellt
    """
