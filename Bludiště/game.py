from gameobject import GameObject
from gui import Gui
from vector2 import Vector2
from world import World

class Game:
    __world: World
    __hero: GameObject
    __home: GameObject
    
    def __init__(self, world: World, hero: GameObject, home: GameObject) -> None:
        self.__world = world
        self.__hero = hero
        self.__home = home
        
    def run(self) -> bool:
        self.__world.draw(Gui(10, 10))
        self.__hero.move(self.__hero.position.)


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