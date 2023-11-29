from gameobject import GameObject
from gui import Gui
from vector2 import Vector2
from world import World

class Game:
    __world: World
    __hero: GameObject
    __home: GameObject
    
    __gui: Gui
    
    def __init__(self, world: World, hero: GameObject, home: GameObject) -> None:
        self.__world = world
        self.__hero = hero
        self.__home = home
        
        self.__gui = Gui(world.width, world.height)
        
    def run(self) -> bool:
        # Vykresli svet
        self.__world.draw(self.__gui)
        self.__hero.draw(self.__gui)
        self.__home.draw(self.__gui)
        self.__gui.show()
        self.__gui.clear()
        inputVector = self.__gui.input_direction()
        self.__hero.move(inputVector)
        if self.__hero.position == self.__home.position:
            return True
        elif self.__world.is_empty(self.__hero.position):
            return self.run()
        return False
    
    
if __name__ == "__main__":
    world = World(
[[1,1,1,1,1,1],
 [1,0,0,1,0,1],
 [1,0,0,1,0,1],
 [1,0,0,0,0,1],
 [1,1,1,1,1,1]],
[' ','#'])
    hero = GameObject(Vector2(1,1),"@")
    home = GameObject(Vector2(4,1),"^")

    destination = Game(world,hero,home).run()
    if destination: 
        print("Vitej doma!")
    else:
        print("... a uz ho nikdy nikdo nevidel... ")