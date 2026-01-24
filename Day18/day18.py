from typing import *

def dayEighteen():
    points = [(0,0)]
    dirs = {'U': (-1,0),'D': (1,0),'L': (0,-1),'R': (0,1)}
    border = 0
    #read
    with open("Day18/18_2.txt") as file:
        for line in file:
            cdir,steps,_ = line.split()
            steps = int(steps)
            dx,dy = dirs[cdir]
            x,y = points[-1]
            points.append( (x+dx*steps,y+dy*steps) )
            border += steps

    res = 0
    for i in range(len(points)):
        res += points[i][0]*( points[i-1][1]-points[(i+1)%len(points)][1] )
    res = abs(res)//2
    inside = res - border//2 + 1

    return inside+border

def dayEighteen2():
    points = [(0,0)]
    dirs = {'3': (-1,0),'1': (1,0),'2': (0,-1),'0': (0,1)}
    border = 0
    #read
    with open("Day18/18_2.txt") as file:
        for line in file:
            _,_,hexa = line.split()
            cdir = hexa[-2]
            dx,dy = dirs[cdir]
            steps = int(hexa[2:len(hexa)-2],16)
            x,y = points[-1]
            points.append( (x+dx*steps,y+dy*steps) )
            border += steps

    res = 0
    for i in range(len(points)):
        res += points[i][0]*( points[i-1][1]-points[(i+1)%len(points)][1] )
    res = abs(res)//2
    inside = res - border//2 + 1

    return inside+border

def main():
    print("Hallo")
    print(dayEighteen(), "ist die Lösung von Teil 1")
    print(dayEighteen2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()