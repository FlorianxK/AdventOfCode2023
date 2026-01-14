from typing import *

def dayNineteen():
    d = {}
    #read
    with open("Day19/19_2.txt") as file:
        block1,block2 = file.read().split("\n\n")

        for line in block1.splitlines():
            name,rest = line[:-1].split('{')
            rules = rest.split(',')
            d[name] = ([], rules.pop())
            for rule in rules:
                compare, target = rule.split(':')
                key = compare[0]
                cmp = compare[1]
                n = int(compare[2:])
                d[name][0].append( (key,cmp,n,target) )

        def correct(item,name="in"):
            if name == "R":
                return False
            if name == "A":
                return True
            
            rules,fallback = d[name]
            for key,cmp,n,target in rules:
                if eval(f"{item[key]} {cmp} {n}"):
                    return correct(item,target)
            return correct(item,fallback)

        res = 0
        for line in block2.splitlines():
            item = {}
            for segment in line[1:-1].split(','):
                ch,n = segment.split('=')
                item[ch] = int(n)
            if correct(item):
                res += sum(item.values())

        return res

def dayNineteen2():
    pass

def main():
    print("Hallo")
    print(dayNineteen(), "ist die Lösung von Teil 1")
    print(dayNineteen2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()