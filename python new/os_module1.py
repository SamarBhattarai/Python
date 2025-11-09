import os

# Getting current working directory.
str = os.getcwd()
print(type(str))
print(str)

if not os.path.exists("data"):
    os.mkdir("data")

# # for i in range(1, 10):
#     os.mkdir(f"data/Day{i}")


# # Changing the name of the sub-directories.
# for i in range(1, 10):
#     os.rename(f"data/Day{i}", f"data/Day {i}")

