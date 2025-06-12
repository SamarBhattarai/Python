class Student:
    college_name = "GBS" #class attribute
    name = "Anonymous" 
    def __init__(self, fullname):
        print("Object created sucessfully.")
        print(self)
        self.name = fullname # here self.name is very much important

s1 = Student("Rajesh")
print(s1.name)
print(s1) # gives same output as print(self)
# The self parameter is a reference to the current instance of the class, and is used to access variables that 
# belongs to the class.

# There are default and parameterized constructors in python.
# precedence of object attribute is more tha class attribute under same name

print(Student.college_name)
print(Student.name)
print(s1.name)