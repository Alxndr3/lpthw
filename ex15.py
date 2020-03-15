# The following line imports argv from sys.
from sys import argv

script, filename = argv

# The content of filename which was provide in the above filename variable through argv wich is given in the command line right after the program name (.py file).
txt = open(filename)

# A simple message is printed with the script's name.
print (f"Here's your file {filename}")
# In this case the very new thing named function is used, in this situation the function read will read the content of the variable txt wich in turn will be printed by print.
print(txt.read())
txt.close()


print("Type the filename again:")
# In this situation the script's name will be assign to the variable file_again interactively.
file_again = input("> ")

# Wich in turn the file's content will be assigned to the variable txt_agian.
txt_again = open(file_again)

# The content of the txt_again variablen will be read and printed.
print(txt_again.read())

