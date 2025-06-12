class Student:
    name = "Anonymous"

    def stu_name(self, name):
        self.__class__.name = name # or we can write Student.name = name to change class attribute 
        # as there are two types of attribute 1) class attribute 2) object attribute
        # NOTE: self.name = name won't change class attribute but a object attribute is created

s1 = Student()
s1.stu_name("Rajesh")
print(Student.name)
print(s1.name)

