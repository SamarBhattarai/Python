# used to store key : value pairs
# they are unordered(no index), mutable, and don't allow duplicate keys
# inside dictionary we can also store lists and tuples

info = {
    "name" : "Rajesh",
    "age" : 23,
    "marks" : [56, 78, 89],
    69 : True,
    6.9 : False,
    ("class", "rollno") :[12, 34] #tuple can also be key but list and dictionary can't be keys

}
print(info["age"])
info["age"] = 24 
info["surname"] = "hitang"
null_dict = {} #null dictionary
print(info)
null_dict["NAME"] = "SAM"
print(null_dict)
