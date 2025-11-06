with open("marks.txt", "r") as f:
    j = 0
    subject = ["Science", "Maths", "Nepali"]
    while True:
        line = f.readline()
        j = j + 1
        if not line:
            break
        # m1 = int(line.split(",")[0]) # To convert to integer we use typecasting.
        # m2 = int(line.split(",")[1]) # To convert to integer we use typecasting.
        # m3 = int(line.split(",")[2]) # To convert to integer we use typecasting.
        # Instead of above code m1, m2 and m3 we can use below code.
        m = line.split(",") # It creates a list such as m = ["m1", "m2", "m3"]

        # Using for loop to display marks of each student.
        for i in range(3):
            print(f"Marks of student{j} in {subject[i]} is {m[i]}")
          
    
    