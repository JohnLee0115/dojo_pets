class Pet:
    def __init__(self, name, type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 50
        self.noise = noise


    # implement the following methods:
    # sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25
        print(f"{self.name}'s energy is {self.energy}")
        return self

    # eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"{self.name}'s energy is {self.energy}")
        print(f"{self.name}'s health is {self.health}")
        return self
    # play() - increases the pet's health by 5
    def play(self):
        self.health += 5
        self.energy -= 15
        print(f"{self.name}'s energy is {self.energy}")
        print(f"{self.name}'s health is {self.health}")
        return self
    # noise() - prints out the pet's sound
    def noise(self):
        print(self.noise)

class Ninja():
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    # implement the following methods:
    # walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        print(f"Walking {self.pet.name}")
        self.pet.play()
        return self

    # feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        print(f"Feeding {self.pet.name} {self.pet_food}")
        self.pet.eat()
        return self
    # bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        print(f"Bathing {self.pet.name}, {self.pet.name} says {self.pet.noise}")

doggo = Pet("doggo", "shibe", "poop", "oogabooga")
naruto = Ninja("Naruto", "Uzumaki", "mcdonalds sprite", "beezchurger", doggo)

naruto.feed().walk().bathe()