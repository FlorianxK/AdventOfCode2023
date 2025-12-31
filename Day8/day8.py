from collections import defaultdict
from math import gcd
from typing import *

def dayEight():
    res = 0
    d = defaultdict(list)
    #read
    with open("Day8/8_2.txt") as file:
        rules = list(file.readline().strip())
        file.readline()
        for line in file:
            l,r = line.strip().split(' = ')
            d[l] = r[1:-1].split(', ')

    curr = "AAA"
    while True:
        for r in rules:
            if r == 'L':
                curr = d[curr][0]
            else:
                curr = d[curr][1]
            res += 1
            if curr == "ZZZ":
                return res

def dayEight2():
    d = defaultdict(list)
    start = []
    #read
    with open("Day8/8_2.txt") as file:
        rules = list(file.readline().strip())
        file.readline()
        for line in file:
            l,r = line.strip().split(' = ')
            d[l] = r[1:-1].split(', ')
            if l[2] == 'A':
                start.append(l)

    nums = []
    for s in start:
        curr = s
        notFound = True
        res = 0
        while notFound:
            for r in rules:
                if r == 'L':
                    curr = d[curr][0]
                else:
                    curr = d[curr][1]
                res += 1
                if curr[2] == 'Z':
                    nums.append(res)
                    notFound = False

    lcm = nums.pop()
    for v in nums:
        lcm = lcm*v//gcd(lcm,v)
    
    return lcm

def main():
    print("Hallo")
    print(dayEight(), "ist die Lösung von Teil 1")
    print(dayEight2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()