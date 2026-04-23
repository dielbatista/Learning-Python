"""Inheritance is the process by which one class takes on the attributes and methods of another.
Newly formed classes are called child classes, and the classes that you derie child classes from are calle parent classes """

from instance_methods import Dog

class rottweiler(Dog):
    pass

rex = rottweiler("Rex", 7, "rottweiler")
print(rex)