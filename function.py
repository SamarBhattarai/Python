def calc_sum(a, b):
    return a + b

print(calc_sum(2, 3))

print("Rajesh", end=" ")
print("Hitang")

# look youtube for default and non-default arguments

list = ["ironman", "thor", "antman", "wanda", "vision", "hulk", "falcon"]

def print_list(a):
    for item in a:
        print(item, end=" ")

print_list(list)

# for printing factorial
def fact(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    print("The factorial of ",n , "is :", res)

a = int(input("Enter the number you want factorial of:"))
fact(a)