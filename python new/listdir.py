import os

# Getting the current working directory.
print(os.getcwd())

var_list = os.listdir("data")
print(type(var_list))
print(var_list)

# Using for loop to get the files, directories inside of the sub-directories present in data folder.
for folder in var_list:
    print(folder)
    print(os.listdir(f"data/{folder}"))