#Tuples & sequences

t = (12345, 54321, 'hello!')
print(t[0]) #tuples can be referenced by the index just like lists

print(t)

u = t, (1, 2, 3, 4, 5) #tuples may be nested
print(u)

#t[0] = 88888 #tuples are immutable, they cannot be changed

#but they can contain mutable objects, like lists
v = ([1, 2, 3], [3, 2, 1])
print(v)
