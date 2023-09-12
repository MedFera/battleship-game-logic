

class Board:
    
    def __init__(self):
        self.name = ""
        self.board = [
            [" ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " "]
        ]
        
    def displayBoard(self):
        board_string = " _0_1_2_3_4_"
        for i in range(len(self.board)):
            board_string += "\n" + str(i) + "_"
            for j in self.board[i]:
                board_string += j + "_"
        print("\n"+self.name +"\n"+ board_string)
        
    def setBoardName(self, name:str , boardtype:str):
        self.name = name + " " + boardtype
        
    def populateBoardWithShips(self, player):
        player.ships