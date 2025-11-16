import os
import shutil

print(os.getcwd())
os.chdir(r"D:\Python\Python\python new")
print(os.getcwd())

folders = ["pizza", "steak"]
sub_folders = ["train", "test"]

for folder in folders:
    for sub_folder in sub_folders:
        os.makedirs(rf"D:\Python\Python\python new\food\{folder}\{sub_folder}", exist_ok = True)


### Another Method to do this:###
# import os
# import shutil

# print(os.getcwd())
# os.chdir(r"D:\Python\Python\python new")
# path = os.getcwd()

# folders = ["pizza", "steak"]
# sub_folders = ["train", "test"]

# for folder in folders:
#     for sub_folder in sub_folders:
#         main_path = os.path.join(path, "food", folder, sub_folder)
#         os.makedirs(main_path, exist_ok = True)


