"""The except clause may specify a variable after the exception name
The variable is bond to the exception in stance which typically has an
args attribute that stores the arguments. For convenience, builtin exception
types defines __str__() to print the arguments without excplicitly accessing .args."""

try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))    # the exception instance
    print(inst.args)     # arguments stored in .args
    print(inst)          # __str__ allows args to be printed directly
    x, y = inst.args     # unpack args into variables
    print('x =', x)
    print('y =', y)
    
"""
The Exception's __str__() output printed as the last part ('detail') of the message for unhandled exceptions.

BaseException is the common base class of all exceptions which are not subclasses of Exception are not tipically
handled, because they are used to indicate that the program should terminate, They include SystemExit which is
raised by sys.exit(), and KeyboardInterrupt which is raised when a user wishes to interrupt the program.

Exception can be used as wildcard that catches (almost) everthing. However, it is good pratice to be as 
specific as possible with the types of exceptions thet we intend to handle, and to allow any unexpected exceptions
to propragate on

The most common pattern for handling Exception is to print of log the exception and the re-raise it (allowing a caller to handle the exception as well)

"""
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except Exception as err:
    print("Unexpected error:", sys.exc_info()[0])
    raise

"""The try ... except statement has an optional else clause, which, when present, must follow all except clauses.
it is useful for code that must be executed if the try clause does not raise and exception for Example:"""

for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()


"""the use of the else clause is better than adding addional code to the try clause beause it avoids accidentally catching 
an exception that wasn't raised by the code being protected by the try ...except statemnet."""

"""Exception handlers do not handle only exceptions that occur immediately in the try clause, but also those that occur inside
functions that are called (even indirectly)in the try clause. For example:"""

def this_fails():
    x = 1/0
    try:
        this_fails()
    except ZeroDivisionError as err:
        print('Handling run-time error:', err)
#Handling run-time error: division by zero



