from typing import *
import re

def dayOne():
    res = 0
    #read
    with open("Day1/1_2.txt") as file:
        for line in file:
            vals = []
            for v in line:
                if v.isnumeric():
                    vals.append(v)
            if len(vals) > 1:
                res += int(vals[0]+vals[-1])
            elif len(vals) == 1:
                res += int(vals[0]*2)
    return res

def dayOne2():
    res = 0
    pattern = ["one","two","three","four","five","six","seven","eight","nine"]
    
    #read
    with open("Day1/1_2.txt") as file:
        for line in file:
            vals = []
            for i in range(len(line)):
                if line[i].isnumeric():
                    vals.append( (i,line[i]) )

            for i in range(len(pattern)):
                indicesTuple = [(x.start(0),str(i+1)) for x in re.finditer(pattern[i],line)]
                vals.extend(indicesTuple)
            
            vals.sort()
            if len(vals) > 1:
                res += int(vals[0][1]+vals[-1][1])
            elif len(vals) == 1:
                res += int(vals[0][1]*2)

    return res

def main():
    print("Hallo")
    print(dayOne(), "ist die Lösung von Teil 1")
    print(dayOne2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()