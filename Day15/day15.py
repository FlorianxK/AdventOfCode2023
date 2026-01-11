from collections import defaultdict
from typing import *

def dayFifteen():
    res = 0

    def hashAlgo(word):
        val = 0
        for c in word:
            asc = ord(c)
            val += asc
            val *= 17
            val = val%256
        return val

    #read
    with open("Day15/15_2.txt") as file:
        for line in file:
            arr = [list(x) for x in line.strip().split(',')]

    for word in arr:
        res += hashAlgo(word)
    return res

def dayFifteen2():
    res = 0

    def hashAlgo(word):
        val = 0
        for c in word:
            asc = ord(c)
            val += asc
            val *= 17
            val = val%256
        return val

    #read
    with open("Day15/15_2.txt") as file:
        for line in file:
            arr = line.strip().split(',')
    
    d = defaultdict(list)
    vals = defaultdict(int)
    for word in arr:
        if word[-1] == '-':
            l = word[:len(word)-1]
            key = tuple(l)
            box = hashAlgo(l)
            if key in d[box]:
                if len(d[box]) == 1:
                    del d[box]
                else:
                    d[box].remove(key)
                del vals[key]
        else:
            l,r = word.split('=')
            key = tuple(l)
            r = int(r)
            box = hashAlgo(list(l))

            if key in d[box]:
                vals[key] = r
            else:
                d[box].append(key)
                vals[key] = r

    #calc
    for k,v in d.items():
        for i in range(len(v)):
            res += (k+1) * (i+1) * vals[v[i]]

    return res

def main():
    print("Hallo")
    print(dayFifteen(), "ist die Lösung von Teil 1")
    print(dayFifteen2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()