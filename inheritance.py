class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.is_alive = True
    def eat(self):
        print(f"{self.name} is eating.")
    def sleep(self):
        print(f"{self.name} is sleeping.")
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")#super() calls the parent class constructor
        self.breed = breed
    def bark(self):
        print(f"{self.name} says Woof!")
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, species="Cat")
        self.color = color
    def meow(self):
        print(f"{self.name} says Meow!")
class Mouse(Animal):
    def __init__(self, name, weight):
        super().__init__(name, species="Mouse")
        self.weight = weight
    def squeak(self):
        print(f"{self.name} says Squeak!")
dog=Dog("Buddy", "Golden Retriever")
cat=Cat("Whiskers", "Tabby")
mouse=Mouse("Squeaky", 0.5)
print(dog.name)
print(cat.color)
print(mouse.weight)
dog.bark()
cat.meow()
mouse.squeak()
dog.eat()