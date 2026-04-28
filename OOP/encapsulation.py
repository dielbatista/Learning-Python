"""Encapsulation is often described as one of the four pillars of OOP.
in simple ters, it's about building data (attributes) and methods that wor on that data
into a single unit (a class) and restricting direct access to some of the object's components

In Python we dont have strict private keywords like Java or C++. Instead, we use naming conventions
to tell other developers how they should treat specific data.


1 - THE "Social contract" of Python:

Access level           convention             Meaning
-------------          ------------           -------------
Public                 <none>                 Can be accessed from anywhere
Protected              _<name>                Should only be accessed from within the class and its subclasses
Private                __<name>               Should only be accessed from within the class """

"""2 - Pratical Example: A smart home thermostat 

Without Encapsulation anyone could set your house temperature to 1,000°C,
with encapsulation, we add a "filter" """

class Thermostat:
    def __init__(self, temp):
        self.__brand = "EcoTemp" #Proteced attribute
        self.__currrent_temp = temp #Private
        
    def get_temperature(self):
        return f"The current temp is {self.__currrent_temp}°C"
    
    def set_temperature(self, new_temp):
        if 10 <= new_temp <= 35:
            self.__currrent_temp = new_temp
            print(f"Temperature set to  {new_temp}°C")
        else:
            print("Temperature out of range. Please set a temperature between 10 and 35°C.")
            
my_ac = Thermostat(22)
print(my_ac.get_temperature())
my_ac.set_temperature(30)


"""Pythonic Way: @property Decorator"""

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.__salary = salary
        
    @property
    def salary(self):
        #The Getter
        return self.__salary
    
    @salary.setter
    def salary(self, value):
        #The setter
        if value > 0:
            self.__salary = value
        else:
            raise ValueError("Salary must be a positive number.")
            
staff = Employee("Alice", 30, 50000)
print(staff.salary)  # Accessing the salary using the getter
staff.salary = 55000  # Updating the salary using the setter
print(staff.salary)  # Accessing the updated salary using the getter    