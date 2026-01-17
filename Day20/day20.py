from collections import deque
import math
from typing import *

class Module:
    def __init__(self,name:str,type:str,outputs:list[str]):
        self.name = name
        self.type = type
        self.outputs = outputs
        
        if type == '%':
            self.memory = "off"
        elif type == '&':
            self.memory = {}
        else:
            raise Exception("Wrong type")

def dayTwenty():
    modules = {}
    broadcast_targets = []
    #read
    with open("Day20/20_2.txt") as file:
        for line in file:
            l,r = line.strip().split(" -> ")
            outputs = r.split(", ")
            if l == "broadcaster":
                broadcast_targets = outputs
            else:
                type = l[0]
                name = l[1:]
                modules[name] = Module(name,type,outputs)

    for name,module in modules.items():
        for output in module.outputs:
            if output in modules and modules[output].type == '&':
                modules[output].memory[name] = "lo"
    
    low = high = 0
    for _ in range(1000):
        low += 1
        q = deque([ ("broadcaster",x,"lo") for x in broadcast_targets ])
        while q:
            origin,target,pulse = q.popleft()
            if pulse == "lo":
                low += 1
            else:
                high += 1
            
            if target not in modules:
                continue
            
            module = modules[target]
            if module.type == '%':
                if pulse == "lo":
                    if module.memory == "off":
                        module.memory = "on"
                        outgoing = "hi"
                    elif module.memory == "on":
                        module.memory = "off"
                        outgoing = "lo"
                    for x in module.outputs:
                        q.append( (module.name,x,outgoing) )
            
            else:
                module.memory[origin] = pulse
                outgoing = "lo" if all(x == "hi" for x in module.memory.values()) else "hi"
                for x in module.outputs:
                    q.append( (module.name,x,outgoing) )

    return low*high

def dayTwenty2():
    modules = {}
    broadcast_targets = []
    #read
    with open("Day20/20_2.txt") as file:
        for line in file:
            l,r = line.strip().split(" -> ")
            outputs = r.split(", ")
            if l == "broadcaster":
                broadcast_targets = outputs
            else:
                type = l[0]
                name = l[1:]
                modules[name] = Module(name,type,outputs)

            if "rx" in outputs:
                intoRx = name

    for name,module in modules.items():
        for output in module.outputs:
            if output in modules and modules[output].type == '&':
                modules[output].memory[name] = "lo"

    cycle_len = {}
    seen = {name:0 for name,module in modules.items() if intoRx in module.outputs}
    
    presses = 0
    while True:
        presses += 1
        q = deque([ ("broadcaster",x,"lo") for x in broadcast_targets ])
        while q:
            origin,target,pulse = q.popleft()
            
            if target not in modules:
                continue
            
            module = modules[target]

            if module.name == intoRx and pulse == "hi":
                seen[origin] += 1
                if origin not in cycle_len:
                    cycle_len[origin] = presses

                if all(seen.values()):
                    x = 1
                    for cycle_l in cycle_len.values():
                        x = math.lcm(x,cycle_l)
                    return x

            if module.type == '%':
                if pulse == "lo":
                    if module.memory == "off":
                        module.memory = "on"
                        outgoing = "hi"
                    elif module.memory == "on":
                        module.memory = "off"
                        outgoing = "lo"
                    for x in module.outputs:
                        q.append( (module.name,x,outgoing) )
            
            else:
                module.memory[origin] = pulse
                outgoing = "lo" if all(x == "hi" for x in module.memory.values()) else "hi"
                for x in module.outputs:
                    q.append( (module.name,x,outgoing) )

def main():
    print("Hallo")
    print(dayTwenty(), "ist die Lösung von Teil 1")
    print(dayTwenty2(), "ist die Lösung von Teil 2")
     
if __name__=="__main__":
    main()