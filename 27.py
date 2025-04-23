# Create a base class Animal with a method speak(), and subclasses Dog and Cat that override speak().

class Animal:
    def speak(self):
        print("The animal makes a sound.")

class Dog(Animal):
    def speak(self):
        print("The dog says: Woof! 🐶")

class Cat(Animal):
    def speak(self):
        print("The cat says: Meow! 🐱")
        

animal = Animal()
dog = Dog()
cat = Cat()

animal.speak()  
dog.speak()
cat.speak()