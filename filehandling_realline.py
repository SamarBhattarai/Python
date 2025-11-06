with open("hello3.txt", "r") as f:
    while True:
        line = f.readline()
        print(line)
        if not line:
            print(line, type(line))
            break