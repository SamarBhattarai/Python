class Engine:
    def __init__(self, horsepower):# Making Constructor
        self.horsepower = horsepower # Public attribute, can be accessed outside of the class.

class Car:
    def __init__(self, brand, engine):
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
car2 = Car("Ferrari", engine = "V8")
print(car2.brand)
print(car2.engine)