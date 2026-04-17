"""
Calculate Factorial 
THe next example involves the mathematical concept of factorial
the Factorial of a positive integer n , denotated as n!, is defined as follows:

                n! = n * 1 * 2 ... * n
                
in the words, n! is the product of all integers from 1 to n, inclusive.

                1             for n = 0 or n = 1 
           n! = 
                n x ( n -1 )! for n > 2          

as with the example shown above, there are base cases that are solvable without recursion.
The more complicated cases are reductive, meaning that they reduce to one of the base cases:

The base cases (n = 0 or n = 1) are solvable without recursion.
for values of n greater than 1, n! is defined in terms of (n - 1)!, so the recursive solution
progressively approaches the base case."""

#Define a Python factorial function

def factorial(n):
    print(f"factorial({n}) called with n = {n} ")
    return_value = 1 if n <= 1 else n * factorial(n - 1)
    print(f"returning {return_value} for factorial({n})")
    return return_value

print(factorial(10))

"""notice how all the recursive calls stack up. the function gets called with n = 4, 3, 2 and 1
in succession before any of the calls return. Finally, when n is 1, the problem can be solved without any 
more recursion. then each of the stack-up recursive calls uniwnds back ou, returning 1, 2, 6 and finally 24 from the outermost call

recursion ins't necessary here. You could implement factorial() iteratively using a for loop
"""
def facttorial(m):
    return_value = 1
    for i in range(2, m + 1):
        return_value *= i
    return return_value

facttorial(4)