class Engine:
    def __init__ (self, type, number): # Making a constructor
        self.engine_type = type # Public attribute
        self.__engine_number = number # Private attribute --> Two underscores
                                      # Protected attribute --> One underscore

class Car:
    def __init__ (self, brand, engine):
        self.brand = brand
        self.engine = engine # Attribute is an object of another class
        
# Creating an Engine object
engine1 = Engine(type = "V8", number = 123)

# Pass it into a car object
car1 = Car("Ferrari", engine1)

print(car1.brand)
print(car1.engine.engine_type)
# print(car1.engine.__engine_number) Private so it can be accessed.
# But you can still reach it if you know the mangled name.

### BEST PRACITCE --> USE GETTERS AND SETTERS ###
# Instead of directly accessing private attributes, use methods.