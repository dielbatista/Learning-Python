import example_modules #by this keyword we import the example_modules defined in the same directory as this file.

print(example_modules.add(4, 5))

"""Import Python Standar library Modules
The python standar library contains many useful modules and we can import a module
according to our needs."""


import math #math module contains mathematical functions and constants

print("The value of pi is:", math.pi)

#And we can also import a module by renaming it. for Example
#import math as m
# print("The value of pi is:", m.pi)

"""Import all names
in python, we can also import all names definitions from a module using the following construct"""

##from math import * #This imports all names from the math module into the current namespace
#print("The value of pi is:", pi) #Now we can use pi directly without the math. prefix





"""The dir() built-in function
in python, we can use the di() function to list all function names in a module
for example, earlier we have defined the add() function in the modules example_modules.py, we can use the dir() function to list all names 
in the example_modules."""

print(dir(example_modules))
#the follwoing result is: ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'add']
print(example_modules.__name__)