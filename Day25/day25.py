import networkx as nx
from typing import *

def dayTwentyFive():
    g = nx.Graph()
    #read
    with open("Day25/25_2.txt") as file:
        for line in file:
            l,r = line.strip().split(": ")
            arr = r.split(' ')
            for a in arr:
                g.add_edge(l,a)
                g.add_edge(a,l)

    minEdges = nx.minimum_edge_cut(g)
    g.remove_edges_from(minEdges)
    left,right = nx.connected_components(g)
    return len(left)*len(right)

def main():
    print("Hallo")
    print(dayTwentyFive(), "ist die Lösung von Teil 1")
     
if __name__=="__main__":
    main()