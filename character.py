class Character:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"Hello, my name is {self.name}.")

    def instigate(self, target):
        print(f"{self.name}: I'm not a big fan of {target}.")

    def attack(self, opponent):
        opponent.health = opponent.health - self.strength
        print(f"{self.name} attacks {opponent.name}!")
        print(f"{opponent.name} HP:",opponent.health)
        if opponent.health < 0:
            print(f"{self.name} wins!")

character_1 = Character("Peter", 342, 40)
character_2 = Character("Joe", 280, 60)

print(character_1.name, character_1.health)
print(character_2.name, character_2.health)

character_1.greet()
character_2.greet()
character_2.instigate(character_1.name)

while character_1.health > 0 and character_2.health > 0:
    character_1.attack(character_2)
    character_2.attack(character_1)