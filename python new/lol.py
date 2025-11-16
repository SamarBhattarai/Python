import os

string = os.getcwd()
print(string)

path = "D:\Python\Python\python new"
os.chdir(path)
print(os.getcwd())

if not os.path.exists("practice"):
    os.mkdir("practice")

