from typing import *

def dayFive():
    res = 0

    #read
    with open("Day5/5.txt") as file:
        for line in file:
            l,r = line.rstrip().split(' | ')
            

def dayFive2():
    pass

def main():
    print("Hallo")
    print(dayFive(), "ist die Lösung von Teil 1")
    print(dayFive2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()