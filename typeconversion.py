# there are two types of conversion one is type conversion and one is type casting
# type conversion- here the python interpreter does conversion automatically for us.
# type casting- manually done by programmer

# example of implicit type conversion

s = 5
a = 10.5
sum = s + a #it does 5.0 + 10.5
print(sum)

# example of type casting

s = 10.25
c = int(s)
print(s)
print(c)
sam = 3.14
sam = str(sam) # we can convert number to sting type
print(type(sam))
