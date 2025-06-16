# Using variable index

marks = [12,23,34,13,34]
# index = 0
# for mark in marks:
#     print(f"{index} {mark}")
#     index += 1

#Now using enumerate() function
print(list(enumerate(marks)))
for index, mark in enumerate(marks):
    print(f"{index} {mark}")