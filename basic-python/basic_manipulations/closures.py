"""A closure is a function that remembers, accesses, and uses variables from its enclosing
function, even after that outer function has finished executing, in other words, it's an innter
function that closes over the variables it needs from the outer function, keeping them alive
for later use."""


def function():
    value = 42
    def closure():
        print(f"The Value is: {value}!")
    return closure

reveal_number = function()
reveal_number()

"""In Pratice, closures have several cases. you can use closures to create stateful functions,
callbacks, decorators, factory functions and more"""

def generate_power(exponent):
    def power(base):
        return base ** exponent
    return power

square = generate_power(2)
print(square(4))

cube = generate_power(3)
print(cube(3))

print(cube(5))

"""In this example, the generate_power() function returns a closure. The inner function,
power(), uses its base argument and the exponent argument from the outer function to 
compute the specified power"""

"""Default Argument Values
if you assign a value to a given parameter in the deifinition of a function, then that value
becomes a default argument value. Parameters with a default value are option parameters, which
means that you can call the function without providing a concrete argument value because you can rely on the default value.
"""

def greet(name="world"):
    print(f"Hello, {name}!")
    
greet("Pythonista")