# This is a decorator function: it takes another function as input (f)
# and returns a modified (wrapped) version of it.
def decorator(f):
    def wrapper():
        print("Starting")  
        f()               
        print("Completed") 
    return wrapper  

# this is a simple function to demonstrate the decorator
def hello():
    print("Executing") 

# manually applying the decorator:
# hello1 now refers to the wrapper function created by decorator(hello)
hello1 = decorator(hello)

# calling hello1 will run the wrapper, which:
# - prints "Starting"
# - calls hello() (which prints "Executing")
# - prints "Completed"
hello1() #calling hello1
