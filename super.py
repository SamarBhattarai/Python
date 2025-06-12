class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod # decorator
    def start():
        print("Car Started.")

    @staticmethod # decorator
    def stop():
        print("Car Stopped.")

class Toyota_car(Car): # it inherits the class Car.
    def __init__(self, name, type):
        self.name = name
        # self.type = type is for Toyota car itself not for the parent car.
        super().__init__(type) # now it is of parent class.
        
o1 = Toyota_car("Fortuner", "Petrol")
print(o1.name)
print(o1.type)