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
        winner = get_winner()
    handle_winner()




def init_game():
    global board, turn, winner
    board = {
        'a1': None, 'b1': None, 'c1': None,
        'a2': None, 'b2': None, 'c2': None, 
        'a3': None, 'b3': None, 'c3': None 
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
    if move in board and board[move] == None:
      return move
    else:
      print("Bogus move! Try again...\n")

def get_winner():
  b = board
  if b['a1'] and b['a1'] == b['a2'] == b['c3']: return b['a1']
  if b['b1'] and b['b1'] == b['b2'] == b['b3']: return b['b1']
  if b['c1'] and b['c1'] == b['c2'] == b['c3']: return b['c1']
  if b['a1'] and b['a1'] == b['b1'] == b['c1']: return b['a1']
  if b['a2'] and b['a2'] == b['b2'] == b['c2']: return b['a2']
  if b['a3'] and b['a3'] == b['b3'] == b['c3']: return b['a3']
  if b['a1'] and b['a1'] == b['b2'] == b['c3']: return b['a1']
  if b['c1'] and b['c1'] == b['b2'] == b['a3']: return b['c1']
  return None if None in b.values() else 'T' 

def handle_winner():
  print_board()
  if winner == "T":
    print("Tie game. Try again!")
  else:
    print(f"{winner} wins!")
play_game()

