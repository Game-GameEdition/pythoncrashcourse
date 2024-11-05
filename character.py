from randomness import *
from random import *
import time

lcg = LCG(time.time())

class Character:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
        self.is_alive = True

    def greet(self):
        print(f"Hello, my name is {self.name}.")

    def instigate(self, target):
        print(f"{self.name}: I'm not a big fan of {target}.")

    def attack(self, opponent):
        #note: this is totally redundant, i just wanted to use functions from randomness.py
        
        # rolled_multiplier = int(self.strength * float(seed.random()))
        # this is very bloated. damage should be a separate function.
        damage = int(self.strength * 0.75 + self.strength * 0.5 * lcg.random())
        opponent.health = opponent.health - damage
        print(f"{self.name} attacks {opponent.name}!")
        print("Damage done:",damage)
        # this could also probably be a separate function
        if (opponent.health <= 0):
            opponent.is_alive = False
            print(f"{opponent.name} has {opponent.health} health remaining.")
            print(f"{self.name}, wins!")
        else:
            print(f"{opponent.name} has {opponent.health} health remaining.")
        

character_1 = Character("Peter", 200, 20)
character_2 = Character("Joe", 200, 20)

print(character_1.name, character_1.health)
print(character_2.name, character_2.health)

character_1.greet()
character_2.greet()
character_2.instigate(character_1.name)

while character_1.health > 0 and character_2.health > 0:
    if (randrange(0,2)) == 0:
        character_1.attack(character_2)
        if character_2.is_alive:
            character_2.attack(character_1)
    else:
        character_2.attack(character_1)
        if character_1.is_alive:
            character_1.attack(character_2)