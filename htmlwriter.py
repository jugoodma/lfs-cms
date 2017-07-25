import re

def main():
    while True:
        command = input("Enter a command (/help for help): ")
        command = command.lower()
        if command =="done" or command == "quit":
            break;
        if command == "/help":
            print("help")
        else:
            for s in command:
                if not re.match('^[a-z0-9- ]*$',s):
                    print("invalid command")
                    break;
        if re.match('^add *',command):
            if add(command[4:]) == 0:
                break;
        elif re.match('^set *',command):
            if set(command[4:]) == 0:
                break;

def add(command):
    f = open("output.txt","a+")
    tag = command.split(' ',1)[0]
    if tag == "paragraph":
        f.write("<p>" + command[len(tag):] + "</p>")
    elif tag == "header":
        f.write("<header>" + command[len(tag):] + "</header>")
    else:
        print("invalid command")
        f.close()
        return 0
    f.write("\n")
    f.close()
    return 1;

def set(command):
    f = open("out.css","w+")
    css = ""
    temp = command.split(' ',1)[0]
    for line in f:
        if temp in line:
            css += temp + ":" + command[len(temp):])
        else:
            css+=line
    f.write(css)
    f.close()
    
main()
