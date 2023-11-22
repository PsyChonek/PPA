class Weapon:
    __defense: int = 0
    __attack: int = 0
    __name: str = ""

    def __init__(self, name: str, attack: int, defense: int):
        self.__name = name
        self.__attack = int(attack)
        self.__defense = int(defense)

    def attack(self) -> int:
        return self.__attack

    def defense(self) ->int:
        return self.__defense
    
    def __str__(self) -> str:
        return self.__name + " [" + str(self.attack()) + "/" + str(self.defense()) + "]"