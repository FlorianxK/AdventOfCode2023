from typing import *

def dayThirteen():
    res = 0

    def mirror(arr):
        for r in range(1,len(arr)):
            up = arr[:r][::-1]
            down = arr[r:]
            p1 = up[:len(down)]
            p2 = down[:len(up)]

            if p1 == p2:
                return r
        return 0

    #read
    with open("Day13/13_2.txt") as file:
        full = file.read().split("\n\n")
        
        for block in full:
            arr = block.splitlines()
            row = mirror(arr)
            res += row*100
            
            col = mirror(list(zip(*arr)))
            res += col

    return res
  
def dayThirteen2():
    res = 0

    def mirror(arr):
        for r in range(1,len(arr)):
            up = arr[:r][::-1]
            down = arr[r:]

            total = 0
            for x,y in zip(up,down):
                lineDiff = 0
                for a,b in zip(x,y):
                    if a != b:
                        lineDiff += 1
                total += lineDiff
            
            if total == 1:
                return r
        return 0

    #read
    with open("Day13/13_2.txt") as file:
        full = file.read().split("\n\n")
        
        for block in full:
            arr = block.splitlines()
            row = mirror(arr)
            res += row*100
            
            col = mirror(list(zip(*arr)))
            res += col

    return res
  

def main():
    print("Hallo")
    print(dayThirteen(), "ist die Lösung von Teil 1")
    print(dayThirteen2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()