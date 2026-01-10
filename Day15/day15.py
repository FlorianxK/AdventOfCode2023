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
    pass

def main():
    print("Hallo")
    print(dayFifteen(), "ist die Lösung von Teil 1")
    print(dayFifteen2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()