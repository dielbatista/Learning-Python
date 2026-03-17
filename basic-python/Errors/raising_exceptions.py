"""The raise statement allows the programmer to force a specified exception to occur. For Example:"""
raise NameError("Hi There")

"""The Sole argument to raise indicates the exception to be raised. This must be either an exception instance of 
exception class (a class that derives from BaseException, such as Exception or one of its subclasses).
If an exception class is passed, it will be implicitly instantiated by calling its constructor with no arguments"""

raise ValueError #Shorthand for 'raise ValueError()'

"""if you need to determinate whether an exception was raised but don't intend to handle it, a simpler form of
the raise statement allows you to be re-raise the exception"""
try:
    raise NameError('Hi There')
except NameError:
    print('An Exception flew by!')
    raise

