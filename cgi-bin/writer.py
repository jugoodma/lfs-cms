## writer.py
#
# About
#  lfs-cms html document write engine
#  this is basically just a html file-writer library
#
# Author
#  written by Clifford Bakalian and Justin Goodman
#
##

# imports
import os #hmmm
import re #hmmm
import cgi #hmmm

# fileName = file name string
# path = path to put the created file
def createFile(fileName, path):
    htmlFile = open(path + fileName, 'w')
    htmlFile.write("")
    htmlFile.close()

# fileName = file name string
# path = path where fileName is located
# data = data string to write to file
def writeFile(fileName, path, data):
    htmlFile = open(path + fileName, 'w')
    htmlFile.write(data)
    htmlFile.close()
