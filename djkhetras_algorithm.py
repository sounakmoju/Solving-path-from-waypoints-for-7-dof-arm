from collections import defaultdict
import sys
class graph:
    def __init__(self):
        self.nodes = []
        #self.edges = {k:[] for k in self.nodes}
        self.edges=defaultdict(list)
        self.distances = {}
    def printnodes(self,dis):
        for i in range(len(self.nodes)):
            print(i,dis[i])

    def add_node(self, value):
        self.nodes.append(value)
    def add_edges(self,fr_node,to_node,distance):
        self.edges[fr_node].append(to_node)
        self.distances[(fr_node,to_node)]=distance
    def minimum_index(self,dist,visited_set):
        min=9999999
        for v in range(len(self.nodes)):
            if dist[v]<min and visited_set[v]==False:
                min=dist[v]
                min_index=v
        return min_index
    def dijstra(self,ini):
        dist=[9999999]*len(self.nodes)
        dist[ini]=0
        visited_set=[False]*len(self.nodes)

        for i in range(len(self.nodes)):
            u=self.minimum_index(dist,visited_set)
            visited_set[u]=True

            for i in self.edges[u]:
                if dist[i]>dist[u]+self.distances[(u,i)]:
                    dist[i]=dist[u]+self.distances[(u,i)]
        self.printnodes(dist)

        








g=graph()
for i in range(5):
    g.add_node(i)

print(g.edges)
g.add_edges(0,1,1)
g.add_edges(0,2,6)
g.add_edges(1,2,2)
g.add_edges(1,3,1)
g.add_edges(3,4,5)
g.add_edges(2,4,5)
g.dijstra(0)

print(g.distances)

    
