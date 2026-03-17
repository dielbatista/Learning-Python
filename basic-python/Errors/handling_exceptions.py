#Handling Exceptions
"""It is possible to write programs that handle selected exceptions.
look at the following example, which asks the user for input until a valid integer has been entered,
but allows the user to interrupt the program with Ctrl-C: (or whatever the operating system's interrupt key is)"""
while True:
    try:
        x = int(input("Please enter a number:"))
        break
    except ValueError:
        print("Oops! That was no valid number. Try again...")
        
"""the try statement may have more than one except clause, to specify handlers for different exceptions.
at most one handler will be executed. handlers only handle exceptions that occur in the corresponding try clause, no int other
handlers of the same try statement. an except clause may name multiple exceptions, for example:
"""
except (RuntimeError, TypeError, NameError):
    pass

"""a ckass in an excet clauses matches exceptions which are instantes of the class 
itself or one of its devived classes but not the way around - an except clause listing
a devired class does not match instances of its base classes). For example, the following code will print
B, C, D in that order:"""


class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass    
for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")  
        
