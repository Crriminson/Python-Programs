#Write a Python Program that does the following task Create example for a module and import it in you program  
 
# A module named my_module.py is created with a function to calculate the area of a circle.
import my_module

radius = int(input("Enter the radius of the circle: "))

area = my_module.area_of_circle(radius)

print(f"The area of the circle with radius {radius} is: {area}")