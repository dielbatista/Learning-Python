"""Even if a statement or expression is syntactically correct,
it may cause an error when an attempt is made to execute it. Errores detected during exeution are called
exceptioons and are not uncondtionally fatal."""

>>> 10 * (1/0)
Traceback (most recent call last)::
    File "<stdin>", line 1, in <module>
    10 * (1/0)
ZeroDivisionError: division by zero
>>> 4 + spam*3
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    4 + spam*3
    
NameError: name 'spam' is not defined
>>> '2' + 2
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    '2' + 2
TypeError: can only concatenate str (not "int") to str



