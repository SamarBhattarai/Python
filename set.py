# set is a collection of unordered items.
# each element in the set must be unique and immutable.
# NOTE : sets are mutable but the elements in it must be immutable.
# we can't store list and dictionary inside set as they are mutable.

collection = {1, 2, 2, 2, 3, "rajesh", "rajesh"}
print(collection) #set ignores duplicate values
print(type(collection))
print(len(collection))

soviyat = {} # it is recognised as empty dictionary
soviyat1 = set() # it is now recognised as empty set

print(type(soviyat))
print(type(soviyat1))

collection.add(7) #we can add tuple as tuple will be a immutabe element
# but we can't add list and dictionary as they, when added,  will be immutable element.
print(collection)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.union(set2)
print(set3)
set4 = set1.intersection(set2)
print(set4)