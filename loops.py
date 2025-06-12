# i = 1
# while i <= 5:
#     print("Hello")
#     i += 1
hello = (1, 4, 9, 25, 36, 49, 64, 81, 100)
print(len(hello))
x = int(input("Enter the number you want to search.")) # important step typecasting
i = 0
while i < len(hello):
    if(hello[i] == x):
        print("Found at index", i)
    else:
        print("finding")
    i += 1 # very very important step
    # learn about break and continue
