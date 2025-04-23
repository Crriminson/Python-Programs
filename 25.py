# Extend the Student class to include a method that checks whether the student has passed (marks > 40). 

# Using the class from the previous question (question 24)

class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Marks: {self.marks}")
    
    def has_passed(self):
        if self.marks > 40:
            print(f"{self.name} has passed.")
        else:
            print(f"{self.name} has not passed.")
            
student = Student("Mr Bean", 70, 100)

student.display()
student.has_passed()    