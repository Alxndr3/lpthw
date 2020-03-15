text = str(input("Insert the wanted text"))
with open("oceans.txt", "a") as f:
    print(text, file=f)
    print("This is your text", file=f)
