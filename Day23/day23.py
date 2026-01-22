from typing import *

def dayTwentyThree():
    arr = []
    #read
    with open("Day23/23_2.txt") as file:
        for line in file:
            arr.append(list(line.strip()))

    m,n = len(arr),len(arr[0])
    start = (0,arr[0].index('.'))
    end = (m-1,arr[m-1].index('.'))

    points = [start,end]

    #find all crossroads
    for i in range(m):
        for j in range(n):
            if arr[i][j] == '#':
                continue
            nghs = 0
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx,ny = i+dx,j+dy
                if 0<=nx<m and 0<=ny<n and arr[nx][ny] != '#':
                    nghs += 1
            
            if nghs >= 3:
                points.append( (i,j) )
    
    dirs = {
        '^': [(-1,0)],
        'v': [(1,0)],
        '<': [(0,-1)],
        '>': [(0,1)],
        '.': [(-1,0),(1,0),(0,-1),(0,1)]
    }

    #reduce paths
    graph = {pt: {} for pt in points}
    for px,py in points:
        stack = [(0,px,py)]
        seen = {(px,py)}
        while stack:
            pos,i,j = stack.pop()

            if pos != 0 and (i,j) in points:
                graph[(px,py)][(i,j)] = pos
                continue
                
            for dx,dy in dirs[arr[i][j]]:
                nx,ny = i+dx,j+dy
                if 0<=nx<m and 0<=ny<n and arr[nx][ny] != '#' and (nx,ny) not in seen:
                    stack.append( (pos+1,nx,ny) )
                    seen.add( (nx,ny) )
    
    seen = set()

    def dfs(point):
        if point == end:
            return 0
        
        maxV = -float("inf")
        seen.add(point)
        for nx in graph[point]:
            maxV = max(maxV, dfs(nx) + graph[point][nx])
        seen.remove(point)

        return maxV
    
    return dfs(start)

def dayTwentyThree2():
    arr = []
    #read
    with open("Day23/23_2.txt") as file:
        for line in file:
            arr.append(list(line.strip()))

    m,n = len(arr),len(arr[0])
    start = (0,arr[0].index('.'))
    end = (m-1,arr[m-1].index('.'))

    points = [start,end]

    #find all crossroads
    for i in range(m):
        for j in range(n):
            if arr[i][j] == '#':
                continue
            nghs = 0
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx,ny = i+dx,j+dy
                if 0<=nx<m and 0<=ny<n and arr[nx][ny] != '#':
                    nghs += 1
            
            if nghs >= 3:
                points.append( (i,j) )

    #reduce paths
    graph = {pt: {} for pt in points}
    for px,py in points:
        stack = [(0,px,py)]
        seen = {(px,py)}
        while stack:
            pos,i,j = stack.pop()

            if pos != 0 and (i,j) in points:
                graph[(px,py)][(i,j)] = pos
                continue
                
            for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx,ny = i+dx,j+dy
                if 0<=nx<m and 0<=ny<n and arr[nx][ny] != '#' and (nx,ny) not in seen:
                    stack.append( (pos+1,nx,ny) )
                    seen.add( (nx,ny) )
    
    seen = set()

    def dfs(point):
        if point == end:
            return 0
        
        maxV = -float("inf")
        seen.add(point)
        for nx in graph[point]:
            if nx not in seen:
                maxV = max(maxV, dfs(nx) + graph[point][nx])
        seen.remove(point)

        return maxV
    
    return dfs(start)

def main():
    print("Hallo")
    print(dayTwentyThree(), "ist die Lösung von Teil 1")
    print(dayTwentyThree2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()