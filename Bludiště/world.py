from gui import Gui
from vector2 import Vector2


class World:
    __width: int
    __height: int
    __world: list[list[str]]
    
    def __init__(self,data:list[list[int]],symbols:list[str]) -> None:
        self.__width = len(data[0])
        self.__height = len(data)
        self.__world = []
        for y in range(self.__height):
            row = []
            for x in range(self.__width):
                row.append(symbols[data[y][x]])
            self.__world.append(row)
        
    def is_empty(self, position:Vector2) -> bool:
        return self.__world[position.y][position.x] == " "
    
    def draw(self, gui:Gui) -> None:
        for y in range(self.__height):
            for x in range(self.__width):
                gui.draw(x, y, self.__world[y][x])
                
    @property
    def width(self)->int:
        return self.__width
    
    @property
    def height(self)->int:
        return self.__height
