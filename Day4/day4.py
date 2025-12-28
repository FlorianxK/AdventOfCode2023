from typing import *

def dayFour():
    res = 0

    #read
    with open("Day4/4_2.txt") as file:
        for line in file:
            l,r = line.rstrip().split(' | ')
            vals = set()
            for x in r.split(' '):
                if x.isnumeric():
                    vals.add(int(x))
            
            l,r = l.split(': ')
            roundVal = 0
            for x in r.split(' '):
                if x.isnumeric():
                    if int(x) in vals:
                        if roundVal == 0:
                            roundVal += 1
                        else:
                            roundVal *= 2
            res += roundVal
    return res

def dayFour2():
    res = 0
    arr = []
    #read
    with open("Day4/4_2.txt") as file:
        for line in file:
            l,r = line.rstrip().split(' | ')
            vals = set()
            for x in r.split(' '):
                if x.isnumeric():
                    vals.add(int(x))
            
            l,r = l.split(': ')
            temp = []
            for x in r.split(' '):
                if x.isnumeric():
                    if int(x) in vals:
                        temp.append(int(x))
            arr.append( (vals,temp) )

    cards = [1]*len(arr)
    
    index = 1
    for vals,winners in arr:
        temp = index
        for w in winners:
            if w in vals:
                cards[temp] += 1*cards[index-1]
                temp += 1
        index += 1

    return sum(cards)

def main():
    print("Hallo")
    print(dayFour(), "ist die Lösung von Teil 1")
    print(dayFour2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()