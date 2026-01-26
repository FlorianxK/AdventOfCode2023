from collections import deque
from typing import *

def dayTwentyTwo():
    bricks = []
    #read
    with open("Day22/22_2.txt") as file:
        for line in file:
            l,r = line.split('~')
            bricks.append( [[int(x) for x in l.split(',')],[int(x) for x in r.split(',')]] )

    n = len(bricks)
    bricks.sort(key=lambda brick: brick[0][2])
    
    def overlaps(brick1,brick2):
        a,lateA = brick1
        b,lateB = brick2
        return max(a[0],b[0]) <= min(lateA[0],lateB[0]) and max(a[1],b[1]) <= min(lateA[1],lateB[1])

    for index,brick in enumerate(bricks):
        max_z = 1
        for check in bricks[:index]:
            if overlaps(brick,check):
                max_z = max(max_z,check[1][2] + 1)
        brick[1][2] -= brick[0][2] - max_z
        brick[0][2] = max_z

    bricks.sort(key=lambda brick: brick[0][2])

    k_supports_v = {i: set() for i in range(n)}
    v_supports_k = {i: set() for i in range(n)}

    for j,upper in enumerate(bricks):
        for i,lower in enumerate(bricks[:j]):
            if overlaps(lower,upper) and upper[0][2] == lower[1][2]+1:
                k_supports_v[i].add(j)
                v_supports_k[j].add(i)
    
    res = 0
    for i in range(n):
        if all( len(v_supports_k[j]) >= 2 for j in k_supports_v[i] ):
            res += 1
    return res

def dayTwentyTwo2():
    bricks = []
    #read
    with open("Day22/22_2.txt") as file:
        for line in file:
            l,r = line.split('~')
            bricks.append( [[int(x) for x in l.split(',')],[int(x) for x in r.split(',')]] )

    n = len(bricks)
    bricks.sort(key=lambda brick: brick[0][2])
    
    def overlaps(brick1,brick2):
        a,lateA = brick1
        b,lateB = brick2
        return max(a[0],b[0]) <= min(lateA[0],lateB[0]) and max(a[1],b[1]) <= min(lateA[1],lateB[1])

    for index,brick in enumerate(bricks):
        max_z = 1
        for check in bricks[:index]:
            if overlaps(brick,check):
                max_z = max(max_z,check[1][2] + 1)
        brick[1][2] -= brick[0][2] - max_z
        brick[0][2] = max_z

    bricks.sort(key=lambda brick: brick[0][2])

    k_supports_v = {i: set() for i in range(n)}
    v_supports_k = {i: set() for i in range(n)}

    for j,upper in enumerate(bricks):
        for i,lower in enumerate(bricks[:j]):
            if overlaps(lower,upper) and upper[0][2] == lower[1][2]+1:
                k_supports_v[i].add(j)
                v_supports_k[j].add(i)
    
    res = 0
    for i in range(n):
        q = deque(j for j in k_supports_v[i] if len(v_supports_k[j]) == 1)
        falling = set(q)
        falling.add(i)

        while q:
            j = q.popleft()
            for k in k_supports_v[j] - falling:
                if v_supports_k[k] <= falling:
                    q.append(k)
                    falling.add(k)
        res += len(falling)-1

    return res

def main():
    print("Hallo")
    print(dayTwentyTwo(), "ist die Lösung von Teil 1")
    print(dayTwentyTwo2(), "ist die Lösung von Teil 2")

if __name__=="__main__":
    main()