from typing import *

def dayEleven():
    rows = []
    #read
    with open("Day11/11_2.txt") as file:
        for line in file:
            rows.append(list(line.rstrip()))
            if '#' not in line:
                rows.append(list(line.rstrip()))
    
    cols = []
    for col in zip(*rows):
        cols.append(col)
        if '#' not in col:
            cols.append(col)

    arr = []
    for a in zip(*cols):
        arr.append(list(a))

    m,n = len(arr),len(arr[0])
    galaxy = []
    num = 1
    for i in range(m):
        for j in range(n):
            if arr[i][j] == '#':
                galaxy.append( (i,j) )
                arr[i][j] = str(num)
                num += 1

    res = 0
    for i in range(len(galaxy)-1):
        x1,y1 = galaxy[i]
        for j in range(i+1,len(galaxy)):
            x2,y2 = galaxy[j]
            res += abs(x1-x2)+abs(y1-y2)
    return res

def dayEleven2():
    arr = []
    rows = []
    index = 0
    #read
    with open("Day11/11_2.txt") as file:
        for line in file:
            arr.append(list(line.rstrip()))
            if '#' not in line:
                rows.append(index)
            index += 1
    
    cols = []
    index = 0
    for col in zip(*arr):
        if '#' not in col:
            cols.append(index)
        index += 1

    m,n = len(arr),len(arr[0])
    galaxy = []
    num = 1
    for i in range(m):
        for j in range(n):
            if arr[i][j] == '#':
                galaxy.append( (i,j) )
                arr[i][j] = str(num)
                num += 1

    res = 0
    for i in range(len(galaxy)-1):
        x1,y1 = galaxy[i]
        for j in range(i+1,len(galaxy)):
            x2,y2 = galaxy[j]
            for v in rows:
                if min(x1,x2) < v < max(x1,x2):
                    res += 1000000-1
            for v in cols:
                if min(y1,y2) < v < max(y1,y2):
                    res += 1000000-1
            res += abs(x1-x2)+abs(y1-y2)
    return res

def main():
    print("Hallo")
    print(dayEleven(), "ist die Lösung von Teil 1")
    print(dayEleven2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()