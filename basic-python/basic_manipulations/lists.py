#Data structure List

"""Python lists syntax is so simple like [] 
"""

#we can declarate an list as

numbers = [1, 2, 3, 4, 5]
#and access the list by referent index like
print(numbers[0])#index 0 number 1
print(numbers[4])#index 4 number 5

#or print all of list content by reference of your name
print(numbers)

"""In Python, if(loops) evaluates to false"""

lista = [] 
if lista :
    print("never be executed")
else:
    print("always be executed")
    
    
"""Unlike strings, lists are mutable, which means that you can change their content without changing their identity."""
cubes = [1, 8, 27, 65, 125] # something's wrong here
4 ** 3 # the cube of 4 is 64, not 65!
cubes[3] = 64 # replace the wrong value with the right one
print(cubes)    

"""You can also add new items to the end of a list, by using the append() method:"""
cubes.append(216) # add the cube of 6
cubes.append(7 ** 3) # add the cube of 7
print(cubes)

"""Simple assignmets in Python never copies data, they create bindings between a target and an object.
This means that when you assign a list to another variable, both variables refer to the same list.
If you change the list through one of the variables, the change will be visible through the other variable as well. 
This is because both variables are referencing the same list object in memory."""


rgb = ['red', 'green', 'blue']
rgba = rgb # rgba is just another name for the same list

print(rgb) # ['red', 'green', 'blue']

id(rgb) == id(rgba) # True they refer to the same object
rgba.append('alpha')

print(rgb) # ['red', 'green', 'blue', 'alpha'] both variables refer

"""All slice operations return a new list containing the requsted elements
this means the the following sliece rturns a shallow copy of the list:"""

correct_rgba = rgba[:] # make a copy of the list
correct_rgba[-1] = 'alpha' # replace the wrong value with the right one
print(correct_rgba) # ['red', 'green', 'blue', 'alpha']
print(rgba) # ['red', 'green', 'blue', 'alpha'] the original list is unchanged

#The built-in function len() returns the number of items in a list:
letters = ['a', 'b', 'c', 'd']
print(len(letters)) # 4
