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
    return 1 if n <= 1 else n * factorial(n - 1)

print(factorial(4))