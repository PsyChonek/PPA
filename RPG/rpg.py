    
from character import Character
from weapon import Weapon

class RPG:
    character1: Character
    character2: Character
    
    def __init__(self):
        pass
    
    def run(self):
        # Create character1
        self.character1 = self.inputCharacter()
                
        # Equip character1 with weapon
        self.character1.equip(0,self.inputWeapon())
        self.character1.equip(1,self.inputWeapon())
         
        print(self.character1)        
        print(self.character1.getWeapon(0))
        print(self.character1.getWeapon(1))
        
        # Create character2
        self.character2 = self.inputCharacter()

        # Equip character2 with weapon
        self.character2.equip(0,self.inputWeapon())
        self.character2.equip(1,self.inputWeapon())	
        
        print(self.character2)
        print(self.character2.getWeapon(0))
        print(self.character2.getWeapon(1))
               
        print("Souboj zacina")
        while self.character1.isAlive() and self.character2.isAlive():
            self.fight(self.character1, self.character2)

        if self.character1.isAlive():
            print("Vitez: " + str(self.character1))
        else:
            print("Vitez: " + str(self.character2))

    def fight(self, character1: Character, character2: Character):
        character2.receiveDamage(character1.attack())
        if character2.isAlive():
            character1.receiveDamage(character2.attack())
    
    def inputCharacter(self)->Character|None:
        return Character(input(), input(), input(), input())
    
    def inputWeapon(self)->Weapon|None:
        name = input()
        
        if name == "":
            return None
        else:
            return Weapon(name, input(), input())            
        
if __name__ == "__main__":
    rpg = RPG()
    rpg.run()