from Ship import Ship
from Board import Board
import random

def find_index_2d(arr, target):
    for i, row in enumerate(arr):
        for j, item in enumerate(row):
            if item == target:
                return i, j
    return None

def new_CPU_ship_gen (ship_size:int, possible_points_list:list):
    ship_placed = False
    while ship_placed == False:
        orientation = ["H","V"]
        orient_choice = random.randint(0, 1)
        
        random_row_value = -1
        random_column_value = -1
        
        #possible start points for size 4 ship
        
        if(orientation[orient_choice] == "H"):
            random_row_value = random.randint(0, 4) 
            random_column_value = random.randint(0, (5 - ship_size)) 
        elif(orientation[orient_choice] == "V"):
            random_row_value = random.randint(0, (5 - ship_size)) 
            random_column_value = random.randint(0, 4) 
        else:
            print("ERROR WITH RANDOM PROCESS")
        
        start_point = str(random_row_value) + str(random_column_value)
        #print(start_point)
        #print(orientation[orient_choice])
        
        #create potential array for start points
        potential_array = []
        size = ship_size # size of ship
        row = int(start_point[0])
        column = int(start_point[1])
        
        if(orientation[orient_choice] == "H"):
            for j in range(column, (size+column), 1):
                potential_array.append(str(row) + str(j))
        elif(orientation[orient_choice] == "V"):
            for i in range(row, (size+row), 1):
                potential_array.append(str(i) + str(column))
        else:
            potential_array = []
            
        #print(potential_array)
        
        #Next we check if points are available in possible points (points left after placing ships)
        
        if all(any(point in sublist for sublist in possible_points_list) for point in potential_array):
            #print("Points are available placing ship")
            for point in potential_array:
                result = find_index_2d(possible_points_list, point)
                r, c = result
                possible_points_list[r][c] = "XX"
            ship_placed = True
            
        else:
            #print("Points conflict retry!")
            ship_placed = False
    #print(possible_points_list)
    return size, potential_array, possible_points_list

class Player:
    def __init__(self, attack:Board, defense:Board) -> None:
        self.name = ""
        self.ships = []
        self.turn = False
        self.defBoard = defense
        self.atkBoard = attack
        
        
    def newComputerPlayer(self):
        self.name = "CPU Opponent"
        self.turn = False
        pass
    
    def setName(self):
        name_accepted = False
        while name_accepted == False:
            entry = input("\nPlease enter your name: \n")
            confirm = input("Is this correct: " + entry + " (Enter Y or N)\n")
            if confirm == "Y":
                print("\n\nWelcome to the battle " + entry)
                self.name = entry
                name_accepted = True
            elif confirm == "N":
                print("Okay enter your name again!")
                name_accepted = False
            else:
                print("Wrong input try again!")
                name_accepted = False
                
    def addShip(self, ship):
        self.ships.append(ship)
    
    def showPlayerShips(self):
        print("\nCoordinates of Ships: \n")
        for ship in self.ships:
            print(ship.name + ": " + str(ship.points))
            
    def generateCPUBoard1(self, CPU_board):
        possible_points = [["00", "01", "02", "03", "04"],
                           ["10", "11", "12", "13", "14"],
                           ["20", "21", "22", "23", "24"],
                           ["30", "31", "32", "33", "34"],
                           ["40", "41", "42", "43", "44"]]
        
        for i in range(4,0,-1):
            ship = new_CPU_ship_gen(i, possible_points)
            size, list, new_possible_points = ship
            new_CPU_ship = Ship()
            new_CPU_ship.CPUship(size, list)
            self.addShip(new_CPU_ship)
            for point in new_CPU_ship.points:
                row = int(point[0])
                col = int(point[1])
                CPU_board.board[row][col] = "S"
            possible_points = new_possible_points
            
        
        
        

        
