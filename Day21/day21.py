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

    def bfs(start,steps):
        q = deque([start])
        for _ in range(steps):
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
            q = nextQ
        
        return len(nextQ)

    steps = 26501365
    grid_width = steps//n-1
    odd = (grid_width//2*2+1)**2
    even = ((grid_width+1)//2*2)**2
    odd_points = bfs(start,n*2+1)
    even_points = bfs(start,n*2)

    corner_t = bfs( (n-1,start[1]) ,n-1)
    corner_r = bfs( (start[0],0)   ,n-1)
    corner_b = bfs( (0,start[1])   ,n-1)
    corner_l = bfs( (start[0],n-1) ,n-1)

    small_tr = bfs( (n-1,0)   ,n//2-1)
    small_tl = bfs( (n-1,n-1) ,n//2-1)
    small_br = bfs( (0,0)     ,n//2-1)
    small_bl = bfs( (0,n-1)   ,n//2-1)

    large_tr = bfs( (n-1,0)   ,n*3//2-1)
    large_tl = bfs( (n-1,n-1) ,n*3//2-1)
    large_br = bfs( (0,0)     ,n*3//2-1)
    large_bl = bfs( (0,n-1)   ,n*3//2-1)

    res = odd*odd_points + even*even_points + corner_b+corner_l+corner_r+corner_t+\
        (grid_width+1)*(small_tr+small_tl+small_br+small_bl)+\
        grid_width*(large_tr+large_tl+large_br+large_bl)
    return res

def main():
    print("Hallo")
    print(dayTwentyOne(), "ist die Lösung von Teil 1")
    print(dayTwentyOne2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()