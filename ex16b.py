from sys import argv
script, myfile = argv
refile = open(myfile)

print(refile.read())
refile.close()

