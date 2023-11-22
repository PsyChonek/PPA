from weapon import Weapon

class Character:
    HAND_LEFT: int = 0
    HAND_RIGHT: int = 1

    __name: str = ""
    __vitality: int = 0
    __strength: int = 0
    __agility: int = 0
    
    __leftHand: Weapon = None
    __rightHand: Weapon = None

    def __init__(self, name: str, vitality: int, strength: int, agility: int):
        self.__name = name
        self.__vitality = int(vitality)
        self.__strength = int(strength)
        self.__agility = int(agility)

    def attack(self) -> int:
        totalAttack: int = self.__strength
        if self.__leftHand != None:
            totalAttack += self.__leftHand.attack()
        if self.__rightHand != None:
            totalAttack += self.__rightHand.attack()
        return totalAttack
    
    def defense(self) -> int:
        totalDefense: int = self.__agility
        if self.__leftHand != None:
            totalDefense += self.__leftHand.defense()
        if self.__rightHand != None:
            totalDefense += self.__rightHand.defense()
        return totalDefense
    
    def receiveDamage(self, damage: int):
        dmg = int(damage) - int(self.defense())
        if dmg < 0:
            dmg = 0
        
        self.__vitality -= int(dmg)
    
    def equip(self, hand:int, weapon: Weapon|None):
        if hand == self.HAND_LEFT:
            self.__leftHand = weapon
        elif hand == self.HAND_RIGHT:
            self.__rightHand = weapon
        else:
            raise ValueError("Invalid hand")
        
    def isAlive(self) -> bool:
        return int(self.__vitality) > int(0)
    
    def getWeapon(self, hand: int) -> Weapon:
        if hand == self.HAND_LEFT:
            return self.__leftHand
        elif hand == self.HAND_RIGHT:
            return self.__rightHand
        else:
            raise ValueError("Invalid hand")
    
    def __str__(self)-> str:
        return self.__name + " [" + str(self.__vitality) + "] " + "("+ str(self.attack()) +"/"+ str(self.defense())+")"