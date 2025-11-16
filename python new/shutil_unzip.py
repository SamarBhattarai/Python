import os
import shutil

# Using shutil module to first unzip or unarchive our food.zip file/ folder.

string = os.getcwd()
print(string)

# Changing the working directory from current working directory.
os.chdir("D:/")

zip_path = r"D:\food-101.zip"

destination_path = r"D:\food_unzipped"

if not os.path.exists(destination_path):
    os.mkdir(destination_path) # if not present, creating a new directory.

# Extracting the entire zip into food_unzipped folder.
shutil.unpack_archive(zip_path, destination_path)

print("Unzipped successfully.")



