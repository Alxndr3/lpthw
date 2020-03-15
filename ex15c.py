from sys import argv
script, filename = argv
content =  open(filename) 
print(content.readline())
content.close()
