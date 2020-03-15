#This is another way to open files.
filetoopen = str(input("Type down the file's name: "))
with open(filetoopen) as fobj:
	bio = fobj.read()
print(bio)
