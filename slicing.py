# str[starting_index : ending_index] where starting index is included but ending index is not included.
# example of slicing is given below

str = "utech_college"
print(str[0 : 5])
print(str[6 :]) # it is same as print(str[6 : len(str)])
print(str[6 : len(str)])
print(str[ : 5]) # here 0 is filled