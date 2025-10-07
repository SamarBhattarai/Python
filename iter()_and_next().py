a = [1, 2, 3]
print(type(a)) # Output : <class 'list'>

# Using iter function to create iterator object
it = iter(a)
print(type(it)) # Output : <class 'list_iterator'>

# Using next() function
print(next(it))
print(next(it))
print(next(it))
# print(next(it)) # It raises StopIteration exception.

print(next(it, "End"))

# iter(callable, sentinel)

import random
for num in iter(lambda: random.randint(1, 10), 5):
    print(num)
# It repeatedly calls the function until it returns the sentinel value.
# Stops automatically when the random number equals 5.
# (no infinite loop!)