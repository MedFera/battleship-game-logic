def takePoint(size):
    input_accepted = False
    while input_accepted == False:
        try:
            start_point = input("\nEnter a start point for your "+ str(size)+" length ship: (RowColumn)\n")
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
            
def takeOrientation(start_point: str, board, size: int):
    orientation_accepted = False
    pointsArray = []
    while orientation_accepted == False:
        try:
            orientation = input("\nEnter ship orientation vertically or horizontally (H or V)\n")
            answer = orientation.upper()
            if answer == "V" or answer == "H":
                try:
                    row = int(start_point[0])
                    column = int(start_point[1])
                    if orientation == "V" and size+row <= 5:                         
                        for i in range(row, (size+row), 1):
                            board[i][column] = "S"
                            pointsArray.append(str(i) + str(column))
                            #print("Placed at " + str(i) + "," + str(column))
                        orientation_accepted = True
                        return pointsArray
                    elif orientation == "H" and size+column <= 5:
                        for j in range(column, (size+column), 1):
                            board[row][j] = "S"
                            pointsArray.append(str(row) + str(j))
                            #print("Placed at " + str(row) + "," + str(j))
                        orientation_accepted = True
                        return pointsArray
                    else:
                        print("The whole ship must be placed on the board!!!")
                        orientation_accepted = False
                        return pointsArray
                except Exception as e: 
                    print(e)
            else:
                print("Please enter H or V!")
                orientation_accepted = False
        except Exception as e: 
            print(e)

def determineShipName(size):
    carrier = [ "Submarine", "Cruiser", "Carrier", "Battleship"]
    return carrier[size - 1]
    

def checkCollision(potential_points, all_ships):
    TwoD_Array = []
    for item in all_ships:
        TwoD_Array.append(item.points)
        
    if potential_points == []:
        return False
    elif any(any(value in sublist for value in potential_points) for sublist in TwoD_Array):
        return False
    else:
        return True
    
    
        
class Ship:
    def __init__(self):
        self.name = ""
        self.is_afloat = False
        self.size = 0
        self.points = []
    
    def CPUship(self, size:int , provided_points:list):
        self.name = determineShipName(size)
        self.points = provided_points
        self.is_afloat = True
        self.size = size
        
    def PlaceShip(self, size:int, board, current_ships_placed):
        self.name = determineShipName(size)
        self.size = size
        ship_placed = False
        
        while ship_placed == False:
            try:
                start = takePoint(self.size)
                potential_array = takeOrientation(start, board, size)
                ship_placed = checkCollision(potential_array, current_ships_placed)
                
                if ship_placed == True:
                    self.points = potential_array
                    self.is_afloat = True
                
                else:
                    print("***ERROR COULD NOT PLACE SHIP COLLISION ERROR!***")
            except Exception as e: 
                print(e)
            

        
        
        
        