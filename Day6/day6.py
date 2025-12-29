from typing import *

def daySix():
    res = 1
    time = []
    records = []
    #read
    with open("Day6/6_2.txt") as file:
        line = file.readline()
        line = ' '.join(line.split()).split(' ')
        time = [int(x) for x in line[1:]]

        line = file.readline()
        line = ' '.join(line.split()).split(' ')
        records = [int(x) for x in line[1:]]

    for t,r in zip(time,records):
        ways = 0
        for i in range(1,t):
            tempRes = i*(t-i)
            if tempRes > r:
                ways += 1
        res *= ways
    
    return res

def daySix2():
    res = 0
    time = 0
    record = 0
    #read
    with open("Day6/6_2.txt") as file:
        line = file.readline()
        line = ''.join(line.split()).split(' ')
        line = str(line[0]).split(':')
        time = int(line[1])

        line = file.readline()
        line = ''.join(line.split()).split(' ')
        line = str(line[0]).split(':')
        record = int(line[1])

    for i in range(1,time):
        tempRes = i*(time-i)
        if tempRes > record:
            res += 1
    
    return res

def main():
    print("Hallo")
    print(daySix(), "ist die Lösung von Teil 1")
    print(daySix2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()