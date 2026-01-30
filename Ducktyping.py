#Duck typing is a concept in programming where the type or class of an object is less important
#than the methods it defines or the behavior it exhibits. The name comes from the saying
#"If it looks like a duck and quacks like a duck, it must be a duck
class Animal:
    alive = True
class Dog(Animal):
    def speak(self):
        print("Woof!")
class Cat(Animal):
    def speak(self):
        print("Meow!")
class car:

    alive = False
    def speak(self):
        print("Vroom!")
animals = [Dog(), Cat(), car()]

for animal in animals:
    animal.speak()
    print(animal.alive)