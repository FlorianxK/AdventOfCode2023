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
    d = {}
    #read
    with open("Day19/19_2.txt") as file:
        block1,_ = file.read().split("\n\n")

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

    def count(ranges,name="in"):
        if name == "R":
            return 0
        if name == "A":
            product = 1
            for l,r in ranges.values():
                product *= r-l+1
            return product

        rules,fallback = d[name]

        res = 0
        for key,cmp,n,target in rules:
            l,r = ranges[key]
            if cmp == "<":
                trueHalf = (l,n-1)
                falseHalf = (n,r)
            else:
                trueHalf = (n+1,r)
                falseHalf = (l,n)

            if trueHalf[0] <= trueHalf[1]:
                copy = dict(ranges)
                copy[key] = trueHalf
                res += count(copy,target)
            if falseHalf[0] <= falseHalf[1]:
                ranges = dict(ranges)
                ranges[key] = falseHalf
            else:
                break
        else:
            res += count(ranges,fallback)
        return res

    return count({key:(1,4000) for key in "xmas"})

def main():
    print("Hallo")
    print(dayNineteen(), "ist die Lösung von Teil 1")
    print(dayNineteen2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()