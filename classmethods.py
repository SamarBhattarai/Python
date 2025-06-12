class Student:
    college_name = "Utech"
    
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("Constructor created")
    
    @staticmethod # works at class level and no need to use self keyword
    def hello():
        print("Hello")

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi", self.name, "your average is :", sum/3)

s1 = Student("Rajesh", [10, 20, 30])
Student.hello()
print(Student.college_name)
s1.get_avg()