class Student:
    class_year=2024
    num_students=30
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        Student.num_students += 1
student1=Student("Alice", 14, "9th")
student2=Student("Bob", 15, "10th")
student3=Student("Charlie", 14, "9th")
student4=Student("David", 16, "11th")

print(f"my graduating class of {Student.class_year} has {Student.num_students} students")
print(student1.name)
print(student2.age)
print(student3.grade)
print(student4.name)