from typing import *

def dayFive():
    #read
    with open("Day5/5_2.txt") as file:
        seeds,*blocks = file.read().split("\n\n")
    
    seeds = [int(x) for x in seeds[7:].split(' ')]
    
    for block in blocks:
        ranges = []
        for line in block.splitlines()[1:]:
            ranges.append([int(x) for x in line.split()])
        
        nxtBlock = []
        for x in seeds:
            for a,b,c in ranges:
                if x in range(b,b+c):
                    nxtBlock.append(x-b+a)
                    break
            else:
                nxtBlock.append(x)
        seeds = nxtBlock

    return min(seeds)

def dayFive2():
    #read
    with open("Day5/5_2.txt") as file:
        inputs,*blocks = file.read().split("\n\n")

    inputs = [int(x) for x in inputs[7:].split(' ')]
    
    seeds = []
    for i in range(0,len(inputs), 2):
        seeds.append( (inputs[i],inputs[i]+inputs[i+1]) )

    for block in blocks:
        ranges = []
        for line in block.splitlines()[1:]:
            ranges.append([int(x) for x in line.split()])
        
        nxtBlock = []
        while len(seeds):
            start,end = seeds.pop()
            for a,b,c in ranges:
                overlapStart = max(start,b)
                overlapEnd = min(end,b+c)
                if overlapStart < overlapEnd:
                    nxtBlock.append( (overlapStart-b+a,overlapEnd-b+a) )
                    if overlapStart > start:
                        seeds.append( (start,overlapStart) )
                    if end > overlapEnd:
                        seeds.append( (overlapEnd,end) )
                    break
            else:
                nxtBlock.append( (start,end) )
        seeds = nxtBlock

    return min(seeds)[0]

def main():
    print("Hallo")
    print(dayFive(), "ist die Lösung von Teil 1")
    print(dayFive2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()