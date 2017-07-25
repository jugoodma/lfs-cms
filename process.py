import re #eeeeeeeeeeeeeeee
import cgi

data = cgi.FieldStorage().getvalue('userInput') # <input type="text" name="userInput">
# data = input("Input: ")
outstring =""
pattern = '^[a-z0-9]$'

# clear the output.txt everytime, and whenever we present the html form 
# to the user we will just copy the output.txt and put it in the form field 
# (that way they're just editing their original text every time and not 
# just a blank field)

f = open("output.txt","w+")
for s in outstring:
    if re.match(pattern, s):
        outstring+= s
f.write(outstring)
f.close()
