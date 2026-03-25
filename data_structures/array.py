"""An array is basically a data structure which can hold more than one value at a time.
It is a collection or ordere series of elements of the same type."""
#EXAMPLE:

#Array can be created after importing the array module as follows
import array as arr
# from array import *    another model of import

#the following syntax
# a=array(data type, value list) when import using *

a=arr.array('d',[1.2,1.3,2.3]) #when import using array a
print(a)

"""note 
all values specified are of the type float. we cannot spicify the values
of different data types to a single array."""
#and we can access elements of array by their index's
print(a[1])
print(len(a))

# The basic array Operations are
# !*ADDING/CHANGING
a.append(3.4)
print(a)
print(len(a))

#we can change the value of the specific element at the particular position 
# !*INSERT
a.insert(1, 5.8)
print(a)

# !*CONCATENATING
# any two arrays can be concatenated using the + symbol.
b=arr.array('d', [3.7, 8.6])
c=a+b
print("Array c = ", c)
print("The lenght of Array C = ", len(c))

# !*REMOVING/DELETING
# Array elements can be removed using pop() or remove() method
print(c.pop()) #remove the last value of array
print(c.pop(3)) #remove the value of index[3]

# !*SLICING
#An array can be sliced using the : symbol
print(c[0:4])

# !*LOOPING

#looping through an array

print("all values")
for x in c:
    print(x)
print("Specific Values")
for x in c[1:3]:
    print(x)