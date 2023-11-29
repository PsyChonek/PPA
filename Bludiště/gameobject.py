from gui import Gui
from vector2 import Vector2

class GameObject:
    __position: Vector2
    __symbol: str
    
    def __init__(self, position: Vector2, symbol: str) -> None:
        self.__position = position
        self.__symbol = symbol
    
    def move(self, direction:Vector2)-> None:
        self.__position += direction
    
    def draw(self, gui:Gui) -> None:
        gui.draw(self.__position.__x, self.__position.__y, self.__symbol)
        
    @property
    def position(self) -> Vector2:
        return self.__position