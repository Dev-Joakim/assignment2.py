# Base class: Character
class Character:
    def __init__(self, name, power, health):
        self.name = name
        self.power = power
        self.health = health

    def introduce(self):
        print(f"I am {self.name}. My power is {self.power}. Health: {self.health}")

    def attack(self, target):
        print(f"{self.name} attacks {target.name} using {self.power}!")
        target.take_damage(10)

    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} takes {amount} damage. Health now: {self.health}")

# Subclass: Superhero
class Superhero(Character):
    def __init__(self, name, power, health, catchphrase):
        super().__init__(name, power, health)
        self.catchphrase = catchphrase

    def introduce(self):
        super().introduce()
        print(f"Catchphrase: \"{
