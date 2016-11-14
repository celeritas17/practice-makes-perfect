# are parallel edges allowed? Assume no.

import queue

class Graph:
    def __init__(self, n):
        self.n = n
        self.connections = {}
        #Assume no parallel edges
        for i in range(n):
            self.connections[i] = []
    
    def connect(self, node1, node2):
        self.connections[node1].append(node2)
        self.connections[node2].append(node1)
        
    def find_all_distances(self, s):
        edge_distance = 6
        distances = [-1]*self.n
        self.BFS_distances(s, distances)
        for d in distances:
            if d != 0:
                print((-1 if d == -1 else edge_distance*d), '', end='')
        print()
                    
    def BFS_distances(self, s, distances):
        explored = [False]*self.n # position i is a boolean telling whether that node has been explored
        explored[s] = True
        layer = 0
        q = queue.Queue()
        q.put((s, layer))
        while not q.empty():
            v, layer = q.get()
            distances[v] = layer
            layer += 1
            for w in self.connections[v]:
                if not explored[w]:
                    explored[w] = True
                    q.put((w, layer))

if __name__ == '__main__':
    num_queries = int(input())
    for i in range(num_queries):
        num_nodes,num_edges = [int(value) for value in input().split()]
        graph = Graph(num_nodes)
        for i in range(num_edges):
            u,v = [int(x) for x in input().split()]
            graph.connect(u-1,v-1) 
        s = int(input())
        graph.find_all_distances(s-1)
        