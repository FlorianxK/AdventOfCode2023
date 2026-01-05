from collections import deque
from typing import *

def dayTen():
    arr = []
    i = 0

    #read
    with open("Day10/10_2.txt") as file:
        for line in file:
            arr.append(list(line.rstrip()))
            for j in range(len(line)):
                if line[j] == 'S':
                    start = (i,j)
            i += 1

    m,n = len(arr),len(arr[0])
    q = deque([])
    seen = set()
    seen.add(start)
    maxDist = 0
    #first move
    for nxt in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx,ny = start[0]+nxt[0],start[1]+nxt[1]
        if 0<=nx<m and 0<=ny<n:
            if nxt == (-1,0):
                if arr[nx][ny] == '|':
                    q.append( ((nx,ny),'N',1) )
                    seen.add( (nx,ny) )
                if arr[nx][ny] == '7':
                    q.append( ((nx,ny),'W',1) )
                    seen.add( (nx,ny) ) 
                if arr[nx][ny] == 'F':
                    q.append( ((nx,ny),'E',1) )
                    seen.add( (nx,ny) )

            elif nxt == (1,0):
                if arr[nx][ny] == '|':
                    q.append( ((nx,ny),'S',1) )
                    seen.add( (nx,ny) )
                if arr[nx][ny] == 'L':
                    q.append( ((nx,ny),'E',1) )
                    seen.add( (nx,ny) ) 
                if arr[nx][ny] == 'J':
                    q.append( ((nx,ny),'W',1) )
                    seen.add( (nx,ny) )

            elif nxt == (0,-1):
                if arr[nx][ny] == '-':
                    q.append( ((nx,ny),'W',1) )
                    seen.add( (nx,ny) )
                if arr[nx][ny] == 'L':
                    q.append( ((nx,ny),'N',1) )
                    seen.add( (nx,ny) ) 
                if arr[nx][ny] == 'F':
                    q.append( ((nx,ny),'S',1) )
                    seen.add( (nx,ny) )

            elif nxt == (0,1):
                if arr[nx][ny] == '-':
                    q.append( ((nx,ny),'E',1) )
                    seen.add( (nx,ny) )
                if arr[nx][ny] == '7':
                    q.append( ((nx,ny),'S',1) )
                    seen.add( (nx,ny) ) 
                if arr[nx][ny] == 'J':
                    q.append( ((nx,ny),'N',1) )
                    seen.add( (nx,ny) )
    
    if q:
        maxDist += 1
    
    while True:
        nextQ = deque([])
        while q:
            curr,comp,dist = q.popleft()
            maxDist = max(maxDist,dist)
            x,y = curr

            if comp == 'N':
                x -= 1
                if 0<=x<m and (x,y) not in seen:
                    if arr[x][y] == '|':
                        nextQ.append( ((x,y),'N',dist+1) )
                        seen.add( (x,y) )
                    elif arr[x][y] == '7':
                        nextQ.append( ((x,y),'W',dist+1) )
                        seen.add( (x,y) ) 
                    elif arr[x][y] == 'F':
                        nextQ.append( ((x,y),'E',dist+1) )
                        seen.add( (x,y) )

            elif comp == 'S':
                x += 1
                if 0<=x<m and (x,y) not in seen:
                    if arr[x][y] == '|':
                        nextQ.append( ((x,y),'S',dist+1) )
                        seen.add( (x,y) )
                    elif arr[x][y] == 'L':
                        nextQ.append( ((x,y),'E',dist+1) )
                        seen.add( (x,y) ) 
                    elif arr[x][y] == 'J':
                        nextQ.append( ((x,y),'W',dist+1) )
                        seen.add( (x,y) )

            elif comp == 'E':
                y += 1
                if 0<=y<n and (x,y) not in seen:
                    if arr[x][y] == '-':
                        nextQ.append( ((x,y),'E',dist+1) )
                        seen.add( (x,y) )
                    elif arr[x][y] == 'J':
                        nextQ.append( ((x,y),'N',dist+1) )
                        seen.add( (x,y) ) 
                    elif arr[x][y] == '7':
                        nextQ.append( ((x,y),'S',dist+1) )
                        seen.add( (x,y) )

            elif comp == 'W':
                y -= 1
                if 0<=y<n and (x,y) not in seen:
                    if arr[x][y] == '-':
                        nextQ.append( ((x,y),'W',dist+1) )
                        seen.add( (x,y) )
                    elif arr[x][y] == 'L':
                        nextQ.append( ((x,y),'N',dist+1) )
                        seen.add( (x,y) ) 
                    elif arr[x][y] == 'F':
                        nextQ.append( ((x,y),'S',dist+1) )
                        seen.add( (x,y) )

        if nextQ:
            q = nextQ
        else:
            break
    return maxDist

def dayTen2():
    arr = []
    ngh = [(-1,0),(1,0),(0,-1),(0,1)]
    i = 0
    #read
    with open("Day10/10_2.txt") as file:
        for line in file:
            arr.append(list(line.rstrip()))
            for j in range(len(line)):
                if line[j] == 'S':
                    start = (i,j)
            i += 1

    #first find all cells of the loop
    m,n = len(arr),len(arr[0])
    q = deque([])
    seen = set()
    seen.add(start)
    #first move
    for nxt in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx,ny = start[0]+nxt[0],start[1]+nxt[1]
        if 0<=nx<m and 0<=ny<n:
            if nxt == (-1,0):
                if arr[nx][ny] == '|':
                    q.append( ((nx,ny),'N') )
                    seen.add( (nx,ny) )
                if arr[nx][ny] == '7':
                    q.append( ((nx,ny),'W') )
                    seen.add( (nx,ny) ) 
                if arr[nx][ny] == 'F':
                    q.append( ((nx,ny),'E') )
                    seen.add( (nx,ny) )

            elif nxt == (1,0):
                if arr[nx][ny] == '|':
                    q.append( ((nx,ny),'S') )
                    seen.add( (nx,ny) )
                if arr[nx][ny] == 'L':
                    q.append( ((nx,ny),'E') )
                    seen.add( (nx,ny) ) 
                if arr[nx][ny] == 'J':
                    q.append( ((nx,ny),'W') )
                    seen.add( (nx,ny) )

            elif nxt == (0,-1):
                if arr[nx][ny] == '-':
                    q.append( ((nx,ny),'W') )
                    seen.add( (nx,ny) )
                if arr[nx][ny] == 'L':
                    q.append( ((nx,ny),'N') )
                    seen.add( (nx,ny) ) 
                if arr[nx][ny] == 'F':
                    q.append( ((nx,ny),'S') )
                    seen.add( (nx,ny) )

            elif nxt == (0,1):
                if arr[nx][ny] == '-':
                    q.append( ((nx,ny),'E') )
                    seen.add( (nx,ny) )
                if arr[nx][ny] == '7':
                    q.append( ((nx,ny),'S') )
                    seen.add( (nx,ny) ) 
                if arr[nx][ny] == 'J':
                    q.append( ((nx,ny),'N') )
                    seen.add( (nx,ny) )
    
    while True:
        nextQ = deque([])
        while q:
            curr,comp = q.popleft()
            x,y = curr

            if comp == 'N':
                x -= 1
                if 0<=x<m and (x,y) not in seen:
                    if arr[x][y] == '|':
                        nextQ.append( ((x,y),'N') )
                        seen.add( (x,y) )
                    elif arr[x][y] == '7':
                        nextQ.append( ((x,y),'W') )
                        seen.add( (x,y) ) 
                    elif arr[x][y] == 'F':
                        nextQ.append( ((x,y),'E') )
                        seen.add( (x,y) )

            elif comp == 'S':
                x += 1
                if 0<=x<m and (x,y) not in seen:
                    if arr[x][y] == '|':
                        nextQ.append( ((x,y),'S') )
                        seen.add( (x,y) )
                    elif arr[x][y] == 'L':
                        nextQ.append( ((x,y),'E') )
                        seen.add( (x,y) ) 
                    elif arr[x][y] == 'J':
                        nextQ.append( ((x,y),'W') )
                        seen.add( (x,y) )

            elif comp == 'E':
                y += 1
                if 0<=y<n and (x,y) not in seen:
                    if arr[x][y] == '-':
                        nextQ.append( ((x,y),'E') )
                        seen.add( (x,y) )
                    elif arr[x][y] == 'J':
                        nextQ.append( ((x,y),'N') )
                        seen.add( (x,y) ) 
                    elif arr[x][y] == '7':
                        nextQ.append( ((x,y),'S') )
                        seen.add( (x,y) )

            elif comp == 'W':
                y -= 1
                if 0<=y<n and (x,y) not in seen:
                    if arr[x][y] == '-':
                        nextQ.append( ((x,y),'W') )
                        seen.add( (x,y) )
                    elif arr[x][y] == 'L':
                        nextQ.append( ((x,y),'N') )
                        seen.add( (x,y) ) 
                    elif arr[x][y] == 'F':
                        nextQ.append( ((x,y),'S') )
                        seen.add( (x,y) )

        if nextQ:
            q = nextQ
        else:
            break
    
    special = "|-FJL7"

    #what is S ???
    maybe_s = {'|','-','L','J','7','F'}
    for dx,dy in ngh:
        nx,ny = start[0]+dx,start[1]+dy
        if (dx,dy) == (-1,0):
            if arr[nx][ny] in "|7F":
                maybe_s &= {'|','L','J'}
        elif (dx,dy) == (1,0):
            if arr[nx][ny] in "|LJ":
                maybe_s &= {'|','7','F'}
        elif (dx,dy) == (0,-1):
            if arr[nx][ny] in "-LF":
                maybe_s &= {'-','J','7'}
        elif (dx,dy) == (0,1):
            if arr[nx][ny] in "-J7":
                maybe_s &= {'-','L','F'}
    arr[start[0]][start[1]] = maybe_s.pop()

    #replace all cells that dont belong to the loop
    for i in range(m):
        for j in range(n):
            if arr[i][j] in special and (i,j) not in seen:
                arr[i][j] = '.'

    h = {'|':[['*','|','*'],['*','|','*'],['*','|','*']], '-':[['*','*','*'],['-','-','-'],['*','*','*']], '7':[['*','*','*'],['-','7','*'],['*','|','*']] , 'F':[['*','*','*'],['*','F','-'],['*','|','*']] , 'L':[['*','|','*'],['*','L','-'],['*','*','*']] , 'J':[['*','|','*'],['-','J','*'],['*','*','*']]}
    newArr = [['.']*n*3 for _ in range(m*3)]

    for i in range(m):
        for j in range(n):
            char = arr[i][j]
            if char in special:
                for a in range(i*3,i*3+3):
                    for b in range(j*3,j*3+3):
                        newArr[a][b] = h[char][a-i*3][b-j*3]

    m,n = len(newArr),len(newArr[0])
    seen = set()
    def bfs(i,j):
        count = 1
        inside = True
        q = deque([(i,j)])
        seen.add( (i,j) )

        while q:
            curr = q.popleft()
            x,y = curr
            for dx,dy in ngh:
                nx,ny = dx+x,dy+y
                if 0<=nx<m and 0<=ny<n:
                    if newArr[nx][ny] in '.*' and (nx,ny) not in seen:
                        seen.add( (nx,ny) )
                        q.append( (nx,ny) )
                        
                        if newArr[nx][ny] == '.':
                            count += 1
                else:
                    inside = False

        if inside:
            return count
        else:
            return 0

    inloop = 0
    for i in range(m):
        for j in range(n):
            if newArr[i][j] == '.' and (i,j) not in seen:
                inloop += bfs(i,j)

    return inloop//9

def main():
    print("Hallo")
    print(dayTen(), "ist die Lösung von Teil 1")
    print(dayTen2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()