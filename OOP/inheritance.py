"""Inheritance is the process by which one class takes on the attributes and methods of another.
Newly formed classes are called child classes, and the classes that you derive child classes from are calle parent classes """

from instance_methods import Dog


class rottweiler(Dog):
    pass

rex = rottweiler("Rex", 7, "rottweiler")
print(rex)
"""on The above class rottweiler is the child class and Dog is the parent class. 
the child class inherits all the attributes and methods of the parent class. 
In this case, the rottweiler class inherits the __init__ method and the __str__ method from the Dog class.
Therefore, when we create an instance of the rottweiler class and print it, 
it uses the __str__ method from the Dog class to return a
string representation of the object. """
print(rex.species)


"""Now imagine you decid to learn a second language, like German. in this case, you've extended your attributes because 
you've added an attribute your parents don't have:"""

class Parent:
    speaks = "english"
    
class Child(Parent):
    def __init__(self):
        super().__init__()
        self.speaks = Parent.speaks + " and german"

child1 = Child()
print(child1.speaks)