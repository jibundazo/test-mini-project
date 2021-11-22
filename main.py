# print("我很厉害")
# print("hello world")

"""
Easier to use for large comments
 Print below:
 ___|___|___
 ___|___|___
    |   |

O wins
"""

import random as r 

# 0 = no input, 1 = O, 2 = X
inputs = [0,0,0,0,0,0,0,0,0]
player_input = 0


def ask_for_input():
    player_input = 0
    while player_input == 0:
        try:
            player_input = int(input("Enter a number between 1 - 9: "))

            if player_input < 1 or player_input > 9:
                raise ValueError("Out of Range")

            # Do not re-insert in to filled block
            if inputs[player_input - 1] != 0:
                raise ValueError("Position already taken")
        except ValueError as e:
            player_input = 0
            print(e)

    return player_input


def render():
    input_render = ["","","","","","","","",""]
    for idx in range(9):
        render = ""
        input = inputs[idx]
        if input == 0:
            render = " "
        elif input == 1:
            render = "O"
        elif input == 2:
            render = "X"
        input_render[idx] = render

    #print board with inputs
    print(" ", input_render[0], "|" , input_render[1], "|", input_render[2], sep=" ")
    print("----+---+----")
    print(" ", input_render[3], "|" , input_render[4], "|", input_render[5], sep=" ")
    print("----+---+----")
    print(" ", input_render[6], "|" , input_render[7], "|", input_render[8], sep=" ")
    print("")

def machine_move():
    # if center square is empty then choose that
    if inputs[4] == 0:
        return 4
    
    while True:
        move=r.randint(0,8)
        #if the move (square) is blank, go ahead and choose, otherwise try again
        if inputs[move] == 0:
            # print("Did I come here before?")
            return move
            


# Check winners
def check_for_win():
    possible_win_combinations = [
        [inputs[0], inputs[1], inputs[2]], # Top Horizontal
        [inputs[3], inputs[4], inputs[5]], # Middle Horizontal
        [inputs[6], inputs[7], inputs[8]], # Bottom Horizontal
        [inputs[0], inputs[3], inputs[6]], # Left Vertical
        [inputs[1], inputs[4], inputs[7]], # Middle Vertical
        [inputs[2], inputs[5], inputs[8]], # Bottom Vertical
        [inputs[0], inputs[4], inputs[8]], # \ Diagonal
        [inputs[2], inputs[4], inputs[6]], # / Diagonal
    ]

    for combination in possible_win_combinations:
        if combination == [1,1,1]:
            return [True, 1]
        elif combination == [2,2,2]:
            return [True, 2]

    return [False, 0] # No win combination found at this point.

def main():
    player_turn = True
    while True:
        #If (player_turn) {ask for input} else {machine_move}
        if player_turn:
            player_input = ask_for_input()
            inputs[player_input - 1] = 1
            player_turn = False
        else:
            print("Machine's turn!")
            player_input = machine_move()
            inputs[player_input] = 2
            player_turn = True

        # print(inputs)
        render()

        determine_winner = check_for_win()
        if determine_winner[0]:
            print("Congratulations Player ", str(determine_winner[1]), ", you WIN!", sep="")
            break

main()