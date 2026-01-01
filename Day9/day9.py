from collections import deque
from typing import *

def dayNine():
    res = 0
    arr = []
    #read
    with open("Day9/9_2.txt") as file:
        for line in file:
            arr.append([int(x) for x in line.strip().split(' ')])

            while True:
                nextArr = []
                allZero = True
                for i in range(1, len(arr[-1])):
                    v = arr[-1][i]-arr[-1][i-1]
                    if v != 0:
                        allZero = False
                    nextArr.append(v)

                arr.append(nextArr)
                if allZero:
                    break

            arr[-1].append(0)
            for i in range(len(arr)-2,-1,-1):
                newVal = arr[i][-1] + arr[i+1][-1]
                arr[i].append(newVal)

            res += newVal
            arr = []
    return res

def dayNine2():
    res = 0
    arr = []
    #read
    with open("Day9/9_2.txt") as file:
        for line in file:
            arr.append(deque([int(x) for x in line.strip().split(' ')]))

            while True:
                nextArr = deque([])
                allZero = True
                for i in range(1, len(arr[-1])):
                    v = arr[-1][i]-arr[-1][i-1]
                    if v != 0:
                        allZero = False
                    nextArr.append(v)

                arr.append(nextArr)
                if allZero:
                    break

            arr[-1].appendleft(0)
            for i in range(len(arr)-2,-1,-1):
                newVal = arr[i][0] - arr[i+1][0]
                arr[i].appendleft(newVal)

            res += newVal
            arr = []
    return res

def main():
    print("Hallo")
    print(dayNine(), "ist die Lösung von Teil 1")
    print(dayNine2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()