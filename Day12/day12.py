from typing import *

def dayTwelve():
    res = 0
    cache = {}

    def count(curr,groups):
        if curr == "":
            return 1 if groups == () else 0
        if groups == ():
            return 0 if '#' in curr else 1
        
        key = (curr,groups)

        if key in cache:
            return cache[key]

        tempRes = 0
        if curr[0] in ".?":
            tempRes += count(curr[1:],groups)
        
        if curr[0] in "#?":
            if groups[0] <= len(curr) and '.' not in curr[:groups[0]] and (groups[0] == len(curr) or curr[groups[0]] != '#'):
                tempRes += count( curr[groups[0] + 1:], groups[1:] )
        
        cache[key] = tempRes
        return tempRes
    
    #read
    with open("Day12/12_2.txt") as file:
        for line in file:
            arr,r = line.rstrip().split(' ')
            groups = tuple([int(x) for x in r.split(',')])
            
            res += count(arr, groups)
    return res
  
def dayTwelve2():
    res = 0
    cache = {}

    def count(curr,groups):
        if curr == "":
            return 1 if groups == () else 0
        if groups == ():
            return 0 if '#' in curr else 1
        
        key = (curr,groups)

        if key in cache:
            return cache[key]

        tempRes = 0
        if curr[0] in ".?":
            tempRes += count(curr[1:],groups)
        
        if curr[0] in "#?":
            if groups[0] <= len(curr) and '.' not in curr[:groups[0]] and (groups[0] == len(curr) or curr[groups[0]] != '#'):
                tempRes += count( curr[groups[0] + 1:], groups[1:] )
        
        cache[key] = tempRes
        return tempRes
    
    #read
    with open("Day12/12_2.txt") as file:
        for line in file:
            l,r = line.rstrip().split(' ')
            arr = "?".join([l]*5)
            groups = tuple([int(x) for x in r.split(',')]*5)
            
            res += count(arr, groups)
    return res

def main():
    print("Hallo")
    print(dayTwelve(), "ist die Lösung von Teil 1")
    print(dayTwelve2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()