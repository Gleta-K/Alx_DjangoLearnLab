class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age 
    def student_information(self):
        student_details = f"My name is {self.name} and I am {self.age} years old"
        return student_details
student1 = Student("Much", "noyb")
print(student1.student_information())    