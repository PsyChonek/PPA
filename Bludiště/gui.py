from vector2 import Vector2

class Gui:
    __canvas: list[list[str]]
    
    def __init__(self, width:int, height:int) -> None:
        self.__canvas = [[" " for _ in range(width)] for _ in range(height)]
    
    def draw(self, x:int, y:int, symbol:str) -> None:
        self.__canvas[y][x] = symbol
    
    def show(self) -> None:
        full_canvas = ""
        for row in self.__canvas:
            full_canvas += "".join(row) + "\n"
        print(full_canvas)
        
    def clear(self) -> None:
        for row in self.__canvas:
            for i in range(len(row)):
                row[i] = " "
    
    def input_direction(self) -> Vector2:
        userInput = int(input("Direction 8-up, 2-down, 4-left, 6-right:"))
        
        if (userInput == 8):
            inputVector = Vector2(0, -1)
        elif (userInput == 2):
            inputVector = Vector2(0, 1)
        elif (userInput == 4):
            inputVector = Vector2(-1, 0)
        elif (userInput == 6):
            inputVector = Vector2(1, 0)
        else:
            inputVector = Vector2(0, 0)
        
        return inputVector
        
    
    