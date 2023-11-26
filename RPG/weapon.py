class Weapon:
    """
    Třída reprezentující zbraň.
    @Author Daniel Vazač
    @Date 26.11.2023
    """
    __defense: int = 0
    __attack: int = 0
    __name: str = ""

    def __init__(self, name: str, attack: int, defense: int):
        """
        Inicializace zbraně.
        Args:
            name (str): Název zbraně.
            attack (int): Síla útoku.
            defense (int): Síla obrany.
        """
        self.__name = name
        self.__attack = int(attack) * 2
        self.__defense = int(defense)

    def attack(self) -> int:
        """
        Vrací hodnotu útoku zbraně.
        """
        return self.__attack

    def defense(self) ->int:
        """
        Vrací hodnotu obrany zbraně.
        """
        return self.__defense
    
    def __str__(self) -> str:
        """
        Vrací textovou reprezentaci zbraně.
        """
        return self.__name + " [" + str(self.attack()) + "/" + str(self.defense()) + "]"