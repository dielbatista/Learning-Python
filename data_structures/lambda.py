#link for consult: realpython.com/python-lambda/

"""First example
The identity function, a function that returns its argument, is expressedn with a standard 
Python function definitionusing the keyword def as follows:"""
def identity(x):
    return x

"""identity() takes an argument x and returns it upon invocation.
in contrast, if you use a Python lambda construction, you get the following>"""
identity = lambda x: x

"""We can write a slightly more elaborated example, a function that adds 1 to an argument, as follows:"""
add_one = lambda x: x + 1

print(add_one(2))  # Output: 3

"""(lambda x: x + 1)(2) = lambda 2: 2 + 1
                        = 2 + 1
                        = 3
                        
because a lambda function is and expression, it can be named. Therefore you could write the
previous code as follows:
"""
add_one = lambda x: x + 1
print(add_one(2))

#The above lambda function is equivalent to writing this:
def add_one(x):
    return x + 1

"""These functions all take a single argument. You may have noticed that, in the definition of
the lambdas, the argument don't have parentheses around them. Milti-argument functions (functions that take more than one argument)
are expressed in python lambdas by listing arguments and separating them with a comma (,) but without sorrounding them
with parentheses."""

full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
print(full_name('guido', 'van rossum'))

"""The lambda function assigned to full_name takes two arguments and returns a string
interpolating the two parameters first and last. As expected, the definition of the lambda
lists the arguments with no parentheses, whereas calling the function is done exactly a normal python function,
with parentheses surrounding the arguments."""

