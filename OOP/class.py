"""How do we define a class in python
in python classes can be defined by using the class keyord followed by a name and a colon.
Then you use. __init__() to declare which attributes each instance of the class should have:"""

class Employee:
    cargo = "diretoria"
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        
        
        
        
"""Another way to do this is to represent each employee as a list: """
kirk = ["James kirk", 34, "Captain", 2265]
spock = ["Spock", 35, "Science officer", 2254]
mccoy = ["Leonard Mccoy","Chief Medical officer",2266]

"""There are a number of issues with this approach.
first, it can make larger code files more difficult to manage. if we reference kirk[0] several lines
away from where declarated the kirk list, will we remember thet the element with index 0
is the employee's name?

Second, it can introduce errors if employees don't have the same number of elements in their respective lists. 
In the mccoy list above, the age is missing so mccoy[1] will return (Chief Medical Officer) instead of Dr. McCoy's age

A greater way to make this type of code more manageable and more maintainable is to use CLASSES """

kirk1 = Employee("Kirk", 24, 1900)
print(kirk1.salary)
print(kirk1.cargo)

mccoy1 = Employee("Mccoy", 35, 1540)
mccoy1.cargo = "Faxina"
print(mccoy1.cargo)
