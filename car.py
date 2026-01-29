class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print("You drive the {self.color} {self.model}")
    def stop(self):
        print("You stop the {self.color} {self.model}")
    def describe(self):
        print(f"This car is a {self.year} {self.color} {self.model}")