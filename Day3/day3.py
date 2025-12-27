from collections import deque
from typing import *

def dayThree():
    res = 0
    arr = []

    def checkDir(pos,direction):
        nx,ny = pos
        while True:
            if direction:
                ny += 1
            else:
                ny -= 1
            if 0 <= ny < n and arr[nx][ny].isnumeric():
                if direction:
                    val.append( arr[nx][ny] )
                else:
                    val.appendleft( arr[nx][ny] )
                arr[nx][ny] = '.'
            else:
                break
        return val

    #read
    with open("Day3/3_2.txt") as file:
        for line in file:
            arr.append(list(line.rstrip()))

    m,n = len(arr),len(arr[0])
    for i in range(m):
        for j in range(n):
            if arr[i][j] != '.' and not arr[i][j].isnumeric():
                for dx,dy in [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]:
                    nx,ny = i+dx,j+dy
                    if 0<=nx<m and 0<=ny<n and arr[nx][ny].isnumeric():
                        val = deque(arr[nx][ny])
                        arr[nx][ny] = '.'
                        # both or ny - or ny +
                        if ny-1 >= 0 and ny+1 < n and arr[nx][ny-1].isnumeric() and arr[nx][ny+1].isnumeric():
                            val = checkDir( (nx,ny),False )
                            val = checkDir( (nx,ny),True )

                        elif ny-1 >= 0 and arr[nx][ny-1].isnumeric():
                            #left is true
                            val = checkDir( (nx,ny),False )

                        elif ny+1 < n and arr[nx][ny+1].isnumeric():
                            #right is true
                            val = checkDir( (nx,ny),True )

                        res += int(''.join(val))

    return res

def dayThree2():
    res = 0
    arr = []

    def checkDir(pos,direction):
        nx,ny = pos
        while True:
            if direction:
                ny += 1
            else:
                ny -= 1
            if 0 <= ny < n and arr[nx][ny].isnumeric():
                if direction:
                    val.append( arr[nx][ny] )
                else:
                    val.appendleft( arr[nx][ny] )
                arr[nx][ny] = '.'
            else:
                break
        return val

    #read
    with open("Day3/3_2.txt") as file:
        for line in file:
            arr.append(list(line.rstrip()))

    m,n = len(arr),len(arr[0])
    for i in range(m):
        for j in range(n):
            if arr[i][j] != '.' and not arr[i][j].isnumeric() and arr[i][j] == '*':
                temp = []
                for dx,dy in [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]:
                    nx,ny = i+dx,j+dy
                    if 0<=nx<m and 0<=ny<n and arr[nx][ny].isnumeric():
                        val = deque(arr[nx][ny])
                        arr[nx][ny] = '.'
                        # both or ny - or ny +
                        if ny-1 >= 0 and ny+1 < n and arr[nx][ny-1].isnumeric() and arr[nx][ny+1].isnumeric():
                            val = checkDir( (nx,ny),False )
                            val = checkDir( (nx,ny),True )

                        elif ny-1 >= 0 and arr[nx][ny-1].isnumeric():
                            #left is true
                            val = checkDir( (nx,ny),False )

                        elif ny+1 < n and arr[nx][ny+1].isnumeric():
                            #right is true
                            val = checkDir( (nx,ny),True )

                        temp.append(int(''.join(val)))
                
                if len(temp) == 2:
                    res += temp[0]*temp[1]

    return res

def main():
    print("Hallo")
    print(dayThree(), "ist die Lösung von Teil 1")
    print(dayThree2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()