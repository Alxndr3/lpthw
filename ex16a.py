from sys import argv
# filename is the variable wich will be the name for our bran new file.
script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
# target is the variable where the content of our file filename will be written
target = open(filename, 'w')

print("Truncating the file. Goodby!")
# The truncate function erases the file
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1:")
line2 = input("line 2:")
line3 = input("line 3:")

print ("I'm going to write these to the file.")

target.write(line1)
# "/n" inserts a new line, without it line1, line2 and line3 would be wirtten in the same line.
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
# target.close closes our file.
target.close()
