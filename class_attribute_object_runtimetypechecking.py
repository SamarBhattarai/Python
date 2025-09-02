class Engine:
    def __init__(self, horsepower):# Making Constructor
        self.horsepower = horsepower # Public attribute, can be accessed outside of the class.

"""If you want runtime enforcement
You must add a check inside your class:"""

class Car:
    def __init__(self, brand : str, engine : Engine):
        if not isinstance(engine, Engine):
            raise TypeError("engine must be an Engine object")
        self.brand = brand # Public attribute
        self.engine = engine # Public attribute (object)

# Creating an object of Engine class
engine1 = Engine(1700)

# Creating an object of Car class
car1 = Car("Toyota", engine1)

# Accessing the values of the attributes
print(engine1.horsepower)
print(car1.brand)
print(car1.engine.horsepower)


### BUT WHAT HAPPENS IF I DO THIS ###
car2 = Car("Ferrari", engine = engine1)
print(car2.brand)
print(car2.engine) 
print(car2.engine.horsepower)