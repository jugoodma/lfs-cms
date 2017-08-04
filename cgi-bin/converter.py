import os
def get_segments():
    f = open (os.path.dirname(__file__) + "/../output.txt","r")
    output = ""
    group = []
    next(f)
    next(f)
    count = 1
    for line in f:
        #print("{}:\t{}".format(count,line))
        if "{" in line:
            count += 1
            continue
        if "}," in line:
            count -=1
            if count ==1:
                group.append(output)
                output =""
            continue
        if count >0:
            output +=line
            continue
    return group
#def get_attributes(grouping[]):
    
groups = get_segments()
for g in groups:
    print("group\n" +g)
