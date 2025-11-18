import os
import pathlib

cwd = os.getcwd()
print(cwd)

p = pathlib.Path(cwd)
print(p)
print(type(p)) # <class 'pathlib.WindowsPath'>
print(p.exists())
print(f"{p} is a file = {p.is_file()}")
print(f"{p} is a folder/directory = {p.is_dir()}")

new_path  = p / "python new"
print(new_path)
print(type(new_path)) # <class 'pathlib.WindowsPath'>
print(new_path.exists())
print(type(p.exists())) # <class 'bool'>
print(type(p.is_file()))
print(type(p.is_dir()))
print(f"{new_path} is a file = {new_path.is_file()}")
print(f"{new_path} is a folder/directory = {new_path.is_dir()}")

for file in new_path.iterdir():
    print(file)
print(new_path.iterdir())
print(type(new_path.iterdir()))

