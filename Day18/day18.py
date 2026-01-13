from collections import deque
from typing import *

def dayEighteen():
    input = []
    m,n = 0,0
    l,r,u,d = 0,0,0,0
    lm,rm,um,dm = 0,0,0,0
    #read
    with open("Day18/18.txt") as file:
        for line in file:
            cdir,steps,hexa = line.split(' ')
            steps = int(steps)
            input.append([cdir,steps,hexa])
            if cdir == 'R':
                r += steps
                l = max(0,l-steps)
            elif cdir == 'L':
                l += steps
                r = max(0,r-steps)
            elif cdir == 'D':
                d += steps
                u = max(0,u-steps)
            elif cdir == 'U':
                u += steps
                d = max(0,d-steps)
            lm = max(lm,l)
            rm = max(rm,r)
            dm = max(dm,d)
            um = max(um,u)
            
        m = max(um,dm)
        n = max(lm,rm)
        m += 1
        n += 1
    arr = [['.']*n for _ in range(m)]
    arr[0][0] = '#'
    ring = 0
    i,j = 0,0
    for cdir,steps,_ in input:
        ring += steps
        if cdir == 'R':
            dx,dy = (0,1)
        elif cdir == 'L':
            dx,dy = (0,-1)
        elif cdir == 'D':
            dx,dy = (1,0)
        elif cdir == 'U':
            dx,dy = (-1,0)
        
        for _ in range(steps):
            i,j = i+dx,j+dy
            arr[i][j] = '#'

    seen = set()
    def bfs(i,j):
        q = deque([(i,j)])
        seen.add((i,j))
        seenInRound = set()
        seenInRound.add( (i,j) )
        inside = True
        while q:
            curr = q.popleft()
            i,j = curr
            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                nx,ny = dx+i,dy+j
                if 0<=nx<m and 0<=ny<n:
                    if (nx,ny) in seen or arr[nx][ny] != '.':
                        continue

                    seen.add( (nx,ny) )
                    seenInRound.add( (nx,ny) )
                    q.append((nx,ny))
                else:
                    inside = False

        if inside:
            for a,b in seenInRound:
                arr[a][b] = '#'
            return len(seenInRound)
        else:
            return 0

    inside = 0
    for i in range(m):
        for j in range(n):
            if arr[i][j] == '.' and (i,j) not in seen:
                inside += bfs(i,j)

    for a in arr:
        print(''.join(a))
    return ring+inside

def dayEighteen2():
    pass

def main():
    print("Hallo")
    print(dayEighteen(), "ist die Lösung von Teil 1")
    print(dayEighteen2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()