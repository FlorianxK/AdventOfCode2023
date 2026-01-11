from collections import deque
from typing import *

def daySixteen():
    arr = []
    #read
    with open("Day16/16_2.txt") as file:
        for line in file:
            line = list(line.strip())
            for j in range(len(line)):
                if line[j] == '\\':
                    line[j] = 'b'
            arr.append(line)
    m,n = len(arr),len(arr[0])
    start = ((0,-1),(0,1))
    # pos,dir
    seen = set()
    def bfs(arr,start):
        q = deque([start])

        while True:
            nextQ = deque([])
            lastLen = len(seen)
            while q:
                coord,dir = q.popleft()
                nx,ny = coord[0]+dir[0],coord[1]+dir[1]

                if 0<=nx<m and 0<=ny<n and ((nx,ny),dir) not in seen:
                    seen.add( ((nx,ny),dir) )

                    if arr[nx][ny] == '.':
                        nextQ.append( ((nx,ny),dir) )
                    elif arr[nx][ny] == '|':
                        nextQ.append( ((nx,ny),(-1,0)) )
                        nextQ.append( ((nx,ny),(1,0)) )
                    elif arr[nx][ny] == '-':
                        nextQ.append( ((nx,ny),(0,-1)) )
                        nextQ.append( ((nx,ny),(0,1)) )
                    elif arr[nx][ny] == '/':
                        if dir == (-1,0):
                            nextQ.append( ((nx,ny),(0,1)) )
                        elif dir == (1,0):
                            nextQ.append( ((nx,ny),(0,-1)) )
                        elif dir == (0,-1):
                            nextQ.append( ((nx,ny),(1,0)) )
                        elif dir == (0,1):
                            nextQ.append( ((nx,ny),(-1,0)) )
                    elif arr[nx][ny] == 'b': # \
                        if dir == (-1,0):
                            nextQ.append( ((nx,ny),(0,-1)) )
                        elif dir == (1,0):
                            nextQ.append( ((nx,ny),(0,1)) )
                        elif dir == (0,-1):
                            nextQ.append( ((nx,ny),(-1,0)) )
                        elif dir == (0,1):
                            nextQ.append( ((nx,ny),(1,0)) )

            if lastLen == len(seen):
                break
            else:
                q = nextQ

    bfs(arr,start)
    unique = set()
    for a,_ in seen:
        unique.add(a)

    return len(unique)

def daySixteen2():
    arr = []
    #read
    with open("Day16/16_2.txt") as file:
        for line in file:
            line = list(line.strip())
            for j in range(len(line)):
                if line[j] == '\\':
                    line[j] = 'b'
            arr.append(line)
    m,n = len(arr),len(arr[0])

    # pos,dir
    def bfs(arr,start,seen):
        q = deque([start])

        while True:
            nextQ = deque([])
            lastLen = len(seen)
            while q:
                coord,dir = q.popleft()
                nx,ny = coord[0]+dir[0],coord[1]+dir[1]

                if 0<=nx<m and 0<=ny<n and ((nx,ny),dir) not in seen:
                    seen.add( ((nx,ny),dir) )

                    if arr[nx][ny] == '.':
                        nextQ.append( ((nx,ny),dir) )
                    elif arr[nx][ny] == '|':
                        nextQ.append( ((nx,ny),(-1,0)) )
                        nextQ.append( ((nx,ny),(1,0)) )
                    elif arr[nx][ny] == '-':
                        nextQ.append( ((nx,ny),(0,-1)) )
                        nextQ.append( ((nx,ny),(0,1)) )
                    elif arr[nx][ny] == '/':
                        if dir == (-1,0):
                            nextQ.append( ((nx,ny),(0,1)) )
                        elif dir == (1,0):
                            nextQ.append( ((nx,ny),(0,-1)) )
                        elif dir == (0,-1):
                            nextQ.append( ((nx,ny),(1,0)) )
                        elif dir == (0,1):
                            nextQ.append( ((nx,ny),(-1,0)) )
                    elif arr[nx][ny] == 'b': # \
                        if dir == (-1,0):
                            nextQ.append( ((nx,ny),(0,-1)) )
                        elif dir == (1,0):
                            nextQ.append( ((nx,ny),(0,1)) )
                        elif dir == (0,-1):
                            nextQ.append( ((nx,ny),(-1,0)) )
                        elif dir == (0,1):
                            nextQ.append( ((nx,ny),(1,0)) )

            if lastLen == len(seen):
                unique = set()
                for a,_ in seen:
                    unique.add(a)
                return len(unique)
            else:
                q = nextQ

    maxStart = 0
    #left and right
    for i in range(m):
        start = ((i,-1),(0,1))
        maxStart = max(maxStart,bfs(arr,start,set()))
        start = ((i,n),(0,-1))
        maxStart = max(maxStart,bfs(arr,start,set()))
    #top and bottom
    for j in range(n):
        start = ((-1,j),(1,0))
        maxStart = max(maxStart,bfs(arr,start,set()))
        start = ((m,j),(-1,0))
        maxStart = max(maxStart,bfs(arr,start,set()))

    return maxStart


def main():
    print("Hallo")
    print(daySixteen(), "ist die Lösung von Teil 1")
    print(daySixteen2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()