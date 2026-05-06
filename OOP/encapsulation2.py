"""Encapsulation helps in managing game object states by protecting
internal data and behavior. For example, game developers use encapsulation to 
manage object behavior and debug faster"""

class GameCharacter:
    def __init__(self, name, health):
        self.name = name
        self.__health = health
        self.__max_health = health
    
    @property
    def health(self):
        return self.__health

    def take_damage(self, amount):
        
        self.__health = max(0, self.__health - amount)
        
    def heal(self, amount):
        
        self.__health = min(self.__max_health, self.__health + amount)
    
hero = GameCharacter("Archer", 100)
print(hero.health)
hero.take_damage(30)
print(hero.health)
hero.heal(20)
print(hero.health)