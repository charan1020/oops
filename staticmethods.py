#static method is a method that belongs to a class rather than an instance of a class.
#It can be called on the class itself, rather than on an instance of the class.
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
    def get_info(self):
        return f"Name: {self.name}, Position: {self.position}"
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Developer", "Designer", "Intern"]
        return position in valid_positions
employee=Employee("Alice", "Developer")
employee2=Employee("Bob", "Chef")
employee3=Employee("Charlie", "Manager")
print(Employee.is_valid_position("Developer")) 
print(employee.get_info())
print(employee2.get_info())
print(employee3.get_info())