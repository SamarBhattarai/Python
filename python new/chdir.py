import os

# Getting the current working directory.
string = os.getcwd()
print(string)

# Changing the path of working directory.
os.chdir("/Python")
print(os.getcwd())