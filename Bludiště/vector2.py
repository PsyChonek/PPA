from __future__ import annotations

class Vector2:
    __x: int
    __y: int
    
    def __init__(self, x: int, y: int) -> None:
        self.__x = x
        self.__y = y
                
    def __add__(self, other: Vector2) -> Vector2:
        return Vector2(self.__x + other.__x, self.__y + other.__y)
    
    def __eq__ (self, other: Vector2) -> bool:
        if self.__x == other.__x and self.__y == other.__y:
            return True
        else:
            return False
    
    def __str__(self)->str:
        return f"({self.__x}, {self.__y})"
    
    @property 
    def x(self) -> int:
        return self.__x
    
    @property 
    def y(self) -> int:
        return self.__y