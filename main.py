import random
import os
def draw(table):
    print(f'{table[0]} {table[1]} {table[2]}\n'
          f'{table[3]} {table[4]} {table[5]}\n'
          f'{table[6]} {table[7]} {table[8]}')

def draw_check(game):
    if (game[0] != "_" and game[1] != "_" and game[2] != "_" and game[3] != "_" and game[4] != "_" and game[5] != "_" and game[
        6] != "_" and game[7] != "_" and game[8] != "_"):
        return True
    else:
        return False

def check(game, player):
    if ((game[0] == player and game[1] == player and game[2] == player)
            or (game[3] == player and game[4] == player and game[5] == player)
            or (game[6] == player and game[7] == player and game[8] == player)
            or (game[0] == player and game[3] == player and game[6] == player)
            or (game[1] == player and game[4] == player and game[7] == player)
            or (game[2] == player and game[5] == player and game[8] == player)
            or (game[0] == player and game[4] == player and game[8] == player)
            or (game[2] == player and game[4] == player and game[6] == player)):
        return True
    else:
        return False

def enter(symbol):
    try:
        z = int(input(f'Where {symbol}'))
        if z < 1 or z > 9:
            raise ValueError
    except ValueError:
        print("You entered wrong number")
    return z

def change(player):
    if (player == "X"):
        return "O"
    else:
        return "X"


print("\nHow to play\nYou have to enter a number between 1 and 9 to place a symbol)")
print("1 2 3 \n"
      "4 5 6 \n"
      "7 8 9 \n")

a = 0
empty = []
game = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
player = "X"
winner = False
tie = False
draw(game)

while winner == False and tie == False:
    try:
        a = int(input(f'Where {player}: '))
        if a < 1 or a > 9:
            raise ValueError
    except ValueError:
        print("You entered wrong number")
    else:
        if game[a-1] == "_":
            game[a-1] = player
            draw(game) #print table
            winner = check(game, player)
            if winner == True:
                print(f'{player} won the game')
                break
            else:
                tie = draw_check(game)
                if tie == True:
                    print("Draw")
                else:
                    player = change(player)
        else:
            print("This place is not available")

