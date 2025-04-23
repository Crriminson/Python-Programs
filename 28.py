#Write a Python Program that does the following task. Take user’s First name and Last name as an input Concatenate both Print a personalize message “Hello ______ Welcome to SFIT

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def greet(self):
        full_name = f"{self.first_name} {self.last_name}"
        return f"Hello {full_name}, Welcome to SFIT!"
    

user = User(input("Enter your first name: "), input("Enter your last name: "))
print(user.greet())