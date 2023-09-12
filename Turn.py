import random

def takePoint():
    input_accepted = False
    while input_accepted == False:
        try:
            start_point = input("Enter an attack point (RowColumn): ")
            if len(start_point) > 2 or len(start_point) < 2:
                input_accepted = False
                print("CoordinateError: String length not length 2")
            elif int(start_point[0]) > 4 and int(start_point[1]) > 4:
                input_accepted = False
                print("CoordinateError: A digit is too big")
            else:
                input_accepted = True
                return start_point
        except Exception as e: 
            print(e)

    
    

class Turn:
    
    def __init__(self, Player, CPU):
        #PLAYER TURN ACTIONS
        if Player.turn == True:
            attack_accepted = False
            while attack_accepted == False:
                Player.atkBoard.displayBoard()
                print("\n")
                Player.defBoard.displayBoard()
                print("\n")
                player_input = takePoint()
                row = int(player_input[0])
                col = int(player_input[1])
                if Player.atkBoard.board[row][col] == " ":
                    attack_accepted = True
                    if CPU.defBoard.board[row][col] == "S":
                        Player.atkBoard.board[row][col] = "H"
                        CPU.defBoard.board[row][col] = "X"
                        for ship in CPU.ships:
                            for point in ship.points:
                                if point == player_input:
                                    ship.points.remove(player_input)
                                    if ship.points == []:
                                        ship.is_afloat == False
                                        print("You sunk a " + ship.name)
                                    break
                        Player.turn = False
                        CPU.turn = True
                    else:
                        Player.atkBoard.board[row][col] = "M"
                        CPU.defBoard.board[row][col] = "O"
                        Player.turn = False
                        CPU.turn = True
                else:
                    attack_accepted = False
                    print("Attack Not Accepted. Try Again.")
        #CPU TURN ACTIONS
        elif CPU.turn == True:
            attack_accepted = False
            while attack_accepted == False:
                row = random.randint(0, 4)
                col = random.randint(0, 4)
                if CPU.atkBoard.board[row][col] == " ":
                    attack_accepted = True
                    if Player.defBoard.board[row][col] == "S":
                        CPU.atkBoard.board[row][col] = "H"
                        Player.defBoard.board[row][col] ="X"
                        print("\nCPU hit you at " +str(row)+str(col)+"\n")
                        guess_point = str(row) + str(col)
                        for ship in Player.ships:
                            for point in ship.points:
                                if point == guess_point:
                                    ship.points.remove(guess_point)
                                    if ship.points == []:
                                        ship.is_afloat == False
                                        print("CPU sunk a " + ship.name)
                                    break
                        Player.turn = True
                        CPU.turn = False        
                    else:
                        CPU.atkBoard.board[row][col] = "M"
                        Player.defBoard.board[row][col] = "O"
                        print("\nCPU missed you at " +str(row)+str(col)+"\n")
                        Player.turn = True
                        CPU.turn = False
                else:
                    attack_accepted = False
                    #print("CPU trying shot again")
        else:
            print("Turn error neither player or CPU have turn")
    
    