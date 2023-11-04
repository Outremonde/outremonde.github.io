import random

options = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
player_turn = "x"

def reset():
    options = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    player_turn = "x"

def draw_board():
    print(options[7] + " | " + options[8] + " | " + options[9])
    print("----------")
    print(options[4] + " | " + options[5] + " | " + options[6])
    print("----------")
    print(options[1] + " | " + options[2] + " | " + options[3])

def win_check():
    if options[1] == options[2] == options[3]:
        return(options[1])
    elif options[4] == options[5] == options[6]:
        return(options[4])
    elif options[7] == options[8] == options[9]:
        return(options[7])
    elif options[1] == options[4] == options[7]:
        return(options[1])
    elif options[2] == options[5] == options[8]:
        return(options[2])
    elif options[3] == options[6] == options[9]:
        return(options[3])
    elif options[1] == options[5] == options[9]:
        return(options[1])
    elif options[3] == options[5] == options[7]:
        return(options[3])

def write_choice(choice, player):
    if options[int(choice)] == " ":
        if player == "x":
            options[int(choice)] = "x"
        elif player == "o":
            options[int(choice)] = "o"
    else:
        print("Space is taken, try again!")
        ask_choice(player)

def ask_choice(player):
    if player == "x":
        x_choice = input("Player X, choose a space (1-9 as if on a numpad): ")
        write_choice(x_choice, "x")
    elif player == "o":
        o_choice = input("Player O, choose a space (1-9 as if on a numpad): ")
        write_choice(o_choice, "o")

reset()
draw_board()
while True:
    if player_turn == "x":
        player_turn = "o"
        ask_choice("x")
        draw_board()
    elif player_turn == "o":
        player_turn = "x"
        ask_choice("o")
        draw_board()

    if win_check() == "x":
        print("X wins!")
        restart = input("Play again? (y/n): ")
        if restart == "n":
            reset()
            break
    elif win_check() == "o":
        print("O wins!")
        restart = input("Play again? (y/n): ")
        if restart == "n":
            reset()
            break
    



