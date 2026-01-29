#polymorphism is the ability to present the same interface for differing underlying data types.
#In polymorphism, methods in different classes that do similar things have the same name.
from abc import ABC, abstractmethod
class Shape(ABC):

    @abstractmethod
    def area(self) -> float:
        pass
class Circle(Shape):
    def __init__(self, radius=1):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
class Square(Shape):
    def __init__(self, side=1):
        self.side = side
    def area(self):
        return self.side ** 2
class Triangle(Shape):
    def __init__(self, base=1, height=1):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
class Pizza(Circle):
    def __init__(self, topping, radius=1):
        super().__init__(radius)
        self.topping = topping
shapes = [Circle(4), Square(5), Triangle(6,7), Pizza("pepperoni", 8)]
for shape in shapes:
    print(f"The area of the {shape.__class__.__name__} is {shape.area()}")
