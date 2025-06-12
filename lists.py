# list is a datatype as array
# indexing is available in list
# in lists we can store elements of different types together i.e string integer float etc.
# strings in python is immutable that is only access at a certain index is allowed while change is not allowed
# but lists in python are mutable that is both access and change at a certain index is allowed

student =["Rajesh", "Poland", 1]
print(student)
student[2] = 1.5 # mutable
print(student)
# List of multiple-dictionaries
people = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "San Francisco"},
    {"name": "Charlie", "age": 35, "city": "Los Angeles"}
]

# Accessing the list and dictionaries
for person in people:
    print(f"Name: {person['name']}, Age: {person['age']}, City: {person['city']}")
