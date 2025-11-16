import os
import shutil
import random

print(os.getcwd())
os.chdir(r"D:\CNN-food\food\images")
base = os.getcwd()

foods = ["pizza", "steak"]
size = []

# Counting the size of number of files(only images) in our pizza and steak folder:
for food in foods:
    count = 0   # reset for each folder
    path = os.path.join(base, food)
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
           count = count + 1 
    size.append(count)    

print(size) # Here, we see that both pizza and steak folder have same no of files(images) i.e 1000

# Using random module
random.seed(42)
sub_folders = ["train", "test"]

# Picking random files
source_path = r"D:\CNN-food\food\images"
destination_path = r"D:\Python\Python\python new\food"
for food in foods:
    for sub_folder in sub_folders:
        copy_count = 80 if sub_folder == "train" else 20 # Single-line conditional expression (Ternary Operator)
        all_files = [f for f in os.listdir(os.path.join(source_path, food)) if os.path.isfile(os.path.join(source_path, food, f))]
        random_files = random.sample(all_files, copy_count)
        for file in random_files:
            source_file = rf"D:\CNN-food\food\images\{food}\{file}" # Note: we can also use os.path.join() functionality here.
            destination_file = rf"D:\Python\Python\python new\food\{food}\{sub_folder}\{file}" # Note: we can also use os.path.join() functionality here.
            shutil.copy2(source_file, destination_file)

print("Success")

