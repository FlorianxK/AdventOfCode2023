from typing import *

def dayTwo():
    res = 0

    def checkLine(arr):
        for a in arr:
            colors = a.split(', ')
            for c in colors:
                vals = c.split(' ')
                amount = int(vals[0])
                if vals[1] == "red":
                    if amount > 12:
                        return False
                elif vals[1] == "green":
                    if amount > 13:
                        return False
                elif vals[1] == "blue":
                    if amount > 14:
                        return False
        return True

    #read
    with open("Day2/2_2.txt") as file:
        for line in file:
            line = line.rstrip()
            l,r = line.split(':')
            id1 = int(l.split(' ')[1])
            arr = r.split('; ')
            arr[0] = arr[0][1:]

            if checkLine(arr):
                res += id1

    return res

def dayTwo2():
    res = 0

    def checkLine(arr):
        maxRed,maxGreen,maxBlue = 0,0,0
        for a in arr:
            colors = a.split(', ')
            for c in colors:
                vals = c.split(' ')
                amount = int(vals[0])
                if vals[1] == "red":
                    maxRed = max(maxRed,amount)
                elif vals[1] == "green":
                    maxGreen = max(maxGreen,amount)
                elif vals[1] == "blue":
                    maxBlue = max(maxBlue,amount)
        return maxRed*maxGreen*maxBlue

    #read
    with open("Day2/2_2.txt") as file:
        for line in file:
            line = line.rstrip()
            l,r = line.split(':')
            arr = r.split('; ')
            arr[0] = arr[0][1:]

            res += checkLine(arr)

    return res

def main():
    print("Hallo")
    print(dayTwo(), "ist die Lösung von Teil 1")
    print(dayTwo2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()