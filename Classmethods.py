class Student:
    count: int = 0
    total_gpa: float = 0.0
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
    #instance method
    def get_info(self):#self refers to the instance of the class
        return f"Name: {self.name}, GPA: {self.gpa}"
    @classmethod
    def get_count(cls):#cls refers to the class Student
        return f"Total number of students: {cls.count}"
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        return f"Average GPA: {cls.total_gpa / cls.count}"
student1 = Student("John", 3.5)
student2 = Student("Jane", 3.8)
student3 = Student("Jim", 3.2)
Student.total_gpa = student1.gpa + student2.gpa + student3.gpa
print(student1.get_info())
print(student2.get_info())
print(student3.get_info())
print(Student.get_count())
print(Student.get_average_gpa())