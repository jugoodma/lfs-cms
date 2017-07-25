## init.py
#
# About
#  lfs-cms initializer
#  this script instantiates everything for lfs-cms
#
#  if you're seeing this script on the front-end, you probably
#  don't have mod_wsgi installed/configured properly...
#
# Author
#  written by Clifford Bakalian and Justin Goodman
#
##

# imports
from writer import * #import the writer.py functions
from config import * #import the config.py class/func.
import re #hmmm
import cgi #hmmm

# the main function
def main():
    GLOBE = Config()
    createFile("index.html", GLOBE.URIPATH)
    writeFile("index.html", GLOBE.URIPATH, "<p>TEST</p>")
# and finally, start :D
main()
