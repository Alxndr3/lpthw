from sys import argv
from os.path import exists

script, from_file, to_file = argv; in_file = open(from_file); indata = in_file.read(); out_file = open(to_file, 'w'); out_file.write(indata); print("alright, all done."); out_file.close(); in_file.close()
