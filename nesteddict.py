info = {
    "name" : "Rajesh",
    "age" : 23,
    "subjects" : { #nested dictionary
        "phy" : 34,
        "chem" : 23,
        "maths" : 56
    },
    "roll_no" : 23
}
print(info["name"])
print(info["subjects"]["chem"])
print(len(list(info.keys())))
print(list(info.values())) #thus it shows that we can also store dictionary inside list and list inside dictionary
print(list(info.items())) #we can also store tuples inside of lists
pairs = list(info.items())
print(pairs[0])