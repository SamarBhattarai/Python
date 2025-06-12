f = open("demo.txt", "r") # we can also write rt but text is by default but we should write rb for binary 
data = f.read()
print(data)
print(type(data))

f = open("sample.txt", "w")
f.write("Hi there")
f.close

# look stack overflow, pointer is important
# with automatically closes the file for us and as is alias

with open("demo.txt", "r") as f:
    data = f.read()
    print(data)
    