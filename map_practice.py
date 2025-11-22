a = [1, 2, 3, 4, 5 ]

def add(one):
    return one + 10

# map(function, iterable1, iterable2, ...) 

result = map(add, a)
print(result)
print(type(result))
print(list(result))

def multwoiterable(a, b):
    return a * b

result_2 = map(multwoiterable, a, a)
print("\n")
print(result_2)
print(type(result_2))
print(list(result_2))

# Using map() function in the most common way that is, by using lambda function.

result_3 = map(lambda x, y: x + y, a, a)
print("\n")
print(result_3)
print(type(result_3))
print(list(result_3))