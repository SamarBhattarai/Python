with open("hello.txt", "r") as f: # Here, using with keyword no need to do f.close(). It automatically does so.
    print(f)
    print(type(f))
    txt = f.read()
    print(txt)
    print(type(txt))