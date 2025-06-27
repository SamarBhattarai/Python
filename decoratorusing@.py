def decorator(f):
    def wrapper():
        print("Starting")  
        f()               
        print("Completed") 
    return wrapper  

@decorator 
def hello():
    print("Executing")
    
# Python does hello = decorator(hello)
hello()