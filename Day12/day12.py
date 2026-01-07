import itertools
from typing import *

def dayTwelve():
    res = 0
    def match(curr,groups):
        pattern = []
        temp = 0
        curr.append('.')
        for c in curr:
            if c == '#':
                temp += 1
            else:
                if temp > 0:
                    pattern.append(temp)
                    temp = 0

        if groups == pattern:
            return True
        else:
            return False
    
    #read
    with open("Day12/12_2.txt") as file:
        for line in file:
            l,r = line.rstrip().split(' ')
            missing = 0
            arr = list(l)
            groups = [int(x) for x in r.split(',')]
            for v in arr:
                if v == '?':
                    missing += 1

            for comb in itertools.product(['.','#'], repeat=missing):
                index = 0
                curr = arr.copy()
                for i in range(len(curr)):
                    if curr[i] == '?':
                        curr[i] = comb[index]
                        index += 1
                if match(curr,groups):
                    res += 1
    return res
            
    

def dayTwelve2():
    pass

def main():
    print("Hallo")
    print(dayTwelve(), "ist die Lösung von Teil 1")
    #print(dayTwelve2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()