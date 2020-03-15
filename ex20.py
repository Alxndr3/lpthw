from sys import argv

# the script is run with a file as argument via terminal ex. #python3.7 ex20.py any_file.txt
script, input_file = argv

# this function reads the content of the file passed once through the console ex. python3.7 ex20.py my_file.txt
def print_all(f):
    print(f.read())

# this function goes to the first bit of the file
def rewind(f):
        f.seek(0)

# the line number line_count is read is read and printed from the f file with the method .readline
def print_a_line(line_count, f):
    print(line_count, f.readline())

# the variable current_file receives the content of inpu_file passed prieviously through the argv
current_file = open(input_file)

print("First let's print whole file:\n")

# the content of current file is read and printed through the function print_all
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

# this calls the current_file vireable wich has the content of the open file and seeks to the line 0
rewind(current_file)

print("Lets's print three lines:")

# the functin print_a_line is calles with the value 1 for the current line
current_line = 1
print_a_line(current_line, current_file)

# now current_line variable wich is assigned with value 1 is reasigned with its value 1 + 1
current_line = current_line + 1
# the function print_a_line is called printing the current_line 1 from the current_file 
print_a_line(current_line, current_file)

# now current_line variable wich is assigned with value 2 is reasigned with its value 2 + 1
current_line = current_line + 1
print_a_line(current_line, current_file)

