from collections import deque
from typing import *

def dayTwentyOne():
    arr = []
    i = 0
    #read
    with open("Day21/21_2.txt") as file:
        for line in file:
            arr.append(list(line.strip()))
            for j in range(len(line)):
                if line[j] == 'S':
                    start = (i,j)
            i += 1
    m,n = len(arr),len(arr[0])
    arr[start[0]][start[1]] = '.'

    def bfs(q:deque):
        nextQ = deque([])
        nxt = set()
        while q:
            curr = q.popleft()
            x,y = curr
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx,ny = x+dx,y+dy
                if 0<=nx<m and 0<=ny<n and arr[nx][ny] in '.' and (nx,ny) not in nxt:
                    nxt.add( (nx,ny) )
                    nextQ.append( (nx,ny) )

        return nextQ

    q = deque([start])
    steps = 64
    for _ in range(steps):
        q = bfs(q)

    return len(q)

def dayTwentyOne2():
    pass

def main():
    print("Hallo")
    print(dayTwentyOne(), "ist die Lösung von Teil 1")
    print(dayTwentyOne2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()