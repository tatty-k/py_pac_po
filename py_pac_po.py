print("---------------------")
print("Let's play Py-Pac-Poe")
print("---------------------")

def init_game():
    state = {}

    state['board'] = {
        'a1':' ', 'b1':' ', 'c1': ' ',
        'a2':' ', 'b2':' ', 'c2':' ', 
        'a3':' ', 'b3':' ', 'c3':' ' 
    }

    state['turn'] = {
        1: "X",
        -1: "O"
    }

    print( """
        A   B   C
        1) {} | {} | {}
        ---------------
        2) {} | {} | {}
        ---------------
        3) {} | {} | {}
        """.format(state['board']['a1'], 
        state['board']['b1'], state['board']['c1'], 
        state['board']['a2'], state['board']['b2'], 
        state['board']['c2'], state['board']['a3'],
        state['board']['b3'], state['board']['c3']))
    
    player = state['turn'][1]
    
    player_input = input(f"Player {player}'s Move (example B2): ")

init_game()


