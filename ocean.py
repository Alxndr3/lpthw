oceans = ["Pacific", "Atlantic", "Indian", "Southern", "Arctic"]

with open("oceans.txt", "w") as f:
    for ocean in oceans:
        f.write(ocean)
        f.write("\n")

