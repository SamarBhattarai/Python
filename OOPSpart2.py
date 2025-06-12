# del keyword
class Account:
    def __init__(self, acc_id, acc_pass):
        self.acc_id = acc_id
        self.__acc_pass = acc_pass # for private we use "__" infront of properties and methods
        print("Account Created Successfully.")

    def show_pass(self):
        return self.__acc_pass
        
rajesh = Account(101, "abcde")
print(rajesh.acc_id)
# print(rajesh.__acc_pass) not valid as __acc_pass is made private
print(rajesh.show_pass())

# INHERITANCE
# super() method is used to access methods of parent class.