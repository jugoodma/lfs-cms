import re

def main():
    while True:
        command = input("Enter a command (/help for help): ")
        command = command.lower()
        if command =="exit" or command == "quit":
            break;
        if command == "/help":
            printHelp()
#        else:
#            for s in command:
#                if not re.match('^[a-z0-9 -]* $',s):
#                    print("invalid command")
#                    break;
        if re.match('^add *',command):
            if add(command[4:]) == 0:
                break;
        elif re.match('^set *',command):
            if seta(command[4:]) == 0:
                break;
        elif re.match('^insert*',command):
            insert(command[6:])
            
def add(command):
    name = False
    tag = command.split(' ',1)[0]
    if "-" in tag:
        ID = tag.split('-',1)[1]
        value = command[len(tag):]
        tag = tag.split('-',1)[0]
        name = True
    else:
        value = command[len(tag):]
    f = open("output.html","r+")
    line = next(f)
    output = line;
    while not "</body>" in line:
        output += line
        line = next(f)
    if tag == "paragraph":
        if name:
            output+='\t\t<p id="'+ID+'">\n\t\t\t' + value + "\n\t\t</p>\n"
        else:
            output+="\t\t<p>\n\t\t\t" + value + "\n\t\t</p>\n"
    elif tag == "header":
        if name:
            output+='\t\t<header id="'+ID+'">\n\t\t\t' + value + "\n\t\t</header>\n"
        else:
            output+="\t\t<header>\n\t\t\t" + value + "\n\t\t</header>\n"
    else:
        return 0
    output+="\t</body>\n</html>"
    f.close()
    f = open("output.html","w+")
    f.write(output)
    f.close()

def seta(command):
    name = False
    tag = command.split(' ',1)[0]
    if "-" in tag:
        ID = tag.split('-',1)[0]
        value = command[len(tag):]
        tag = tag.split('-',1)[1]
        name = True
    else:
        value = command[len(tag):]
    f = open("output.css","r+")
    line = next(f)
    output = ""
    added = False
    count = len(line)
    if not name:
        while not "}" in line:
            if tag in line:
                output+="\t"+tag+":"+value+"\n"
                line = next(f)
                count+=len(line)
                added = True
            if "}" in line:
                break;
            output += line
            try:
                line = next(f)
                count += len(line)
            except:
                break;
        if not added:
            output+="\t"+tag+":"+value+"\n}\n"
        else:
            output+="}\n"
        f.seek(count)
        for line in f:
            output+=line
    else:
        while not ID+" {" in line:
            output+=line
            line = next(f)
            count += len(line)
        while not "}" in line:
            if tag in line:
                output+="\t"+tag+":"+value+"\n"
                line = next(f)
                count+=len(line)
                added = True
            if "}" in line:
                break;
            output += line
            try:
                line = next(f)
                count += len(line)
            except:
                break;
        if not added:
            output+="\t"+tag+":"+value+"\n}\n"
        else:
            output+="}\n"
        f.seek(count)
        for line in f:
            output+=line
    f.close()
    f = open("output.css","w+")
    f.write(output)
    f.close()

def insert(command):
    ego = False
    if "-" in command:
        where = command.split(' ',1)[0]
        where = where[1:]
        command = command[len(where)+1:]
    else:
        where = "before"
        command = command[1:]
    if ":" in command.split(' ',1)[0]:
        ID = command.split(':',1)[0]
        command = command[len(ID)+1:]
        ego = True
    what = command.split(' ',1)[0]
    value = command[len(what)+1:]
    f = open("output.html","r+")
    line = next(f)
    output = ""
    print(where)
    if where == "before":
        if ego:
            while not 'id="'+ID in line:
                output+=line
                count = len(line)
                line = next(f)
            if what == "paragraph":
                output+='\t\t<p id="'+ID+'">\n\t\t\t' + value + "\n\t\t</p>\n"
            elif what == "header":
                output+='\t\t<header id="'+ID+'">\n\t\t\t' + value + "\n\t\t</header>\n"
            else:
                return 0
            output+=line
            count = len(line)
            f.seek(count)
            for line in f:
                output+=line
        else:
            for i, l in enumerate(f):
                pass
            i-=1
            f.seek(i)
            line = next(f)
            print(line)
            search = line.split('<',1)[0]
            i -=1
            while not search in line:
                line = f.seek(i)
                i -=1
            f.seek(0)
            for c in range(i):
                f.seek(c)
                output += next(f)
            if what == "paragraph":
                output+='\t\t<p>\n\t\t\t' + value + "\n\t\t</p>\n"
            elif what == "header":
                output+='\t\t<header>\n\t\t\t' + value + "\n\t\t</header>\n"
            else:
                return 0
            f.seek(i)
            for line in f:
                output+=line
        f.close()
        f = open("output.html","w+")
        f.write(output)
        f.close()
    elif where == "after":
        if not ego:
            add(what+" "+value)
        else:
            while not 'id="'+ID in line:
                output+=line
                count = len(line)
                line = next(f)
            search = line.split('<',1)[0]
            output+=line
            while not search in line:
                output+=line
                count = len(line)
                line = next(f)
            if what == "paragraph":
                output+='\t\t<p id="'+ID+'">\n\t\t\t' + value + "\n\t\t</p>\n"
            elif what == "header":
                output+='\t\t<header id="'+ID+'">\n\t\t\t' + value + "\n\t\t</header>\n"
            else:
                return 0
            output+=line
            count = len(line)
            f.seek(count)
            for line in f:
                output+=line
            f.close()
            f = open("output.html","w+")
            f.write(output)
            f.close()
    else:
        print("invalid command")
    
def makeGeneric():
    f = open("output.html","w+")
    html = '<!DOCTYPE html>\n<html lang="en">\n\t<head>\n\t\t<meta charset="UTF-8">\n\t\t<link type="text/css" rel="stylesheet" href="page.css"/>\n\t\t<title>Title Page</title>\n\t</head>\n\t<body>\n\t\t<section>\n\t\t\t<h1>\n\t\t\t\t<strong>This is A Title</strong>\n\t\t\t</h1>\n\t\t<section>\n\t\t\tLorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sed euismod risus. Aenean at imperdiet nulla. Vestibulum finibus ligula sem, at sollicitudin metus commodo nec. Vestibulum sagittis turpis massa, placerat pellentesque eros pretium non. In consectetur vestibulum semper. Proin eget sapien consectetur, faucibus leo et, condimentum nunc. Cras ultricies malesuada scelerisque. Pellentesque finibus scelerisque bibendum. Aliquam sollicitudin nisl purus, vel porta massa porttitor a. Donec viverra tempor auctor.\n\t\t</section>\n\t</body>\n</html>'
    f.write(html)
    f.close()
    f = open("output.css","w+")
    css = "body {\n\tfont-family: 'Raleway', sans-serif;\n}"
    f.write(css)
    f.close()

def printHelp():
    f = open("help.txt","r+")
    out="\n"
    for line in f:
        out += line
    print(out)
main()
