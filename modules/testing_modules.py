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

