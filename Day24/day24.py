def dayTwentyFour():
    hailstorms = []
    minA = 200000000000000
    maxA = 400000000000000
    res = 0
    #read
    with open("Day24/24_2.txt") as file:
        for line in file:
            l,r = line.strip().split(" @ ")
            p = [int(x) for x in l.split(", ")]
            v = [int(x) for x in r.split(", ")]
            hailstorms.append((p, v))

    n = len(hailstorms)
    for i in range(n):
        x1,y1,_ = hailstorms[i][0]
        vx1,vy1,_ = hailstorms[i][1]
        
        for j in range(i+1,n):
            x2,y2,_ = hailstorms[j][0]
            vx2,vy2,_ = hailstorms[j][1]
            # vx1 vy1
            # vx2 vy2
            determ = vx1*vy2-vx2*vy1

            if determ == 0:
                continue

            dx = x2-x1
            dy = y2-y1
            
            t1_num = dx*vy2 - dy*vx2
            t2_num = dx*vy1 - dy*vx1

            t1_positive = (t1_num > 0 and determ > 0) or (t1_num < 0 and determ < 0)
            t2_positive = (t2_num > 0 and determ > 0) or (t2_num < 0 and determ < 0)
            
            if t1_positive and t2_positive:
                interX = x1*determ + t1_num*vx1
                interY = y1*determ + t1_num*vy1

                if determ > 0:
                    if minA*determ <= interX <= maxA*determ and \
                        minA*determ <= interY <= maxA*determ:
                        res += 1
                else:
                    if maxA*determ <= interX <= minA*determ and \
                        maxA*determ <= interY <= minA*determ:
                        res += 1
    return res
    
def dayTwentyFour2():
    pass

def main():
    print("Hallo")
    print(dayTwentyFour(), "ist die Lösung von Teil 1")
    print(dayTwentyFour2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()