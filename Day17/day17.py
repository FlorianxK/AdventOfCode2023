from heapq import *
from typing import *

def daySeventeen():
    arr = []
    #read
    with open("Day17/17_2.txt") as file:
        for line in file:
            arr.append([int(x) for x in line.strip()])
    m,n = len(arr),len(arr[0])
    
    def djikstra(start):
        #heatloss,pos,direction,steps
        pq = [(0,start,(0,0),0)]
        heapify(pq)

        seen = set()
        while pq:
            heatloss,pos,direction,steps = heappop(pq)
            x,y = pos
            dx,dy = direction

            if pos == (m-1,n-1):
                return heatloss

            if (pos,direction,steps) in seen:
                continue
            
            seen.add( (pos,direction,steps) )

            if steps < 3 and direction != (0,0):
                nx,ny = dx+x,dy+y
                if 0<=nx<m and 0<=ny<n:
                    heappush(pq, (heatloss+arr[nx][ny],(nx,ny),direction,steps+1) )
            
            for ndx,ndy in [(1,0),(-1,0),(0,1),(0,-1)]:
                if (ndx,ndy) != (dx,dy) and (ndx,ndy) != (-dx,-dy):
                    nx,ny = ndx+x,ndy+y
                    if 0<=nx<m and 0<=ny<n:
                        heappush(pq, (heatloss+arr[nx][ny],(nx,ny),(ndx,ndy),1) )

    res = djikstra((0,0))
    return res

def daySeventeen2():
    arr = []
    #read
    with open("Day17/17_2.txt") as file:
        for line in file:
            arr.append([int(x) for x in line.strip()])
    m,n = len(arr),len(arr[0])
    
    def djikstra(start):
        #heatloss,pos,direction,steps
        pq = [(0,start,(0,0),0)]
        heapify(pq)

        seen = set()
        while pq:
            heatloss,pos,direction,steps = heappop(pq)
            x,y = pos
            dx,dy = direction

            if pos == (m-1,n-1) and steps >= 4:
                return heatloss

            if (pos,direction,steps) in seen:
                continue
            
            seen.add( (pos,direction,steps) )

            if steps < 10 and direction != (0,0):
                nx,ny = dx+x,dy+y
                if 0<=nx<m and 0<=ny<n:
                    heappush(pq, (heatloss+arr[nx][ny],(nx,ny),direction,steps+1) )
            
            if steps >= 4 or direction == (0,0):
                for ndx,ndy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    if (ndx,ndy) != (dx,dy) and (ndx,ndy) != (-dx,-dy):
                        nx,ny = ndx+x,ndy+y
                        if 0<=nx<m and 0<=ny<n:
                            heappush(pq, (heatloss+arr[nx][ny],(nx,ny),(ndx,ndy),1) )

    res = djikstra((0,0))
    return res


def main():
    print("Hallo")
    print(daySeventeen(), "ist die Lösung von Teil 1")
    print(daySeventeen2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()