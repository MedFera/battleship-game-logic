from Board import Board
from Ship import Ship
from Player import Player
from Turn import Turn
import random

def any_ships_on_board(arr, target):
    for row in arr:
        for element in row:
            if element == target:
                return True
    return False

def extra_print_lines():
    print("\n\n\n\n")
    
def coin_flip (player: Player):
    coin_flip = random.randint(0,1)
    choice_flip = input("Please select Heads or Tails (Enter H or T):\n")

    choice_flip_upper = choice_flip.upper()

    if choice_flip_upper == "H" and coin_flip == 1:
        player.turn = True
        
    elif choice_flip_upper == "T" and coin_flip == 0:
        player.turn = True
        
    else:
        player.turn = False

#EVERYTHING BELOW IS FOR NEW GAME PLAYER SETUP
print("""
Welcome to MedFer's Battle Ship

You will be given four ships to place down on the board

The board will consist of rows(horizontal) and columns(vertical) labeled 0 through 4

When placing ships down on your board you will be prompted to pick a start point then an orientation

After you select the point the orientation will place the ship horizontally to the right or vertically downward

Keep this in mind so you do not place the ship off the board

Then enjoy a normal game of BattleShip!

- Thank you for playing
	Medin Feratovic
""")

player_defense = Board()
player_attacks= Board()
player1 = Player(player_attacks, player_defense)
player1.setName()
extra_print_lines()

player_defense.setBoardName(player1.name + "'s" , "Defense Board")
player_attacks.setBoardName(player1.name + "'s" , "Attack Board")

print("\nThis is your empty board: ")
player1.defBoard.displayBoard()

player_4_ship = Ship()
player_4_ship.PlaceShip(4, player_defense.board, player1.ships)
player1.addShip(player_4_ship)
player1.defBoard.displayBoard()

player_3_ship = Ship()
player_3_ship.PlaceShip(3, player_defense.board, player1.ships)
player1.addShip(player_3_ship)
player1.defBoard.displayBoard()

player_2_ship = Ship()
player_2_ship.PlaceShip(2, player_defense.board, player1.ships)
player1.addShip(player_2_ship)
player1.defBoard.displayBoard()

player_1_ship = Ship()
player_1_ship.PlaceShip(1, player_defense.board, player1.ships)
player1.addShip(player_1_ship)

extra_print_lines()

print("\nYou finished setting up your board.\nThese are your boards: ")

player_attacks.displayBoard()
player_defense.displayBoard()

#EVERYTHING BELOW WILL BE A COMPUTER PLAYER

CPU_defense = Board()
CPU_attacks = Board()
CPU_Player = Player(CPU_attacks, CPU_defense)
CPU_Player.newComputerPlayer()

CPU_defense.setBoardName(CPU_Player.name + "'s" , "Defense Board")
CPU_attacks.setBoardName(CPU_Player.name + "'s" , "Attack Board")

CPU_Player.generateCPUBoard1(CPU_defense)
#CPU_defense.displayBoard()
#CPU_attacks.displayBoard()


extra_print_lines()
coin_flip(player1)

if player1.turn == False:
    CPU_Player.turn = True
    extra_print_lines()
    print("CPU will go first!")
else:
    extra_print_lines()
    print("Player will go first!")



player_won = False
cpu_won = False
round_number = 0

while player_won == False and cpu_won == False:
    round_number += 1
    player_has_ships = any_ships_on_board(player1.defBoard.board, "S")
    cpu_has_ships = any_ships_on_board(CPU_Player.defBoard.board, "S")
    if player_has_ships == False:
        cpu_won = True
        print("**********YOU LOST************")
        break
    elif cpu_has_ships == False:
        player_won = True
        print("**********YOU WON************")
        break
    else:
        print("Round Number: " + str(round_number))
    newTurn = Turn(player1, CPU_Player)
    
#EVERYTHING ABOVE WORKS AND RUNS A WHOLE GAME