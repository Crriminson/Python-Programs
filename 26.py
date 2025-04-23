#Write a class with a static variable college_name, and instance variables name and roll_no, and display all. 

class Student:
    college_name = "St Francis Institute of Technology" 
    
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
    
student = Student("Who Asked", "69")    

print("College Name:", Student.college_name)
print("Name:", student.name)
print("Roll No:", student.roll_no)