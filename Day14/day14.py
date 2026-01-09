from typing import *

def dayFourteen():
    res = 0
    arr = []

    #read
    with open("Day14/14_2.txt") as file:
        for line in file:
            arr.append(list(line.strip()))
    m,n = len(arr),len(arr[0])

    def moveNorth(arr):
        for j in range(n):
            rocks = 0
            for i in range(m-1,-1,-1):
                if arr[i][j] == 'O':
                    rocks += 1
                    arr[i][j] = '.'
                elif arr[i][j] == '#' and rocks == 0:
                    continue
                elif arr[i][j] == '#' and rocks > 0:
                    pos = i+1
                    while rocks > 0:
                        arr[pos][j] = 'O'
                        rocks -= 1
                        pos += 1
            while rocks > 0:
                arr[i][j] = 'O'
                rocks -= 1
                i += 1

    def count(arr):
        res = 0
        val = m
        for a in arr:
            total = 0
            for c in a:
                if c == 'O':
                    total += 1
            res += val*total
            val -= 1
        return res

    moveNorth(arr)
    res = count(arr)
    return res
  
def dayFourteen2():
    arr = []
    #read
    with open("Day14/14_2.txt") as file:
        for line in file:
            arr.append(list(line.strip()))
    m,n = len(arr),len(arr[0])

    # N = i innen m-1 -> 0, j aussen 0,n-1
    def moveNorth(arr):
        for j in range(n):
            rocks = 0
            for i in range(m-1,-1,-1):
                if arr[i][j] == 'O':
                    rocks += 1
                    arr[i][j] = '.'
                elif arr[i][j] == '#' and rocks == 0:
                    continue
                elif arr[i][j] == '#' and rocks > 0:
                    pos = i+1
                    while rocks > 0:
                        arr[pos][j] = 'O'
                        rocks -= 1
                        pos += 1
            while rocks > 0:
                arr[i][j] = 'O'
                rocks -= 1
                i += 1
    
    # E = i aussen 0 -> m-1, j innen 0,n-1
    def moveEast(arr):
        for i in range(0,m):
            rocks = 0
            for j in range(0,n):
                if arr[i][j] == 'O':
                    rocks += 1
                    arr[i][j] = '.'
                elif arr[i][j] == '#' and rocks == 0:
                    continue
                elif arr[i][j] == '#' and rocks > 0:
                    pos = j-1
                    while rocks > 0:
                        arr[i][pos] = 'O'
                        rocks -= 1
                        pos -= 1
            while rocks > 0:
                arr[i][j] = 'O'
                rocks -= 1
                j -= 1

    # S = i innen 0 -> m-1, j aussen 0,n-1
    def moveSouth(arr):
        for j in range(n):
            rocks = 0
            for i in range(0,m):
                if arr[i][j] == 'O':
                    rocks += 1
                    arr[i][j] = '.'
                elif arr[i][j] == '#' and rocks == 0:
                    continue
                elif arr[i][j] == '#' and rocks > 0:
                    pos = i-1
                    while rocks > 0:
                        arr[pos][j] = 'O'
                        rocks -= 1
                        pos -= 1
            while rocks > 0:
                arr[i][j] = 'O'
                rocks -= 1
                i -= 1

    # W = i aussen 0 -> m-1, j innen n-1,0
    def moveWest(arr):
        for i in range(0,m):
            rocks = 0
            for j in range(n-1,-1,-1):
                if arr[i][j] == 'O':
                    rocks += 1
                    arr[i][j] = '.'
                elif arr[i][j] == '#' and rocks == 0:
                    continue
                elif arr[i][j] == '#' and rocks > 0:
                    pos = j+1
                    while rocks > 0:
                        arr[i][pos] = 'O'
                        rocks -= 1
                        pos += 1
            while rocks > 0:
                arr[i][j] = 'O'
                rocks -= 1
                j += 1

    def count(arr):
        res = 0
        val = m
        for a in arr:
            total = 0
            for c in a:
                if c == 'O':
                    total += 1
            res += val*total
            val -= 1
        return res

    h = {}
    index = 1
    while True:
            moveNorth(arr)
            moveWest(arr)
            moveSouth(arr)
            moveEast(arr)
            
            #r = count(arr)
            #print(f"{i} : {r}")

            temp = arr.copy()
            for i in range(len(temp)):
                temp[i] = tuple(temp[i])
            
            if tuple(temp) not in h:
                h[tuple(temp)] = index
            else:
                print(h[tuple(temp)])
                print(index)
                wanted = 1000000000 % (index-h[tuple(temp)])
                
                for k,v in h.items():
                    if v == wanted:
                        test = list(k)
                        for i in range(len(test)):
                            test[i] = list(test[i])

                return count(test)

            index += 1

def main():
    print("Hallo")
    print(dayFourteen(), "ist die Lösung von Teil 1")
    print(dayFourteen2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()