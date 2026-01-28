from typing import *

def daySeven():
    
    letter_map = {'T':'A','J':'B','Q':'C','K':'D','A':'E'}

    def classify(hand):
        counts = [hand.count(card) for card in hand]
        if 5 in counts:
            return 6
        if 4 in counts:
            return 5
        if 3 in counts:
            if 2 in counts:
                return 4
            return 3
        if counts.count(2) == 4:
            return 2
        if 2 in counts:
            return 1
        return 0

    def strength(hand):
        return (classify(hand), [letter_map.get(card,card) for card in hand])
    
    cards = []
    with open("Day7/7_2.txt") as file:
        for line in file:
            l,r = line.split()
            cards.append( (l,int(r)) )
    
    cards.sort( key = lambda x: strength(x[0]) )

    res = 0
    for rank, (_,bid) in enumerate(cards,1):
        res += rank*bid
    return res

def daySeven2():
    letter_map = {'T':'A','J':'.','Q':'C','K':'D','A':'E'}

    def score(hand):
        counts = [hand.count(card) for card in hand]
        if 5 in counts:
            return 6
        if 4 in counts:
            return 5
        if 3 in counts:
            if 2 in counts:
                return 4
            return 3
        if counts.count(2) == 4:
            return 2
        if 2 in counts:
            return 1
        return 0

    def replace(hand):
        if hand == "":
            return [""]
        return [x+y
                for x in ("23456789TQKA" if hand[0] == 'J' else hand[0])
                for y in replace(hand[1:])]

    def classify(hand):
        return max( map(score,replace(hand)) )

    def strength(hand):
        return (classify(hand), [letter_map.get(card,card) for card in hand])
    
    cards = []
    with open("Day7/7_2.txt") as file:
        for line in file:
            l,r = line.split()
            cards.append( (l,int(r)) )
    
    cards.sort( key = lambda x: strength(x[0]) )

    res = 0
    for rank, (_,bid) in enumerate(cards,1):
        res += rank*bid
    return res


def main():
    print("Hallo")
    print(daySeven(), "ist die Lösung von Teil 1")
    print(daySeven2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()