with open("hello.txt", "rb") as f:
    print(type(f))
    bytes = f.read()
    print(type(bytes))
    print(bytes)

    for b in bytes:
        print(b)

    for b in bytes:
        print(bin(b))

    text = bytes.decode("utf-8") # Manually decoding bytes to string.
    print(type(text)) # It provides < class "str" >
    print(text)