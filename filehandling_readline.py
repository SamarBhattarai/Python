with open("hello3.txt", "r") as f:
    line1 = f.readline()
    line2 = f.readline()
    line3 = f.readline()
    line4 = f.readline()
    line5 = f.readline()
   

    print(line1)
    print(line2)
    print(line3)
    print(line4)
   
if line4 == "":
    print("Line 4 is empty string.")

if line5 == "":
    print("Line 5 is empty string.")
