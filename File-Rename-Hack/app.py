import os
import sys

path_of_the_dir = sys.argv[1]
filename_we_want = sys.argv[2]

path = path_of_the_dir
c = 0
for filename in os.listdir(path):
	fileN = os.path.join(path,filename)
	fileToRename = os.path.join(path, filename_we_want)
	os.rename(fileN, fileToRename + str(c) + ".png")
	c += 1
