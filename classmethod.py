# self = object
# Example of class method

class Student:
    name = "Anonymous"

    @classmethod
    def change_name(cls, name):
        cls.name = name
        return cls.name

s1 = Student()
print(s1.name)
print(Student.name)
print(s1.change_name("rajesh"))

# basically there are three types of method
# 1) Static method- that can't change attribute of neither class nor object
# 2) Class method- for changing class attribute (cls)
# 3) Instance method- for object (self)