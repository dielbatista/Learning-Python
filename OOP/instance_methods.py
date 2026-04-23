"""INSTANCE METHODS are functions that you define inside a class and can only call on an 
instance of that class. Just like __init__(), an instance method always takes self as its
first parameter

Open a new editor window in IDLE and type in the following Dog class:"""

class Dog:
    species = "Canis familiaris"
    
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
        
        #instance method
        
 #  def description(self):
    def __str__(self):
        return f"{self.name} has {self.age} years old, and his breed is {self.breed}"
    
        #Another instance Method
    def speak(self, sound):
        return f"{self.name} says {sound}"
    
    
    
miles = Dog("Miles",6, "caramelo")
# print(miles.description()) 
"""description() returns a string displaying the name and age of the dog
   speak() has one parameter called sound and return string containing the dog's name and the sound that the dog makes"""
   
print(miles.speak("Woof Woof")) # by this line the function speak can be receive the argument woof woof on the return.

print(miles)

"""When we print miles, we get a cryptic-looking message telling, that miles is a Dog
object at the memory addres 0x7505c54a2340. This message isn't very helpful and can be changed
what gets printed by defining a special instance method called. __str__()"""