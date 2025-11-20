# # # Inheritance 
# class Shape: # parent class 
#     def __init__(self, name):
#         self.name = name 

#     def area(self):
#         return 0
    
# class Circle(Shape): # Child inherits from Shape
#     def __init__(self, radius):
#         super().__init__("Circle") # Calls parent constructor
#         self.radius = radius 

#     def area(self): # Override parent method 
#         return 3.14 * self.radius * self.radius
    
# class Square(Shape): # Child inherits from Shape 
#     def __init__(self, width, height):
#         super().__init__("Square")
#         self.width = width
#         self.height = height 

#     def area(self): # Override parent method 
#         return self.width * self.height
    
# # Instances. Both Circle and Square inherit 'name' attribute from Shape 
# CircleObj = Circle(5)
# SquareObj = Square(4,5) 

# print(CircleObj.name) # Circle (inherited from Shape)
# print(SquareObj.name) # Square (inhereted from Shape)
# print(SquareObj.area())

# # Polymorphism
# def print_area(Shape): 
#     print(f"{Shape.name} area: {Shape.area()}")

# # Same method call, different behaviours 
# print_area(CircleObj) # "Circle area: 78.5"
# print_area(SquareObj) # "Square area: 16"

# Or with a list 
# Shapes = [Circle(3), Square(5), Circle(2)]
# for Shape in Shapes:
#     print_area(Shape) # Same code, different results 


#------

# # Practice 2: 
# class animal:
#     def __init__(self, name):
#         self.name = name
    
#     def sound(self):
#         return "Can't speak in human language"


# class dog(animal):
#     def __init__(self, name):
#         super().__init__(name)

#     def sound(self):
#         return "Woof! Woof! Woof!"
    
# class cat(animal):
#     def __init__(self, name):
#         super().__init__(name) 

#     def sound(self):
#         return "prrrr, meooowwww!"
    

# DogName = dog("Unit D-92")
# CatName = cat("Ozzy")

# print(DogName.name, "says", DogName.sound())
# print(CatName.name, "says", CatName.sound())

#  Practice 3: 
#  1. Create a parent class Employee with: 
# - name, 
# - salary
# - a method describe() that prints something simple.

# 2. Create two child classes.
# - Manager(Employee)
# - Intern(Employee)

# 3. Override describe() in both to print different messages.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def description(self):
       return f"{self.name} is an Employee earning RM{self.salary}" 

class Manager(Employee):
    def __init__(self, name):
        super().__init__(name, 10000)

    def description(self):
        return f"{self.name} is a Manager earning RM{self.salary}"

    def salary(self):
        return "10,000.00"

class Intern(Employee):
    def __init__(self, name):
        super().__init__(name, 1800)

    def description(self):
        return f"{self.name} is an Intern earning RM{self.salary}"
    
    
ManagerName = Manager("Terence")
InternName = Intern("Cindy")

print(ManagerName.description())
print(InternName.description())




  

# Exercise 1:
# 1. Create a vehichle hierarchy (vehicle --> car, motorcycle, truck) with different behaviours. 