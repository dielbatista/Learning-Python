#Tuples & sequences

"""What is a tuple
in simplest terms, a Python tuple is similar to a list, which is a simple way of defining a multiple variables."""



#Exmample of a simple variable assignment

color1 = 'red'
color2 = 'blue'
color3 = 'green'
color4 = 'yellow'

colors = color1, color2, color3, color4 #we can pack the variables into a tuple
print(type(colors)) #we can see that the type of colors is a tuple

colorst = ('red', 'blue', 'green', 'yellow') #we can also define a tuple with parentheses
print(type(colorst))

t = (12345, 54321, 'hello!')
print(t[0]) #tuples can be referenced by the index just like lists

print(t)

u = t, (1, 2, 3, 4, 5) #tuples may be nested
print(u)

#t[0] = 88888 #tuples are immutable, they cannot be changed

#but they can contain mutable objects, like lists
v = ([1, 2, 3], [3, 2, 1])
print(v)


"""Types of Tuples
there are four different types of tuples:
1. Empty tuple: ()
2. Singleton tuple: (1,) - note the comma, without it, it would be just an integer in parentheses
3. Nested tuple: ((1, 2), (3, 4))
4. Heterogeneous tuple: (1, 'hello', 3.14) - a tuple that contains different types of data
"""