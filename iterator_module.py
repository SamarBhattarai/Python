import itertools
from itertools import count

a = count(start = 5, step = 5)
print(type(a))
for i in a:
    if i < 20:
        print(i)