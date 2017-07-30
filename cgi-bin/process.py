#!/usr/bin/python3
# -*- coding: UTF-8 -*-# enable debugging
##
#
##
import re #eeeeeeeeeeeeeeee
import cgi
import cgitb
from writer import *
from config import *
cgitb.enable()
print("Content-Type: text/html;charset=utf-8")
print()
print("Success")

data = cgi.FieldStorage() # <input type="text" name="userInput">
# data = input("Input: ")
outstring =""
pattern = '^[a-z0-9]$'
# clear the output.txt everytime, and whenever we present the html form 
# to the user we will just copy the output.txt and put it in the form field 
# (that way they're just editing their original text every time and not 
# just a blank field)

createFile("output.txt", "../")
f = open("../output.txt","w+")
#for s in data["input"].value:
#    if re.match(pattern, s):
#        outstring+= s
outstring+=data["input"].value
f.write(outstring)
f.close()
