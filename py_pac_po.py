print("---------------------")
print("Let's play Py-Pac-Poe")
print("---------------------")

score = {"X": 0, "O": 0, "T":0}
board = {}
turn = 'X'
winner = None

def play_game():
    global winner, turn
    init_game()
    while not winner:
        print_board()
        move = get_move()
        board[move] = turn 
        turn = 'O' if turn == 'X' else 'X'




def init_game():
    global board, turn, winner
    board = {
        'a1':' ', 'b1':' ', 'c1': ' ',
        'a2':' ', 'b2':' ', 'c2':' ', 
        'a3':' ', 'b3':' ', 'c3':' ' 
    }

    turn = "X"
    winner = None

def print_board():
    print( """
        A   B   C
        1) {} | {} | {}
        ---------------
        2) {} | {} | {}
        ---------------
        3) {} | {} | {}
        """.format(
            str(board['a1'] or ' '), str(board['b1'] or ' '), str(board['c1'] or ' '),
            str(board['a2'] or ' '), str(board['b2'] or ' '), str(board['c2'] or ' '),
            str(board['a3'] or ' '), str(board['b3'] or ' '), str(board['c3'] or ' ')
            )
        )    

def get_move():
  while True:
    move = input(f"Player {turn}'s Move (example B2): ").lower()
    if move in board and board[move] ==' ':
      return move
    else:
      print("Bogus move! Try again...\n")

play_game()

