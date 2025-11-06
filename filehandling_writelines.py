with open("writelines.txt", "w") as f:
    lines = ["line1\n", "line2\n", "line3\n"]
    f.writelines(lines)