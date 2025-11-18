import os
import pathlib
from pathlib import Path

print(os.getcwd())
p = Path(r"D:\Python\Python\python new")
print(type(p))

for file in p.glob("*.py"):
    print(file)
    # print(type(file)) # <class 'pathlib.WindowsPath'>
