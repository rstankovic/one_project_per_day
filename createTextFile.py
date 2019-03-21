import time as t
import os
import sys
import pathlib

'''
This script creates a text file to a destination chosenDirectory
that includes the names of all the files
in a given directory
'''

def iterateDir(path, f):
    for currentFile in path.iterdir():
        if currentFile.is_dir():
            currentName = os.path.basename(str(currentFile))
            f.write("\n FILES WITHIN %s \n" %currentName)
            iterateDir(currentFile, f)
            f.write("EXITING %s \n \n" %currentName)
        else:
            currentName = os.path.basename(str(currentFile))
            f.write("%s \n" %currentName)

def createFile(dest,chosenDirectory, filename):
    date = t.localtime(t.time())
    name = "%d_%d_%d%s.txt" %(date[1],date[2],date[0],filename)
    chooseDir = pathlib.Path(chosenDirectory)
    if not(os.path.isfile(dest + name)):
        f = open(dest + name, "w")
        currentName = os.path.basename(str(chooseDir))
        f.write("FILES WITHIN %s \n \n \n" %currentName)
        for currentFile in chooseDir.iterdir():
            if currentFile.is_dir():
                iterateDir(currentFile, f)
            currentName = os.path.basename(str(currentFile))
            f.write("%s \n" %currentName)
        currentName = os.path.basename(str(chooseDir))
        f.write("\n EXITING %s \n \n" %currentName)
        f.close()

if __name__ == '__main__':
    createFile(sys.argv[1], sys.argv[2], sys.argv[3])
    raw_input('done!!')
