"""Methods in python are functions that are associated with objects.
They are called using the dot notation and can 
perform various operations on the object they are called on."""

#methos define behaviors and actions that an objecs of a class can be perfomer.
"""methods can take arguments, including a reference to the instance of the class
itself, typically named self, wich allows them to acess and modify the object attributes"""


"""when we define a class, that class can be referenced to create new objects,
and those objects can call the methods defined in the class to perform actions or retrieve information about themselves."""

class Dog:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        return f"{self.name} says woof!"
    
    
class Cat:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return f"{self.name} says meow!"
        
my_dog = Dog("Buddy")
print(my_dog.speak())  

my_dog2 = Dog("Rax")
print(my_dog2.speak())  

my_cat = Cat("Whiskers")
print(my_cat.speak())  # Output: Whiskers says meow!
my_cat2 = Cat("Mia")
print(my_cat2.speak())  # Output: Mia says meow!
