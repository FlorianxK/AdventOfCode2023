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
    pass

def main():
    print("Hallo")
    print(dayEleven(), "ist die Lösung von Teil 1")
    print(dayEleven2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()