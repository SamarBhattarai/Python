class Employee:
    def __init__(self, name):
        self.name = name

    def __len__(self):
        i = 0
        for _ in self.name:
            i += 1
        return i

    def __str__(self):
        return f"The name of the employee is {self.name}"
    
    def __call__(self, number): # The call method allows the instance of the class to be used as
                                #  if it were a function
        if number > 9:
            return f"Double digit"
        else:
            return f"Single digit"
    
print(f"{__name__}")

if __name__ == "__main__":
    obj = Employee("Harry")
    print(obj.name)
    print(len(obj))
    print(obj)
    print(str(obj))
    # obj(90) It will not show the result as we have returned from def __call__() method
    # if instead of returning we have had printed in the def __call__() method if would have shown
    # i.e def __call__(self, number):
            # if number > 9:
                # print("Double digit")

    print(obj(90))