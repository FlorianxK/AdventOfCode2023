from collections import defaultdict
from typing import *

def daySeven():
    cards = []
    bids = []
    #read
    with open("Day7/7.txt") as file:
        for line in file:
            l,r = line.rstrip().split(' ')
            d = defaultdict(int)
            for c in l:
                if c == 'T':
                    d[10] += 1
                elif c == 'J':
                    d[11] += 1
                elif c == 'Q':
                    d[12] += 1    
                elif c == 'K':
                    d[13] += 1
                elif c == 'A':
                    d[14] += 1
                else:
                    d[int(c)] += 1

            cards.append(d)
            bids.append(int(r))

    for c,b in zip(cards,bids):
        print(dict(c),b)
    print()

    temp = defaultdict(list)
    c:defaultdict
    for i,c in enumerate(cards):
        sVals = list(sorted(c.values(),reverse=True))
        if max(c.values()) == 5:
            temp[1].append(i)
        elif max(c.values()) == 4:
            temp[2].append(i)
        elif len(c.values()) == 2 and sVals[0] == 3 and sVals[1] == 2:
            temp[3].append(i)
        elif max(c.values()) == 3:
            temp[4].append(i)
        elif max(c.values()) == 2:
            if sVals[0] == 2 and sVals[1] == 2:
               temp[5].append(i)
            else:
                temp[6].append(i)
        elif max(c.values()) == 1:
            temp[7].append(i)
    temp = dict(sorted(temp.items()))

    def strength(hand):
        cards[hand]

    #compare is wrong because it doesnt look at highest card
    #sort function that looks at hashmap highest val then second highest
    for k,v in temp.items():
        v.sort(key = lambda v: strength(v))

    res = 0
    index = 5
    for v in temp.values():
        for val in v:
            print(bids[val])
            res += index*bids[val]
            index -= 1

    return res

def daySeven2():
    pass

def main():
    print("Hallo")
    print(daySeven(), "ist die Lösung von Teil 1")
    print(daySeven2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()