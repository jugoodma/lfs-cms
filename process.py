import re
incommand = input("Input: ")
outstring =""
pattern = '^[a-z0-9]$'
f = open("output.txt","w+")
for s in incommand:
    if re.match(pattern, s):
        outstring+= s
f.write(outstring)
f.close()
